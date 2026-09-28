#!/usr/bin/env python3

import json
from html.parser import HTMLParser
from pathlib import Path


START_MARKER = "<!-- singlebook-data:start -->"
END_MARKER = "<!-- singlebook-data:end -->"
DATA_SCRIPT = '<script id="singlebook-data" type="application/singlebook+json">'

ROOT = Path(__file__).resolve().parent.parent
MAIN_BOOK = ROOT / "SingleBook.singlebook.html"
EXAMPLES_DIR = ROOT / "examples"
DATA_DIR = EXAMPLES_DIR / "data"


class SingleBookParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.generator = None
        self.in_data_script = False
        self.data_parts = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "meta" and attributes.get("name") == "generator":
            self.generator = attributes.get("content")
        elif tag == "script" and attributes.get("id") == "singlebook-data":
            self.in_data_script = True

    def handle_endtag(self, tag):
        if tag == "script" and self.in_data_script:
            self.in_data_script = False

    def handle_data(self, data):
        if self.in_data_script:
            self.data_parts.append(data)

    @property
    def document_data(self):
        return "".join(self.data_parts).strip()


def inspect_book(source):
    parser = SingleBookParser()
    parser.feed(source)
    return parser.generator, json.loads(parser.document_data)


def replace_document_data(source, document):
    if source.count(START_MARKER) != 1 or source.count(END_MARKER) != 1:
        raise ValueError(f"{MAIN_BOOK.name} must contain exactly one pair of data markers")

    start = source.index(START_MARKER)
    end = source.index(END_MARKER, start) + len(END_MARKER)
    serialized = json.dumps(document, ensure_ascii=False, indent=2).replace("<", "\\u003c")
    block = (
        f"{START_MARKER}\n"
        f"    {DATA_SCRIPT}\n"
        + "\n".join(f"        {line}" for line in serialized.splitlines())
        + "\n    </script>\n"
        f"    {END_MARKER}"
    )
    return source[:start] + block + source[end:]


def main():
    source = MAIN_BOOK.read_text(encoding="utf-8")
    main_generator, _ = inspect_book(source)
    if not main_generator:
        raise ValueError(f"{MAIN_BOOK.name} has no generator version")

    data_paths = sorted(DATA_DIR.glob("*.json"))
    if not data_paths:
        print(f"No example data found in {DATA_DIR.relative_to(ROOT)}")
        return

    for data_path in data_paths:
        document = json.loads(data_path.read_text(encoding="utf-8"))
        output_path = EXAMPLES_DIR / f"{data_path.stem}.singlebook.html"
        reason = None

        if not output_path.exists():
            reason = "created"
        else:
            try:
                existing_generator, existing_document = inspect_book(
                    output_path.read_text(encoding="utf-8")
                )
            except (OSError, ValueError, json.JSONDecodeError):
                reason = "regenerated invalid book"
            else:
                if existing_generator != main_generator:
                    reason = "updated generator"
                elif existing_document != document:
                    reason = "updated data"

        if reason:
            output_path.write_text(
                replace_document_data(source, document),
                encoding="utf-8",
            )
            print(f"{reason}: {output_path.relative_to(ROOT)}")
        else:
            print(f"current: {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
