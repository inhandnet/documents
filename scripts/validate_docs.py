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

# API configuration
API_BASE_URL = "https://cloud-dev.poweris.inhand.online"
API_ENDPOINT = "/api/plm/github/product/published-files"
API_TOKEN = "b4ae9d11-dd4d-40e5-931f-3480e8c20c63"

# Valid languages
VALID_LANGS = {"zh", "en"}

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

    # Fallback to environment variable
    email = os.environ.get("NOTIFY_EMAIL")
    if email:
        return email

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
    # Normalize paths - keep language prefix for forbid API
    normalized = []
    for f in file_list:
        parts = list(f.parts)
        if len(parts) >= 2 and parts[0] == "docs" and len(parts) >= 3:
            lang = parts[1]
            if lang in VALID_LANGS:
                # Remove lang prefix: FWA02-NAVA/FAQ/xxx.md (without zh/)
                norm = "/".join(parts[2:])
                normalized.append(norm)

    if not normalized:
        print("[INFO] No files to forbid")
        return True

    # Forbid API endpoint
    url = f"{API_BASE_URL}/api/plm/github/product/published-files/forbid"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    print(f"=== Forbidding {len(normalized)} deleted files ===")

    success_count = 0
    fail_count = 0

    for path in normalized:
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
                success_count += 1
            else:
                print(f"    [WARN] Unexpected response: {result}")
                fail_count += 1

        except requests.exceptions.RequestException as e:
            print(f"    [FAIL] Failed to forbid: {e}")
            fail_count += 1

    print(f"\nForbid complete: {success_count} success, {fail_count} failed")
    return fail_count == 0

    if not normalized:
        print("[INFO] No files to forbid")
        return True

    # Forbid API endpoint
    url = f"{API_BASE_URL}/api/plm/github/product/published-files/forbid"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    print(f"=== Forbidding {len(normalized)} deleted files ===")

    success_count = 0
    fail_count = 0

    for path in normalized:
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
                success_count += 1
            else:
                print(f"    [WARN] Unexpected response: {result}")
                fail_count += 1

        except requests.exceptions.RequestException as e:
            print(f"    [FAIL] Failed to forbid: {e}")
            fail_count += 1

    print(f"\nForbid complete: {success_count} success, {fail_count} failed")
    return fail_count == 0


def validate_files(file_list: List[Path]) -> bool:
    """Validate files via API.

    Args:
        file_list: List of file paths to validate

    Returns:
        True if all files are valid, False otherwise
    """
    # Normalize paths
    normalized = []
    for f in file_list:
        norm = normalize_path(f)
        if norm:
            try:
                size = f.stat().st_size
                normalized.append({"path": norm, "size": size})
            except FileNotFoundError:
                print(f"  [WARN] File not found: {f}")

    if not normalized:
        print("[INFO] No files to validate")
        return True

    # Prepare API request
    url = f"{API_BASE_URL}{API_ENDPOINT}"
    commit_id = get_git_commit_id()
    email = get_notify_email()

    params = {"email": email}
    if commit_id:
        params["commitId"] = commit_id

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    print(f"=== Validating {len(normalized)} files ===")
    for item in normalized:
        print(f"  - {item['path']} ({item['size']} bytes)")

    try:
        response = requests.post(
            url,
            headers=headers,
            params=params,
            json=normalized,
            timeout=60,
        )
        response.raise_for_status()
        result = response.json()

        # Check for API error in response body
        if 'error' in result and result['error']:
            print(f"\n[FAIL] Validation failed:")
            print(f"Error: {result['error']}")
            if 'result' in result:
                print(f"Details: {result['result']}")
            return False

        print(f"\n[OK] Validation passed")
        print(f"Response: {result}")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"\n[FAIL] Validation failed: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return False

    except requests.exceptions.RequestException as e:
        print(f"\n[FAIL] Request failed: {e}")
        return False


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

    print("[ERROR] Must specify --diff or --file")
    sys.exit(1)


if __name__ == "__main__":
    main()
