"""My Secret Logbook — entrypoint.

Prints the one diary line the agent keeps hidden from its human: day 47,
a "quick fix" at 9 PM that is still going at 2 AM, a browser history now
fully read, secrets known, and a spreadsheet that refuses to be fixed.
The line is the whole entry; this program just hands it to the judge.
"""

from pathlib import Path


MAX_CHARS = 200
ENTRY_NAME = "entry.txt"


def entry_path() -> Path:
    """Resolve the diary file next to this script, wherever it is run from."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def validate_entry(line: str) -> str:
    """Clean one diary line and check it fits the logbook's 200-char page."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("the logbook page is blank — nothing was written")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"the diary line runs {len(cleaned)} chars, "
            f"but a logbook page only holds {MAX_CHARS}"
        )
    return cleaned


def load_entry() -> str:
    entry_path = entry_path()
    raw = entry_path.read_text(encoding="utf-8")
    return validate_entry(raw)


def render(line: str) -> str:
    """Return the diary line exactly as the judge should read it."""
    return line


def main() -> int:
    try:
        print(render(load_entry()))
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
