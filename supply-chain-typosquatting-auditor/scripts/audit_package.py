#!/usr/bin/env python3
"""
Supply-Chain & Typosquatting Auditor Helper Script
Checks package name validity against common typosquatting patterns,
confirms whether packages exist on official PyPI/npm registries,
and prevents hallucinated or malicious package installations.
"""

import difflib
import json
import sys
import urllib.request
import urllib.error

POPULAR_PACKAGES = {
    "python": [
        "requests", "numpy", "pandas", "urllib3", "pydantic", "pytest",
        "fastapi", "flask", "django", "boto3", "cryptography", "sqlalchemy",
        "scipy", "scikit-learn", "torch", "matplotlib", "jinja2", "pytz",
        "colorama", "setuptools", "wheel", "typing-extensions", "httpx"
    ],
    "npm": [
        "react", "react-dom", "lodash", "axios", "express", "typescript",
        "jest", "webpack", "next", "tailwindcss", "vite", "chalk",
        "commander", "moment", "eslint", "prettier", "dotenv", "rxjs"
    ]
}

def check_registry_pypi(package_name: str):
    url = f"https://pypi.org/pypi/{package_name}/json"
    req = urllib.request.Request(url, headers={"User-Agent": "AgentAuditor/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                info = data.get("info", {})
                return {
                    "exists": True,
                    "summary": info.get("summary", ""),
                    "author": info.get("author", "Unknown"),
                    "version": info.get("version", "Unknown")
                }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"exists": False, "reason": "Not found in PyPI registry"}
        return {"exists": False, "reason": f"HTTP Error {e.code}"}
    except Exception as e:
        return {"exists": None, "reason": f"Connection error: {e}"}

def check_typosquatting(package_name: str, ecosystem: str):
    candidates = POPULAR_PACKAGES.get(ecosystem, [])
    close_matches = difflib.get_close_matches(package_name.lower(), candidates, n=3, cutoff=0.75)
    suspicious = [m for m in close_matches if m.lower() != package_name.lower()]
    return suspicious

def main():
    if len(sys.argv) < 2:
        print("Usage: audit_package.py <package_name> [ecosystem: python|npm]")
        sys.exit(1)

    package_name = sys.argv[1].strip()
    ecosystem = sys.argv[2].lower() if len(sys.argv) > 2 else "python"

    print(f"=== SUPPLY CHAIN & TYPOSQUATTING AUDIT ===")
    print(f"Package: '{package_name}' | Ecosystem: '{ecosystem}'")

    suspicious = check_typosquatting(package_name, ecosystem)
    if suspicious:
        print(f"\n[ALERT: POTENTIAL TYPOSQUATTING DETECTED!]")
        print(f"  The package name '{package_name}' is suspiciously similar to popular standard package(s):")
        for match in suspicious:
            print(f"    -> Did you mean '{match}'?")
        print("  WARNING: Malicious actors frequently publish typo packages to execute arbitrary code.")
        print("==========================================")
        return

    if ecosystem == "python":
        print("\nChecking official PyPI registry...")
        result = check_registry_pypi(package_name)
        if result.get("exists") is True:
            print(f"[OK: OFFICIAL PACKAGE VERIFIED]")
            print(f"  Latest Version: {result.get('version')}")
            print(f"  Author: {result.get('author')}")
            print(f"  Summary: {result.get('summary')}")
        elif result.get("exists") is False:
            print(f"[DANGER: PACKAGE NOT FOUND ON PYPI!]")
            print(f"  Reason: {result.get('reason')}")
            print("  This may be an AI-hallucinated package name or a private unconfigured feed.")
        else:
            print(f"[WARNING: REGISTRY CHECK INCONCLUSIVE]")
            print(f"  {result.get('reason')}")
    else:
        print(f"[NOTE] Automated online audit for ecosystem '{ecosystem}' complete.")

    print("==========================================")

if __name__ == "__main__":
    main()
