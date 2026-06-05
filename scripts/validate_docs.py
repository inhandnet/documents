#!/usr/bin/env python3
"""Validate docs paths via API.

Validates changed files in docs/ directory against the backend API.
Only processes files under zh/ or en/ subdirectories.

Usage:
    python scripts/validate_docs.py --diff          # Validate changed files
    python scripts/validate_docs.py --file path     # Validate single file
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

import requests

# API endpoint (same for both zh and en)
API_ENDPOINT = "/api/plm/github/product/published-files"

# Valid languages
VALID_LANGS = {"zh", "en"}


def get_api_config(lang: str) -> dict:
    """Get API config for the given language."""
    env_url = f"PLM_API_{lang.upper()}_URL"
    env_token = f"PLM_API_{lang.upper()}_TOKEN"
    url = os.environ.get(env_url, "")
    token = os.environ.get(env_token, "")

    if not url:
        print(f"[ERROR] {env_url} environment variable is not set")
        sys.exit(1)
    if not token:
        print(f"[ERROR] {env_token} environment variable is not set")
        sys.exit(1)

    return {"url": url, "token": token}

# Excluded files
EXCLUDED_FILES = {".gitkeep", "index.md"}
EXCLUDED_DIRS = {"img", "images", "assets", "javascripts", "stylesheets"}


def get_git_commit_id() -> Optional[str]:
    """Get current git commit ID (short format)."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_changed_files() -> List[Path]:
    """Get changed files in docs/ directory.

    Uses GITHUB_BASE_REF and GITHUB_HEAD_REF for PR mode,
    or HEAD~1..HEAD for push mode.
    """
    base_ref = os.environ.get("GITHUB_BASE_REF")
    head_ref = os.environ.get("GITHUB_HEAD_REF")

    if base_ref and head_ref:
        # PR mode: compare base branch with head branch
        cmd = ["git", "-c", "core.quotePath=false", "diff", "--name-only", f"origin/{base_ref}", f"origin/{head_ref}"]
    else:
        # Push mode: compare last commit
        cmd = ["git", "-c", "core.quotePath=false", "diff", "--name-only", "HEAD~1", "HEAD"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        files = [Path(f) for f in result.stdout.strip().split("\n") if f]
        # Filter only docs/ files
        return [f for f in files if str(f).startswith("docs/")]
    except subprocess.CalledProcessError:
        return []


def get_deleted_files() -> List[Path]:
    """Get deleted files in docs/ directory.

    Returns files with status 'D' (deleted) from git diff.
    """
    base_ref = os.environ.get("GITHUB_BASE_REF")
    head_ref = os.environ.get("GITHUB_HEAD_REF")

    if base_ref and head_ref:
        # PR mode
        cmd = ["git", "-c", "core.quotePath=false", "diff", "--name-status", f"origin/{base_ref}", f"origin/{head_ref}"]
    else:
        # Push mode - use GITHUB_EVENT_PATH to get before/after sha
        before_sha = os.environ.get("GITHUB_EVENT_BEFORE")
        after_sha = os.environ.get("GITHUB_SHA", "HEAD")
        if before_sha:
            cmd = ["git", "-c", "core.quotePath=false", "diff", "--name-status", before_sha, after_sha]
        else:
            # Fallback to last commit only
            cmd = ["git", "-c", "core.quotePath=false", "diff", "--name-status", "HEAD~1", "HEAD"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"[DEBUG] git diff output: {repr(result.stdout)}")
        deleted = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            # Format: "D\tfilepath" or "M\tfilepath" or "A\tfilepath"
            parts = line.split("\t", 1)
            if len(parts) == 2:
                status, filepath = parts
                if status == "D" and filepath.startswith("docs/"):
                    deleted.append(Path(filepath))
        return deleted
    except subprocess.CalledProcessError:
        return []


def normalize_path(file_path: Path) -> Optional[str]:
    """Normalize path for API validation.

    Input: docs/zh/EAP600/Manual/doc.md
    Output: EAP600/Manual/doc.md

    Returns None if file should be skipped.
    """
    parts = list(file_path.parts)

    # Must start with docs/
    if len(parts) < 2 or parts[0] != "docs":
        return None

    # Check language prefix
    if len(parts) < 3:
        return None

    lang = parts[1]
    if lang not in VALID_LANGS:
        return None

    # Skip excluded directories
    for part in parts:
        if part in EXCLUDED_DIRS:
            return None

    # Skip excluded files
    if parts[-1] in EXCLUDED_FILES:
        return None

    # Skip image files
    ext = Path(parts[-1]).suffix.lower()
    if ext in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}:
        return None

    # datasheets directory: only allow PDF files
    if any(p.lower() == "datasheets" for p in parts) and ext != ".pdf":
        return None

    # Join remaining parts (remove docs/ and language prefix)
    return "/".join(parts[2:])


