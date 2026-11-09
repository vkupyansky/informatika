"""Проверка локальных ссылок и ресурсов без внешних запросов."""

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def check_reference(source: Path, reference: str) -> None:
    url = urlsplit(reference)
    if url.scheme or url.netloc or not url.path:
        return
    target = (source.parent / unquote(url.path)).resolve()
    if not target.is_relative_to(ROOT) or not target.is_file():
        raise ValueError(f"{source.relative_to(ROOT)}: отсутствует {reference}")


class Links(HTMLParser):
    def __init__(self, source: Path) -> None:
        super().__init__()
        self.source = source

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value is not None:
                check_reference(self.source, value)


def main() -> None:
    pages = sorted(ROOT.rglob("*.html"))
    for source in pages:
        parser = Links(source)
        parser.feed(source.read_text(encoding="utf-8"))
        parser.close()
    for source in sorted(ROOT.rglob("*.css")):
        for match in re.finditer(r"url\(\s*['\"]?([^)'\"]+)", source.read_text()):
            check_reference(source, match.group(1).strip())
    print(f"Проверены локальные ссылки и ресурсы {len(pages)} HTML-страниц.")


if __name__ == "__main__":
    main()
