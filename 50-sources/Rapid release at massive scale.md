---
type: source
created: 2026-11-09
area: [operations, configuration, process]
tags: [meta]
source: https://engineering.fb.com/2017/08/31/web/rapid-release-at-massive-scale/
publish: true
---
# Rapid release at massive scale

> 한 줄 요약: 페이스북이 하루 세 번 배포하던 방식에서 master에서 바로 내보내는 준지속 배포로 바꾼 과정. 단계적 배포와 기능 플래그가 핵심이다.

## 출처
- 저자·기관: Chuck Rossi, Engineering at Meta 블로그
- 날짜: 2017-08-31
- 링크: https://engineering.fb.com/2017/08/31/web/rapid-release-at-massive-scale/

## 핵심 세 줄
1. 2016년 4월부터 1년에 걸쳐 facebook.com을 master에서 바로 배포하는 방식으로 바꿨다.
2. 직원 → 운영 일부 → 전체 순서로 단계를 밟고, 단계마다 신호를 보고 멈출 수 있다.
3. 배포와 기능 공개를 기능 플래그(Gatekeeper)로 분리했다.

## 절별 요약
- 바꾼 이유: 하루 1,000개가 넘는 변경을 브랜치에서 골라 담는 방식이 한계에 왔다.
- 단계: 자동 테스트 통과 → 직원에게 먼저 → 운영 서버 약 2% → 몇 시간에 걸쳐 100%.
- 도구: Gatekeeper(기능 플래그로 끄면 되돌리기 대신 해결), Flytrap(사용자 신고를 모아 이상 감지).
- 모바일: 배포 주기가 4주에서 1주로 줄었고, 엔지니어 수가 크게 늘어도 생산성과 심각한 릴리스 문제 수는 거의 그대로였다.

## 내 생각
- 트렁크 기반 개발을 왜 하는지에 대한 가장 강한 실제 사례다. 볼트 main 직접 푸시, Maat 트렁크 규칙의 근거로 링크한다.
- "배포와 공개를 분리한다"는 원칙은 1인 프로젝트에도 그대로 쓸 수 있다.

## 어디에 쓸까
- [[06 운영]]
- [[08 형상 관리]]
- [[10 공학 프로세스]]
