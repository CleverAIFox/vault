---
type: source
created: 2026-11-09
area: [quality, construction]
tags: [meta]
source: https://fbinfer.com/docs/about-Infer
publish: true
---
# Infer

> 한 줄 요약: 메타가 만든 정적 분석 도구. 코드 변경마다 CI에서 돌며 널 포인터 역참조나 데이터 경쟁 같은 깊은 버그를 찾는다.

## 출처
- 저자·기관: Meta, fbinfer.com(오픈소스)
- 날짜: 문서 기준 v1.3.0
- 링크: https://fbinfer.com/docs/about-Infer

## 핵심 세 줄
1. Java, C, C++, Objective-C, Erlang 코드를 분석한다.
2. 여러 파일에 걸친 함수 호출까지 따라가며 버그를 찾는다.
3. 메타 CI에서 페이스북·메신저·인스타그램·왓츠앱의 모든 코드 변경을 검사한다.

## 절별 요약
- 찾는 버그: 널 포인터 역참조, 데이터 경쟁 등.
- 쓰는 곳: 메타 CI, 그리고 다른 여러 회사.
- 이론 배경은 분리 논리(separation logic)와 bi-abduction이며, 공식 문서에 별도 페이지가 있다.

## 내 생각
- Python은 지원하지 않는다. Maat(Python)에서는 같은 역할을 pyright·ruff가 맡는다. 원칙(모든 변경에 자동 정적 분석)만 가져온다.
- SWEBOK 17 수학 기초(논리)가 실제 도구로 이어지는 예시로 좋다.

## 어디에 쓸까
- [[12 품질]]
- [[04 구축]]
