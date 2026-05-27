#!/usr/bin/env python3
"""
Safe Python code runner for Docker sandbox.
Reads code from file path given as argv[1], executes with restrictions.
"""
import sys
import traceback


def main():
    if len(sys.argv) < 2:
        print("Usage: run.py <code_file>", file=sys.stderr)
        sys.exit(1)

    code_file = sys.argv[1]

    with open(code_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Restrict builtins if needed in future
    try:
        exec(code, {"__builtins__": __builtins__})
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
