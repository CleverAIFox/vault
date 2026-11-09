# vault

빅테크 문서를 SWEBOK v4 체계로 정리하는 개인 소프트웨어 공학 지식 베이스. 지금은 골격만 있고, 작성 파이프라인을 다시 설계하는 중이다.

## 구조

| 폴더 | 노트 종류(type) | 내용 |
| --- | --- | --- |
| 10-areas | area | SWEBOK 영역 허브 |
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
4. 비밀값은 적지 않는다. 공개하면 안 되는 메모는 private/에.
5. 커밋은 `<종류>(<범위>): <요약>` (docs · chore · ci · build).

## area 값(SWEBOK v4)

requirements · architecture · design · construction · testing · operations · maintenance · configuration · management · process · methods · quality · security · practice · economics · computing · math · engineering
