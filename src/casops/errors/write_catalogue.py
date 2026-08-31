"""Write errors/catalogue.json from spec rows. Source of truth after write."""

from __future__ import annotations

import json

from casops.contracts.canonical import canonical_dumps
from casops.errors.catalogue import CATALOGUE_PATH, catalogue_document


def main() -> None:
    CATALOGUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    document = catalogue_document()
    CATALOGUE_PATH.write_text(canonical_dumps(document) + "\n", encoding="utf-8")
    print(f"wrote {CATALOGUE_PATH} ({len(document['codes'])} codes)")


if __name__ == "__main__":
    main()
