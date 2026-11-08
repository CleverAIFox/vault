---
type: source
created: 2026-11-09
area: [security, quality]
tags: [meta]
source: https://engineering.fb.com/2019/08/15/security/zoncolan/
publish: true
---
# Zoncolan

> 한 줄 요약: 메타가 Hack 코드베이스의 보안·개인정보 문제를 코드 변경마다 찾는 정적 분석 도구.

## 출처
- 저자·기관: Francesco Logozzo 외, Engineering at Meta 블로그
- 날짜: 2019-08-15
- 링크: https://engineering.fb.com/2019/08/15/security/zoncolan/

## 핵심 세 줄
1. 추상 해석으로 코드를 실행하지 않고 사용자 입력이 위험한 곳(sink)까지 흘러가는지 추적한다.
2. 하루 수천 건의 코드 변경을 운영 반영 전에 검사한다.
3. 보안 엔지니어가 버그 하나하나를 찾는 대신 버그 종류 전체를 막는 규칙을 만든다.

## 절별 요약
- 동작: 제어 흐름·호출 그래프를 만들고 함수를 요약해 소스에서 싱크까지 경로를 보고한다.
- 성과: 전체 코드베이스를 30분 안에 분석. 2018년 심각 이상 문제 1,100건 넘게 발견. 46%는 작성자에게 바로, 대부분 반영 전에 처리.
- 한계: 정적 분석에 맞는 문제 종류만 잡는다. 버그 바운티·보안 리뷰와 함께 쓴다.

## 내 생각
- Infer가 일반 버그라면 Zoncolan은 보안 버그다. 둘 다 "모든 변경에 자동 분석" 원칙.
- Maat에서는 GitHub 코드 스캐닝(CodeQL)이 같은 역할을 한다.

## 어디에 쓸까
- [[13 보안]]
- [[12 품질]]
