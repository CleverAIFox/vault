---
type: source
created: 2026-11-09
area: [process, design, testing, configuration, operations]
tags: [microsoft]
source: https://microsoft.github.io/code-with-engineering-playbook/
publish: true
---
# Engineering Fundamentals Playbook

> 한 줄 요약: 마이크로소프트 ISE 팀이 고객사와 함께 개발하며 쌓은 공학 기본기 모음. 애자일·테스트·CI/CD·코드 리뷰·관측성 등을 체크리스트로 정리했다.

## 출처
- 저자·기관: Microsoft ISE(Industry Solutions Engineering) 팀, GitHub 공개 저장소
- 날짜: 상시 개정(PR로 기여 가능)
- 링크: https://microsoft.github.io/code-with-engineering-playbook/

## 핵심 세 줄
1. "일을 끝내는 것"보다 품질과 정확성을 앞에 둔다.
2. 가장 단순하게 동작하는 버전부터 만들고 조금씩 가치를 낸다.
3. 코드는 모두가 함께 책임진다.

## 절별 요약
- 공학 기본기 체크리스트와 "프로젝트 첫 주" 안내.
- 애자일 개발: 백로그, 브랜치, 의식(ceremony), 역할, 팀 합의.
- 자동 테스트: 단위, 통합, E2E, 성능, 스모크, 장애 주입, UI.
- CI/CD: 지속 통합·전달, DevSecOps, GitOps.
- 코드 리뷰, 설계(패턴·설계 리뷰·결정 기록·다이어그램), 개발자 경험(dev container·온보딩), 문서화.
- 비기능 요구사항, 관측성(로그·지표·추적·알림), 보안(위협 모델링), 소스 관리(브랜치·병합·버전·시크릿).

## 내 생각
- 회사 전체 표준이 아니라 한 조직(ISE)의 실무 지침이다. 그 대신 바로 쓸 수 있는 체크리스트라 Maat의 "해야 할 일 목록"으로 가장 실용적이다.
- "결정 기록(decision log)"이 볼트의 decision 템플릿(ADR)과 같은 개념이다.

## 어디에 쓸까
- [[10 공학 프로세스]]
- [[03 설계]]
- [[05 테스트]]
- [[08 형상 관리]]
- [[06 운영]]
