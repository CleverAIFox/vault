# AGENTS.md

이 저장소는 사람의 지식 베이스다. 구조와 규칙은 README.md를 따른다.

- 먼저 `index.json`(카탈로그)을 읽고 필요한 노트만 연다. 주제로 들어갈 때는 10-areas의 영역 허브에서 시작한다.
- 새 노트는 90-templates의 해당 템플릿 형식을 그대로 따르고 머리 정보(type, created, area, tags, source, publish)를 채운다.
- area 값은 README.md의 18개 중에서만 쓴다.
- 만들기 전에 같은 주제의 노트가 있는지 검색한다. 있으면 그 노트를 고치거나 링크한다.
- 출처가 없는 사실은 「확인 필요」로 표시한다. 지어내지 않는다.
- 노트를 지우거나 옮기기 전에 사람에게 묻는다.
- 본문을 일괄 치환(sed 등)하지 않는다. 비밀값을 적지 않는다.
- 커밋 메시지는 README.md의 형식을 따른다.
- 커밋 전에 `python3 scripts/vault.py check`가 통과해야 한다. `index.json`은 직접 고치지 않고 `build`로 만든다.
