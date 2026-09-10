"""Install the reviewed overlay into a matching RAGFlow source checkout."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def planned_files(source: Path, target: Path):
    upstream = json.loads((source / "UPSTREAM_FILES.json").read_text(encoding="utf8"))
    originals = upstream["original_sha256"]
    planned = []
    declared = json.loads((source / "PUBLIC_FILES.json").read_text(encoding="utf8"))["files"]
    for name in sorted(name for name in declared if name.startswith("overlay/")):
        item = source / name
        relative = name.removeprefix("overlay/")
        if not item.is_file() or item.is_symlink() or not item.resolve().is_relative_to((source / "overlay").resolve()):
            raise ValueError("Invalid allowlisted integration file.")
        destination = target / relative
        if destination.is_symlink() or not destination.resolve().is_relative_to(target.resolve()):
            raise ValueError("Refusing a destination outside the RAGFlow source checkout.")
        if relative in originals:
            if not destination.is_file():
                raise ValueError("Missing expected upstream file: " + relative)
            # Allow ordinary Git CRLF checkout conversion, without discarding edits.
            digest = hashlib.sha256(destination.read_text(encoding="utf8").encode("utf8")).hexdigest()
            if digest != originals[relative]:
                raise ValueError("Upstream file differs from the reviewed source: " + relative)
        elif destination.exists():
            raise ValueError("Refusing to overwrite an existing integration file: " + relative)
        planned.append((item, destination))
    return planned


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--apply", action="store_true", help="Apply after checking every target file; default is a dry run")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    target = args.checkout.resolve(strict=True)
    plan = planned_files(source, target)
    for item, destination in plan:
        if args.apply:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(item.read_bytes())
    print(("Installed" if args.apply else "Validated") + f" {len(plan)} integration files.")


if __name__ == "__main__":
    main()
