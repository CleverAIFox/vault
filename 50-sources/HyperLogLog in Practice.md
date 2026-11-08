---
type: source
created: 2026-11-09
area: [math, computing]
tags: [google]
source: https://research.google/pubs/hyperloglog-in-practice-algorithmic-engineering-of-a-state-of-the-art-cardinality-estimation-algorithm/
publish: true
---
# HyperLogLog in Practice

> 한 줄 요약: 고유한 원소 수를 아주 적은 메모리로 추정하는 HyperLogLog 알고리즘을 구글이 실제 시스템에 맞게 개선한 논문.

## 출처
- 저자·기관: Stefan Heule, Marc Nunkesser, Alex Hall, EDBT 2013
- 날짜: 2013
- 링크: https://research.google/pubs/hyperloglog-in-practice-algorithmic-engineering-of-a-state-of-the-art-cardinality-estimation-algorithm/

## 핵심 세 줄
1. 문제는 카디널리티 추정, 즉 데이터에 서로 다른 값이 몇 개인지 어림하는 것이다.
2. 메모리를 줄이면서 중요한 구간에서 정확도를 크게 높였다.
3. 한 번 훑어서 계산하고 병렬화도 잘 된다.

## 절별 요약
- 배경: 정확히 세려면 메모리가 많이 들어서 확률적 추정을 쓴다.
- 개선: 원래 HyperLogLog의 메모리 요구량을 줄이고 정확도를 높이는 일련의 변경.
- 검증: 구글 시스템에 구현해 원래 알고리즘과 실험으로 비교했다.

## 내 생각
- SWEBOK 17 수학 기초의 이산 확률이 실무 알고리즘이 되는 예다. Redis, BigQuery의 근사 집계 함수도 같은 계열이다(「확인 필요」).
- 빅데이터분석기사 공부할 때 근사 알고리즘 예시로 쓴다.

## 어디에 쓸까
- [[17 수학 기초]]
- [[16 컴퓨팅 기초]]
