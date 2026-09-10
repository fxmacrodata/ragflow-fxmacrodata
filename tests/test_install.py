"""Installer preflight must preserve a user's existing source edits."""
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("fxmd_overlay_installer", Path(__file__).parents[1] / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


@pytest.fixture
def source_and_target(tmp_path):
    source, target = tmp_path / "package", tmp_path / "checkout"
    (source / "overlay/web").mkdir(parents=True)
    (target / "web").mkdir(parents=True)
    (target / "web/existing.ts").write_text("original\n")
    (source / "overlay/web/existing.ts").write_text("updated\n")
    (source / "overlay/web/new.ts").write_text("new\n")
    (source / "UPSTREAM_FILES.json").write_text(json.dumps({"original_sha256": {"web/existing.ts": hashlib.sha256(b"original\n").hexdigest()}}))
    (source / "PUBLIC_FILES.json").write_text(json.dumps({"files": ["overlay/web/existing.ts", "overlay/web/new.ts"]}))
    return source, target


def test_preflight_only_plans_explicit_files_without_writing(source_and_target):
    source, target = source_and_target
    (source / "overlay/web/unlisted.ts").write_text("not included")
    assert len(installer.planned_files(source, target)) == 2
    assert (target / "web/existing.ts").read_text() == "original\n"
    assert not (target / "web/new.ts").exists()


def test_existing_edits_block_the_whole_install(source_and_target):
    source, target = source_and_target
    (target / "web/existing.ts").write_text("user edit\n")
    with pytest.raises(ValueError, match="differs"):
        installer.planned_files(source, target)
    assert not (target / "web/new.ts").exists()


def test_existing_new_file_is_not_overwritten(source_and_target):
    source, target = source_and_target
    (target / "web/new.ts").write_text("user file\n")
    with pytest.raises(ValueError, match="overwrite"):
        installer.planned_files(source, target)


def test_allowlist_cannot_escape_the_source_overlay(source_and_target):
    source, target = source_and_target
    (source / "outside.py").write_text("not an integration file")
    (source / "PUBLIC_FILES.json").write_text(json.dumps({"files": ["overlay/../outside.py"]}))
    with pytest.raises(ValueError, match="Invalid allowlisted"):
        installer.planned_files(source, target)
