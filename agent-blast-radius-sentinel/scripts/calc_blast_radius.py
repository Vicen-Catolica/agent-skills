#!/usr/bin/env python3
"""
Blast Radius Calculator Helper Script
Searches for symbol occurrences, imports, and dependent call sites
across the repository to evaluate the potential collateral impact of a modification.
"""

import os
import re
import sys

def calculate_blast_radius(repo_root: str, target_symbol: str, target_file: str = ""):
    occurrences = []
    symbol_pattern = re.compile(r"\b" + re.escape(target_symbol) + r"\b")

    ignored_dirs = {".git", "node_modules", "venv", ".venv", "bin", "obj", "__pycache__", "dist", "build"}
    valid_exts = {".py", ".ts", ".js", ".tsx", ".jsx", ".cs", ".go", ".java", ".json", ".sql", ".md"}

    total_files_scanned = 0
    impacted_files = set()

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in valid_exts:
                total_files_scanned += 1
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, repo_root)

                if target_file and rel_path == target_file:
                    continue

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as file_obj:
                        for line_num, line in enumerate(file_obj, start=1):
                            if symbol_pattern.search(line):
                                impacted_files.add(rel_path)
                                occurrences.append((rel_path, line_num, line.strip()))
                except Exception:
                    pass

    return total_files_scanned, impacted_files, occurrences

def main():
    if len(sys.argv) < 3:
        print("Usage: calc_blast_radius.py <repo_root> <target_symbol> [target_file]")
        sys.exit(1)

    repo_root = sys.argv[1]
    target_symbol = sys.argv[2]
    target_file = sys.argv[3] if len(sys.argv) > 3 else ""

    print(f"=== BLAST RADIUS SENTINEL REPORT ===")
    print(f"Target Symbol: '{target_symbol}'")
    print(f"Scanning from: {repo_root}")

    total_scanned, impacted_files, occurrences = calculate_blast_radius(repo_root, target_symbol, target_file)

    print(f"Total Files Scanned: {total_scanned}")
    print(f"Impacted Dependent Files: {len(impacted_files)}")
    print(f"Total Call Sites / Usages: {len(occurrences)}")
    print("---------------------------------------")

    if not impacted_files:
        print("[LOW RISK] Symbol has no external usages found outside target file.")
    elif len(impacted_files) <= 3:
        print("[MODERATE RISK] Localized blast radius. Impacted files:")
        for f in sorted(impacted_files):
            print(f"  - {f}")
    else:
        print(f"[HIGH RISK] Critical blast radius! {len(impacted_files)} dependent files detected:")
        for f in sorted(impacted_files)[:10]:
            print(f"  - {f}")
        if len(impacted_files) > 10:
            print(f"  ... and {len(impacted_files) - 10} more files.")

    print("\nSample Call Sites:")
    for file_path, line_no, code in occurrences[:5]:
        print(f"  {file_path}:{line_no} -> {code}")
    print("=======================================")

if __name__ == "__main__":
    main()
