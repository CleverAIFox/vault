---
type: source
created: 2026-11-09
area: [computing, architecture]
tags: [meta]
source: https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson
publish: true
---
# TAO

> 한 줄 요약: 페이스북 소셜 그래프를 서비스하는 지리 분산 데이터 저장소 논문. 단순한 데이터 모델과 API로 초당 10억 건 읽기를 처리한다.

## 출처
- 저자·기관: Nathan Bronson 외 페이스북 엔지니어들, USENIX ATC 2013
- 날짜: 2013-06
- 링크: https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson

## 핵심 세 줄
1. 소셜 그래프 서비스에 맞춘 단순한 데이터 모델과 API를 제공한다.
2. 여러 데이터 유형에서 기존 memcache를 대체했다.
3. 수천 대 장비에서 페타바이트 데이터, 초당 10억 건 읽기와 수백만 건 쓰기를 처리한다.

## 절별 요약
- 데이터 모델: 객체(노드)와 연관(엣지)로 그래프를 표현한다(세부는 논문 본문, 「확인 필요」).
- 배치: 지리적으로 분산되어 있다.
- 부하: 고정된 질의 집합으로 페이스북의 까다로운 부하를 감당한다.

## 내 생각
- Dynamo(아마존)와 비교하면 좋다. 둘 다 읽기·가용성을 위해 일관성을 양보한 설계다.
- PostgreSQL + 캐시로 가는 Maat 스택과 규모만 다를 뿐 같은 문제다.

## 어디에 쓸까
- [[16 컴퓨팅 기초]]
- [[02 아키텍처]]
