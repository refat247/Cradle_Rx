#!/usr/bin/env python3
"""Byte-integrity and release-boundary checks only; NOT a clinical QA certificate."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / "ARTIFACTS.json").read_text(encoding="utf-8"))
for item in manifest["artifacts"]:
    path = ROOT / item["path"]
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    assert actual == item["sha256"], (
        f"SHA-256 mismatch: {item['path']}: {actual} != {item['sha256']}"
    )
    if item["kind"] == "compiled_offline_reader":
        assert b'data-artifact-version="1.3.0"' in data, "Reader version not v1.3.0"
    if item["kind"] == "uiux_review_atlas":
        for feature in ("UI01", "UI50", "UX01", "UX50"):
            assert feature.encode() in data, f"Missing Atlas feature {feature}"
    print(f"PASS {item['kind']}: {item['path']} ({len(data)} bytes)")
print("PASS: exact checked-in artifact hashes. Clinical validity NOT assessed.")
