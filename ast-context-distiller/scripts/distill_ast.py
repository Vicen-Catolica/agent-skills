#!/usr/bin/env python3
"""
AST Context Distiller Helper Script
Extracts concise public interfaces, class structures, method signatures,
and type annotations while stripping implementation bodies to minimize token usage.
"""

import ast
import os
import re
import sys

def distill_python(source_code: str) -> str:
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return "// SyntaxError: Unable to parse Python AST. Showing truncated preview."

    class InterfaceStripper(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            docstring = ast.get_docstring(node)
            new_body = []
            if docstring:
                new_body.append(ast.Expr(value=ast.Constant(value=f"\"\"\"{docstring}\"\"\"")))
            new_body.append(ast.Pass())
            node.body = new_body
            return node

        def visit_AsyncFunctionDef(self, node):
            return self.visit_FunctionDef(node)

    stripper = InterfaceStripper()
    pruned_tree = stripper.visit(tree)
    ast.fix_missing_locations(pruned_tree)
    try:
        return ast.unparse(pruned_tree)
    except Exception:
        # Fallback for Python versions where unparse is missing or fails
        return "\n".join(
            line for line in source_code.splitlines()
            if line.strip().startswith(("def ", "class ", "async def ", "@", "import ", "from "))
        )

def distill_generic(source_code: str) -> str:
    """Fallback signature extractor for JS, TS, C#, Go, Java."""
    lines = source_code.splitlines()
    distilled = []
    signature_patterns = [
        r"^(export\s+)?(default\s+)?(interface|type|class|enum)\s+",
        r"^(export\s+)?(async\s+)?function\s+",
        r"^(public|private|protected|static|readonly|async|\s*func)\s+",
        r"^import\s+",
        r"^package\s+",
        r"^namespace\s+",
    ]
    combined_regex = re.compile("|".join(signature_patterns))

    in_block = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if combined_regex.search(stripped):
            distilled.append(line)
        elif stripped.startswith(("/**", "/*", "*", "///")):
            distilled.append(line)

    return "\n".join(distilled) if distilled else source_code[:1000]

def main():
    if len(sys.argv) < 2:
        print("Usage: distill_ast.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.", file_color="red")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".py":
        output = distill_python(content)
    else:
        output = distill_generic(content)

    print(f"// --- AST DISTILLED INTERFACE: {os.path.basename(file_path)} ---")
    print(output)
    print(f"// --- END OF DISTILLED INTERFACE ---")

if __name__ == "__main__":
    main()
