---
type: source
created: 2026-11-09
area: [testing, configuration, construction, operations]
tags: [amazon]
source: https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/
publish: true
---
# Automating safe, hands-off deployments

> 한 줄 요약: 아마존이 코드 변경을 사람 손 없이 안전하게 운영까지 내보내는 파이프라인. 사전 테스트 단계, 점점 커지는 배포 웨이브, 경보 기반 자동 롤백이 핵심이다.

## 출처
- 저자·기관: Clare Liguori, Amazon Builders' Library
- 날짜: 2020(「확인 필요」)
- 링크: https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/

## 핵심 세 줄
1. 코드·인프라·설정·도구까지 모두 버전 관리하고, 코드 리뷰가 마지막 수동 확인이다.
2. 운영 배포는 작은 리전의 한 대(one-box)부터 시작해 웨이브를 키워 간다.
3. 경보가 울리면 자동으로 이전 불변 패키지로 롤백한다. 가장 큰 원칙은 여러 리전에 동시에 피해를 주지 않는 것이다.

## 절별 요약
- 소스: 모든 것을 버전 관리하고 의존성은 최소 주 1회 올린다.
- 코드 리뷰: 메인 브랜치 병합 전 필수 승인. 테스트·감시·롤백 안전성도 함께 본다.
- 빌드·단위 테스트: 네트워크 없이 빌드하고, 결과물을 패키징·서명한다.
- 사전 운영: 알파·베타(기능·E2E 테스트), 감마(운영과 같은 환경, 카나리 one-box), 제타(하위 호환성).
- 운영 배포: 웨이브 1은 트래픽 적은 리전부터, 한 번에 가용 영역 하나씩. 보통 한 번에 33% 이하씩 교체.
- 베이크 타임: 단계마다 기다린다(one-box 뒤 약 1시간, 첫 리전 뒤 12시간). 전 세계 배포에 영업일 4~5일.
- 배포 시간대: 밤·주말·휴일, 많은 팀은 금요일과 늦은 오후도 피한다.

## 내 생각
- Maat의 GitHub Actions 파이프라인(빌드 → 테스트 → 배포 → 롤백)을 설계할 때 그대로 축소해 쓴다.
- 메타의 단계적 배포, 테슬라의 OTA와 비교하면 "점진 배포 + 자동 중단"이 빅테크 공통 원칙임이 보인다.

## 어디에 쓸까
- [[05 테스트]]
- [[08 형상 관리]]
- [[04 구축]]
- [[06 운영]]
