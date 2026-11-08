# vault

SWEBOK v4를 뼈대로 한 개인 소프트웨어 공학 지식 베이스.

## 구조

| 폴더 | 노트 종류(type) | 내용 |
| --- | --- | --- |
| 10-areas | area | SWEBOK 영역 허브 18개 |
| 20-concepts | concept | 개념 |
| 30-decisions | decision | 결정(ADR) |
| 40-incidents | incident | 장애·회고(COE) |
| 50-sources | source | 자료 요약 |
| 60-journal | journal | 일지 |
| 70-projects | project | 프로젝트 허브 |
| 90-templates | — | 템플릿 |
| private | — | 공개 안 함(git 제외) |

## 규칙

1. 노트 하나에 개념 하나. 같은 내용은 복사하지 않고 링크한다.
2. 새 노트는 90-templates의 템플릿으로 만들고 머리 정보를 채운다.
3. 맨 위에 한 줄 요약. 줄글보다 짧은 목록.
4. 기계는 머리 정보만 읽는다. 본문은 자유.
5. 비밀값은 적지 않는다. 공개하면 안 되는 메모는 private/에.
6. 커밋은 `<종류>(<범위>): <요약>` (docs · chore · ci · build).
7. 영역 허브의 빅테크 표에 빈칸을 두지 않는다. 자료를 잇거나 「공개 자료 없음 (YYYY-MM-DD 조사)」로 적는다.
8. `index.json`은 직접 고치지 않는다. 커밋할 때 자동으로 다시 만들어진다.

## 검사와 카탈로그

- `scripts/vault.py`가 규칙을 검사하고, 모든 노트의 머리 정보와 한 줄 요약을 `index.json`(카탈로그)으로 모은다.
- 검사 항목: 머리 정보 필수 항목, type과 폴더 일치, area 값, 날짜 형식, 깨진 링크, 빅테크 표 빈칸, 자료와 허브의 링크 짝.
- 커밋 전: pre-commit 훅이 `build`를 돌린다. 클론한 뒤 한 번만 `git config core.hooksPath .githooks`를 실행한다.
- 푸시 후: GitHub Actions가 `check`를 돌린다. index.json이 최신이 아니어도 실패한다.

## area 값(SWEBOK v4)

requirements · architecture · design · construction · testing · operations · maintenance · configuration · management · process · methods · quality · security · practice · economics · computing · math · engineering
