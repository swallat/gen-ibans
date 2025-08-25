#!/usr/bin/env python3
"""
Utility to append a single informational line ("Weitere Informationen: ...")
to each Markdown prompt in prompts/methods/generated.

- Idempotent: will not add the line if it already exists in the file.
- Encoding: uses UTF-8 for reading and writing.
- Placement: appends the line at the very end of the file (ensuring a newline before it if needed).

Usage:
    python add_info_to_prompts.py
    python add_info_to_prompts.py --text "Weitere Informationen: <your text>"
    python add_info_to_prompts.py --dir prompts\\methods\\generated

Notes:
- The default text is meant to be generic. You can override it via --text.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_TEXT = (
    "Weitere Informationen: Diese Prompt-Vorlage ist Teil der generierten Methoden-Prompts. "
    "Für Details siehe die Bundesbank-Spezifikation und die Hinweise im Projekt-README."
)


def append_info_line(file_path: Path, info_line: str) -> bool:
    """Append info_line to file_path if not already present.

    Returns True if the file was modified, False otherwise.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Fallback: try reading with latin-1 to avoid crash, then rewrite as utf-8
        content = file_path.read_text(encoding="latin-1")

    # If the exact line already exists anywhere, skip to keep idempotent
    if info_line in content.splitlines():
        return False

    # Ensure newline before appending the new line
    if content and not content.endswith("\n"):
        content += "\n"

    content += info_line + "\n"

    # Write back in UTF-8
    file_path.write_text(content, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Append additional info to generated prompts.")
    parser.add_argument(
        "--dir",
        default=str(Path("") / "methods" / "generated"),
        help="Directory containing generated prompt files (default: prompts\\methods\\generated)",
    )
    parser.add_argument(
        "--ext",
        default=".md",
        help="File extension to process (default: .md)",
    )
    parser.add_argument(
        "--text",
        default=DEFAULT_TEXT,
        help="The exact single line of text to append (default: a generic German info line)",
    )
    args = parser.parse_args(argv)

    target_dir = Path(args.dir)
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: directory not found: {target_dir}", file=sys.stderr)
        return 2

    info_line = args.text.strip().replace("\r", "")
    if "\n" in info_line:
        print("Error: --text must be a single line (no newlines).", file=sys.stderr)
        return 2

    modified = 0
    processed = 0

    for path in sorted(target_dir.glob(f"*{args.ext}")):
        if not path.is_file():
            continue
        processed += 1
        try:
            if append_info_line(path, info_line):
                modified += 1
                print(f"Updated: {path}")
            else:
                print(f"Unchanged: {path}")
        except Exception as e:
            print(f"Failed: {path} -> {e}", file=sys.stderr)

    print(f"Done. Processed: {processed}, Modified: {modified}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
