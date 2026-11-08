---
type: source
created: 2026-11-09
area: [computing, architecture]
tags: [amazon]
source: https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html
publish: true
---
# Dynamo

> 한 줄 요약: 아마존 장바구니 같은 서비스를 위해 만든 고가용 키-값 저장소 논문. 일관성보다 가용성을 택한 설계의 고전이다.

## 출처
- 저자·기관: Giuseppe DeCandia 외(Werner Vogels 포함), SOSP 2007
- 날짜: 2007-10
- 링크: https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html

## 핵심 세 줄
1. 언제나 쓰기가 가능하도록(always writeable) 강한 일관성 대신 최종 일관성을 택했다.
2. 충돌은 읽을 때 애플리케이션이나 단순한 규칙으로 해결한다.
3. N·R·W 값을 조정해 성능·내구성·일관성의 균형을 맞춘다.

## 절별 요약
- 분할: 일관된 해싱(consistent hashing)으로 노드에 데이터를 나눠 점진적으로 확장한다.
- 버전 관리: 벡터 시계로 객체 버전 간 인과 관계를 추적한다.
- 일시 장애: sloppy quorum과 hinted handoff로 쓰기 가용성을 지킨다.
- 영구 장애: 머클 트리로 복제본 차이를 백그라운드에서 맞춘다.
- 멤버십: 가십 프로토콜로 중앙 등록소 없이 장애를 감지한다.

## 내 생각
- DynamoDB는 이름만 이어받았고 내부 설계는 다르다는 점을 헷갈리지 않는다(「확인 필요」).
- AWS DEA 자격증의 NoSQL·파티션 키 개념을 이해하는 뿌리다.

## 어디에 쓸까
- [[16 컴퓨팅 기초]]
- [[02 아키텍처]]
