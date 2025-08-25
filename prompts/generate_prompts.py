from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, List

try:
    import jinja2
except Exception as exc:  # pragma: no cover
    sys.stderr.write(
        "Jinja2 is required to run this script. Install with: pip install jinja2\n"
    )
    raise

ROOT = Path(__file__).resolve().parent
TEMPLATE_PATH = ROOT / "methods" / "prompt_template_common_header.md.j2"
OUTPUT_DIR = ROOT / "methods" / "generated"


def iter_method_codes() -> Iterable[str]:
    # 00-99
    for i in range(100):
        yield f"{i:02d}"
    # A0-E9
    for letter in ["A", "B", "C", "D", "E"]:
        for digit in range(10):
            yield f"{letter}{digit}"


def render_template_for_code(template: jinja2.Template, code: str) -> str:
    # Preserve the placeholder for BUNDESBANK_SPEC in the output by supplying it literally
    return template.render(
        code=code,
        BUNDESBANK_SPEC="{{BUNDESBANK_SPEC}}",
    )


def main(argv: List[str] | None = None) -> int:
    argv = argv or sys.argv[1:]

    if not TEMPLATE_PATH.exists():
        sys.stderr.write(f"Template not found: {TEMPLATE_PATH}\n")
        return 2

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    env = jinja2.Environment(autoescape=False)
    template = env.from_string(TEMPLATE_PATH.read_text(encoding="utf-8"))

    count = 0
    for code in iter_method_codes():
        rendered = render_template_for_code(template, code)
        out_path = OUTPUT_DIR / f"method_{code}.md"
        out_path.write_text(rendered, encoding="utf-8")
        count += 1

    print(f"Generated {count} prompt files in {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
