---
type: area
created: {{date:YYYY-MM-DD}}
area: []
tags: [swebok]
source:
publish: false
---
# {{title}}

> 한 줄 정의(SWEBOK v4 기준):

## 이 영역이 다루는 주제

## 빅테크별 관점
| 회사 | 관점 | 자료 |
| --- | --- | --- |
| 아마존 |  | [[ ]] |
| 구글 |  | [[ ]] |
| 마이크로소프트 |  | [[ ]] |
| 메타 |  | [[ ]] |
| 애플 |  | [[ ]] |
| 엔비디아 |  | [[ ]] |
| 테슬라 |  | [[ ]] |
| 넷플릭스(보충) |  | [[ ]] |

## 이 영역의 노트
```base
filters:
  and:
    - area.contains("영역값")
    - type != "area"
views:
  - type: table
    name: 이 영역의 노트
    order:
      - file.name
      - type
      - created
```