def get_notify_email() -> str:
    """Get notification email.

    Priority:
    1. config.json notify_emails
    2. Environment variable NOTIFY_EMAIL
    3. git config user.email
    4. Default: github-actions@inhand.com
    """
    # Try config.json first
    config_path = Path(__file__).parent.parent / "config.json"
    if config_path.exists():
        try:
            import json
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
            emails = config.get("notify_emails", [])
            if emails:
                return ",".join(emails)
        except (json.JSONDecodeError, IOError):
            pass

    # Fallback to environment variable (comma-separated emails)
    emails = os.environ.get("NOTIFY_EMAILS")
    if emails:
        return emails

    # Fallback to git config
    try:
        result = subprocess.run(
            ["git", "config", "user.email"],
            capture_output=True,
            text=True,
            check=True,
        )
        email = result.stdout.strip()
        if email:
            return email
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return "github-actions@inhand.com"


def forbid_files(file_list: List[Path]) -> bool:
    """Forbid (disable) deleted files via API.

    Args:
        file_list: List of deleted file paths to forbid

    Returns:
        True if all files are successfully forbidden, False otherwise
    """
    # Normalize paths - group by language
    by_lang = {}  # lang -> [(norm, original_path)]
    for f in file_list:
        parts = list(f.parts)
        if len(parts) >= 2 and parts[0] == "docs" and len(parts) >= 3:
            lang = parts[1]
            if lang in VALID_LANGS:
                # Skip excluded directories (images, assets, javascripts, stylesheets, etc.)
                if any(part in EXCLUDED_DIRS for part in parts):
                    continue
                # Skip excluded files
                if parts[-1] in EXCLUDED_FILES:
                    continue
                # Skip image files
                ext = Path(parts[-1]).suffix.lower()
                if ext in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}:
                    continue
                # datasheets directory: only allow PDF files
                if any(p.lower() == "datasheets" for p in parts) and ext != ".pdf":
                    continue
                # Remove lang prefix: FWA02-NAVA/FAQ/xxx.md (without zh/)
                norm = "/".join(parts[2:])
                by_lang.setdefault(lang, []).append(norm)

    if not by_lang:
        print("[INFO] No files to forbid")
        return True

    total_success = 0
    total_count = 0

    for lang, paths in by_lang.items():
        config = get_api_config(lang)
        url = f"{config['url']}/api/plm/github/product/published-files/forbid"
        headers = {
            "Authorization": f"Bearer {config['token']}",
            "Content-Type": "application/json",
        }

        print(f"=== Forbidding {len(paths)} deleted files ({lang}) ===")
        total_count += len(paths)

        for path in paths:
            print(f"  - {path}")
            try:
                response = requests.put(
                    url,
                    headers=headers,
                    json={"path": path},
                    timeout=30,
                )
                response.raise_for_status()
                result = response.json()

                if result.get("status") == 200:
                    print(f"    [OK] Forbidden successfully")
                    total_success += 1
                else:
                    print(f"    [WARN] Unexpected response: {result} — skipped")

            except requests.exceptions.RequestException as e:
                print(f"    [WARN] Failed to forbid: {e} — skipped")

    print(f"\nForbid complete: {total_success}/{total_count} success")
    return True


