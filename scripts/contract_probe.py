#!/usr/bin/env python3
import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://api.verifrax.net"
REQUIRED_PUBLIC_PATHS = {
    "/healthz",
    "/readyz",
    "/version",
    "/openapi.json",
}

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence" / "current"
BADGES_DIR = ROOT / "badges"


def request(path: str, accept: str) -> tuple[bytes, str]:
    req = urllib.request.Request(
        f"{BASE}{path}",
        headers={
            "User-Agent": "VERIFRAX-API-contract-probe/1.0",
            "Accept": accept,
        },
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        body = response.read()
        content_type = response.headers.get("content-type", "")
        return body, content_type


def fetch_json(path: str):
    body, content_type = request(path, "application/json, text/plain;q=0.9, */*;q=0.8")
    return json.loads(body.decode("utf-8")), content_type


def fetch_text(path: str) -> tuple[str, str]:
    body, content_type = request(path, "text/plain, application/json;q=0.9, */*;q=0.8")
    return body.decode("utf-8"), content_type


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def badge(label: str, message: str, color: str):
    return {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color,
    }


def main() -> None:
    checked_at = (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

    healthz, healthz_ct = fetch_json("/healthz")
    readyz, readyz_ct = fetch_json("/readyz")
    version_text, version_ct = fetch_text("/version")
    openapi, openapi_ct = fetch_json("/openapi.json")

    for name, payload in (("healthz", healthz), ("readyz", readyz)):
        if not isinstance(payload, dict):
            raise SystemExit(f"/{name} did not return a JSON object")
        for key in ("status", "surface", "role", "live"):
            if key not in payload:
                raise SystemExit(f"/{name} missing key: {key}")
        if payload["live"] is not True:
            raise SystemExit(f"/{name} is not live")

    version_value = version_text.strip()
    if not version_value:
        raise SystemExit("/version returned empty body")
    if len(version_value) > 120:
        raise SystemExit("/version returned unexpectedly long body")
    if not re.search(r"[A-Za-z0-9]", version_value):
        raise SystemExit("/version returned non-informative body")

    if openapi.get("openapi") != "3.1.0":
        raise SystemExit("openapi version mismatch")
    if openapi.get("info", {}).get("title") != "VERIFRAX API":
        raise SystemExit("openapi title mismatch")

    servers = openapi.get("servers") or []
    if not servers or servers[0].get("url") != BASE:
        raise SystemExit("openapi servers[0].url mismatch")

    paths = set((openapi.get("paths") or {}).keys())
    missing = sorted(REQUIRED_PUBLIC_PATHS - paths)
    if missing:
        raise SystemExit(f"openapi missing required public paths: {missing}")

    evidence = {
        "host": "api.verifrax.net",
        "surface_class": "execution_api",
        "checked_at": checked_at,
        "binding_status": "live",
        "checked_endpoints": {
            "/healthz": {
                "status": "pass",
                "content_type": healthz_ct,
                "body": healthz,
            },
            "/readyz": {
                "status": "pass",
                "content_type": readyz_ct,
                "body": readyz,
            },
            "/version": {
                "status": "pass",
                "content_type": version_ct,
                "body": version_value,
            },
            "/openapi.json": {
                "status": "pass",
                "content_type": openapi_ct,
                "openapi": openapi["openapi"],
                "title": openapi["info"]["title"],
                "server_url": servers[0]["url"],
                "required_public_paths_present": sorted(REQUIRED_PUBLIC_PATHS),
            },
        },
        "overall_status": "pass",
    }

    evidence_bytes = (
        json.dumps(evidence, sort_keys=True, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    evidence["evidence_sha256"] = sha256_bytes(evidence_bytes)

    write_json(EVIDENCE_DIR / "contract-status.json", evidence)
    write_json(BADGES_DIR / "healthz.json", badge("/healthz", str(healthz["status"]), "brightgreen"))
    write_json(BADGES_DIR / "readyz.json", badge("/readyz", str(readyz["status"]), "brightgreen"))
    write_json(BADGES_DIR / "version.json", badge("/version", version_value, "blue"))
    write_json(BADGES_DIR / "openapi.json", badge("/openapi.json", f"OpenAPI {openapi['openapi']}", "blueviolet"))
    write_json(BADGES_DIR / "contract.json", badge("contract", "live", "brightgreen"))

    print("[OK] live contract probe passed")
    print("[OK] wrote", EVIDENCE_DIR / "contract-status.json")
    print("[OK] wrote", BADGES_DIR)


if __name__ == "__main__":
    main()
