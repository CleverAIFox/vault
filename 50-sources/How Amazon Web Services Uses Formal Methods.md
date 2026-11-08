---
type: source
created: 2026-11-09
area: [math, methods, quality, design]
tags: [amazon]
source: https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/
publish: true
---
# How Amazon Web Services Uses Formal Methods

> 한 줄 요약: AWS가 TLA+ 명세와 모델 검사로 DynamoDB·S3 같은 핵심 시스템의 설계 버그를 코드 작성 전에 찾아낸 경험을 정리한 논문.

## 출처
- 저자·기관: Chris Newcombe 외 AWS 엔지니어들, Communications of the ACM
- 날짜: 2015(CACM 게재, 연도는 「확인 필요」)
- 링크: https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/

## 핵심 세 줄
1. 설계를 TLA+(집합론과 술어 기반 명세 언어)로 정확히 쓰고, TLC 모델 검사기로 가능한 실행 경로를 전부 확인한다.
2. 리뷰·코드 리뷰·테스트를 다 통과한 설계 버그를 찾아냈다. DynamoDB의 데이터 손실 버그는 최단 재현 경로가 35단계였다.
3. 경험 없는 엔지니어도 2~3주면 생산적으로 쓸 수 있었다.

## 절별 요약
- 도구: TLA+, C 비슷한 문법의 PlusCal, TLC 모델 검사기(분산 실행 포함). Alloy는 표현력이 부족해 제외했다.
- 적용: DynamoDB 복제·장애 허용, 데이터 이전 기능, S3 네트워크 알고리즘 등.
- 교훈: 무엇이 잘못될까보다 무엇이 반드시 성립해야 하는가(안전성·활성 속성)를 쓰는 편이 실수가 적다. 명세는 변경 영향 확인과 신입 교육 문서로도 쓰인다.
- 한계: 실제 코드가 검증한 설계와 같은지는 보장하지 못하고, 재시도 폭주 같은 성능 저하는 예측하지 못한다.

## 내 생각
- SWEBOK 17 수학 기초(논리·집합)가 실무에서 돈이 되는 가장 강한 증거다.
- Maat의 상태 전이(수집 → 판정 → 알림)를 PlusCal로 한 번 써 보는 것은 좋은 학습 과제다.

## 어디에 쓸까
- [[17 수학 기초]]
- [[11 모델과 방법]]
- [[12 품질]]
- [[03 설계]]