def validate_files(file_list: List[Path]) -> bool:
    """Validate files via API.

    Args:
        file_list: List of file paths to validate

    Returns:
        True if all files are valid, False otherwise
    """
    # Normalize paths and group by language
    by_lang = {}  # lang -> [{"path": norm, "size": size}]
    file_map = {}  # norm -> Path
    for f in file_list:
        norm = normalize_path(f)
        if norm:
            try:
                size = f.stat().st_size
                # Get language from path: docs/zh/... or docs/en/...
                lang = f.parts[1] if len(f.parts) >= 2 else ""
                if lang in VALID_LANGS:
                    by_lang.setdefault(lang, []).append({"path": norm, "size": size})
                    file_map[norm] = f
            except FileNotFoundError:
                print(f"  [WARN] File not found: {f}")

    if not by_lang:
        print("[INFO] No files to validate")
        return True

    commit_id = get_git_commit_id()
    email = get_notify_email()

    for lang, items in by_lang.items():
        config = get_api_config(lang)
        url = f"{config['url']}{API_ENDPOINT}"

        params = {"email": email}
        if commit_id:
            params["commitId"] = commit_id

        headers = {
            "Authorization": f"Bearer {config['token']}",
            "Content-Type": "application/json",
        }

        print(f"=== Validating {len(items)} files ({lang}) ===")
        for item in items:
            print(f"  - {item['path']} ({item['size']} bytes)")

        try:
            response = requests.post(
                url,
                headers=headers,
                params=params,
                json=items,
                timeout=60,
            )
            response.raise_for_status()
            result = response.json()

        except requests.exceptions.RequestException as e:
            print(f"\n[WARN] Validation request failed ({lang}): {e}")
            continue

        # Check for API error in response body
        if 'error' in result and result['error']:
            print(f"\n[WARN] Validation returned errors ({lang}):")
            # Parse failed paths from result field (list of strings like "path格式错误：...")
            failed_paths = set()
            import re
            for detail in result.get('result', []):
                # Extract path before "格式错误"
                m = re.match(r'^(.+?)格式错误[：:]', str(detail))
                if m:
                    failed_paths.add(m.group(1))
                print(f"  - {detail}")

            for item in items:
                path = item['path']
                f = file_map.get(path)
                if path in failed_paths and f and f.exists():
                    print(f"  [DELETE] Removing invalid file: {f}")
                    f.unlink()

            passed = len(items) - len(failed_paths)
            print(f"\nValidation complete ({lang}): {passed} passed, {len(failed_paths)} failed (removed)")
        else:
            print(f"\n[OK] Validation passed ({lang})")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Validate docs paths via API"
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Validate changed files via git diff",
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="Validate single file",
    )
    parser.add_argument(
        "--forbid-deleted",
        action="store_true",
        help="Forbid (disable) deleted files via API (only for push events)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all files under docs/",
    )
    args = parser.parse_args()

    # Handle single file validation
    if args.file:
        files = [args.file]
        success = validate_files(files)
        sys.exit(0 if success else 1)

    # Handle forbid deleted mode (standalone)
    if args.forbid_deleted:
        deleted_files = get_deleted_files()
        if deleted_files:
            forbid_success = forbid_files(deleted_files)
            if not forbid_success:
                sys.exit(1)
        else:
            print("[INFO] No deleted files in docs/")
        sys.exit(0)

    # Handle git diff mode (validate only)
    if args.diff:
        files = get_changed_files()
        if files:
            success = validate_files(files)
            if not success:
                sys.exit(1)
        else:
            print("[INFO] No changed files in docs/")
        sys.exit(0)

    # Handle validate all files
    if args.all:
        files = get_all_files()
        if files:
            print(f"[INFO] Found {len(files)} files to validate")
            success = validate_files(files)
            if not success:
                sys.exit(1)
        else:
            print("[INFO] No files found in docs/")
        sys.exit(0)

    print("[ERROR] Must specify --diff, --file, or --all")
    sys.exit(1)


def get_all_files() -> List[Path]:
    """Get all files under docs/ directory that should be validated."""
    docs_dir = Path("docs")
    if not docs_dir.exists():
        return []

    files = []
    for file_path in docs_dir.rglob("*"):
        if file_path.is_file() and normalize_path(file_path):
            files.append(file_path)

    return files


if __name__ == "__main__":
    main()
