#!/usr/bin/env python3
"""볼트 검사와 카탈로그(index.json) 생성.

사용법:
  python3 scripts/vault.py check   규칙 검사 + index.json이 최신인지 확인 (CI)
  python3 scripts/vault.py build   index.json 다시 생성 (pre-commit 훅)

표준 라이브러리만 쓴다. 규칙의 원본은 README.md다(area 값 목록도 README에서 읽는다).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"
SKIP_DIRS = {".git", ".github", ".obsidian", ".trash", "90-templates", "private", "scripts", ".githooks"}
TYPE_DIR = {"area": "10-areas", "concept": "20-concepts", "decision": "30-decisions", "incident": "40-incidents",
            "source": "50-sources", "journal": "60-journal", "project": "70-projects"}
REQUIRED = ["type", "created", "area", "tags", "source", "publish"]
NONE_MARK = "공개 자료 없음"


def area_values():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"## area 값[^\n]*\n+([^\n]+)", text)
    if not m:
        sys.exit("README.md에서 'area 값' 목록을 찾지 못했다")
    return [v.strip() for v in m.group(1).split("·")]


def notes():
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS or len(rel.parts) == 1:
            continue
        yield p, rel


def parse(text):
    """단순한 YAML 머리 정보만 다룬다: key: value, key: [a, b]."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    meta = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        elif v in ("true", "false"):
            v = v == "true"
        elif len(v) >= 2 and v[0] == v[-1] == '"':
            v = v[1:-1]
        meta[k.strip()] = v
    return meta, text[end + 5:]


def links(body):
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    return [re.split(r"[|#]", l)[0].strip() for l in re.findall(r"\[\[([^\]]+)\]\]", body)]


def summary(body):
    m = re.search(r"^> [^:\n]*:\s*(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def load():
    out = []
    for p, rel in notes():
        meta, body = parse(p.read_text(encoding="utf-8"))
        out.append((p, rel, meta, body))
    return out


def build_index(items):
    rows = []
    for p, rel, meta, body in items:
        if meta is None:
            continue
        title = re.search(r"^# (.+)$", body, re.M)
        rows.append({
            "path": rel.as_posix(), "title": title.group(1).strip() if title else p.stem,
            "type": meta.get("type"), "area": meta.get("area", []), "tags": meta.get("tags", []),
            "source": meta.get("source", ""), "created": meta.get("created", ""),
            "publish": meta.get("publish", False), "summary": summary(body),
            "links": sorted(set(links(body)) | ({meta["source"][2:-2]} if str(meta.get("source", "")).startswith("[[") else set())),
        })
    return json.dumps({"generated_by": "scripts/vault.py", "notes": rows}, ensure_ascii=False, indent=1) + "\n"


def check(items):
    errs = []
    areas = set(area_values())
    names = {p.stem for p, *_ in items}
    hubs = {}
    for p, rel, meta, body in items:
        where = rel.as_posix()
        if meta is None:
            errs.append(f"{where}: 머리 정보(---)가 없다"); continue
        for k in REQUIRED:
            if k not in meta:
                errs.append(f"{where}: 머리 정보에 '{k}'가 없다")
        t = meta.get("type")
        if t not in TYPE_DIR:
            errs.append(f"{where}: type '{t}'는 허용 값이 아니다")
        elif rel.parts[0] != TYPE_DIR[t]:
            errs.append(f"{where}: type '{t}'는 {TYPE_DIR[t]}/에 있어야 한다")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("created", ""))):
            errs.append(f"{where}: created는 YYYY-MM-DD여야 한다")
        if not isinstance(meta.get("publish"), bool):
            errs.append(f"{where}: publish는 true 또는 false여야 한다")
        a = meta.get("area", [])
        if not isinstance(a, list):
            errs.append(f"{where}: area는 [목록]이어야 한다"); a = []
        for v in a:
            if v not in areas:
                errs.append(f"{where}: area '{v}'는 README.md의 18개 값이 아니다")
        for l in links(body):
            if l not in names:
                errs.append(f"{where}: 깨진 링크 [[{l}]]")
        if t == "area":
            if len(a) != 1:
                errs.append(f"{where}: 영역 허브는 area 값이 하나여야 한다")
            else:
                hubs[a[0]] = (where, body)
            for row in re.findall(r"^\|[^\n]*\|$", body, re.M):
                cells = [c.strip() for c in row.strip("|").split("|")]
                if len(cells) == 3 and cells[0] not in ("회사", "---") and (not cells[1] or not cells[2]):
                    errs.append(f"{where}: 빅테크 표 빈칸({cells[0]}). 자료를 잇거나 「{NONE_MARK} (YYYY-MM-DD 조사)」로 적는다")
    missing = areas - hubs.keys()
    for v in sorted(missing):
        errs.append(f"10-areas: area '{v}'의 허브가 없다")
    for p, rel, meta, body in items:
        if meta and meta.get("type") == "source" and p.stem != "SWEBOK v4":
            for v in meta.get("area", []):
                if v in hubs and f"[[{p.stem}]]" not in hubs[v][1]:
                    errs.append(f"{rel.as_posix()}: area '{v}'인데 {hubs[v][0]} 표에 링크가 없다")
    return errs


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    items = load()
    new = build_index(items)
    if cmd == "build":
        INDEX.write_text(new, encoding="utf-8")
        print(f"index.json: 노트 {new.count(chr(10) + '  {')}개")
        errs = check(items)
    elif cmd == "check":
        errs = check(items)
        if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != new:
            errs.append("index.json이 최신이 아니다. python3 scripts/vault.py build 후 커밋한다")
    else:
        sys.exit(__doc__)
    for e in errs:
        print("✗", e)
    if errs:
        sys.exit(f"검사 실패: {len(errs)}건")
    print(f"검사 통과: 노트 {len(items)}개")


if __name__ == "__main__":
    main()
