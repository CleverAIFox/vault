---
type: source
created: 2026-11-09
area: [computing]
tags: [google]
source: https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/
publish: true
---
# MapReduce

> 한 줄 요약: 개발자가 map과 reduce 두 함수만 쓰면 분산 처리·장애 복구는 런타임이 맡는 대용량 데이터 처리 모델 논문.

## 출처
- 저자·기관: Jeffrey Dean, Sanjay Ghemawat, OSDI 2004
- 날짜: 2004
- 링크: https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/

## 핵심 세 줄
1. map은 입력 키-값을 중간 키-값으로, reduce는 같은 키의 값을 합친다.
2. 입력 분할, 작업 배치, 장비 장애 복구, 장비 간 통신은 런타임이 처리한다.
3. 분산 시스템 경험이 없는 개발자도 거대한 클러스터를 쓸 수 있게 했다.

## 절별 요약
- 프로그래밍 모델: map 함수와 reduce 함수 두 개만 정의한다.
- 실행: 범용 장비 수천 대에서 테라바이트 단위 데이터를 처리한다.
- 의의: Hadoop 등 빅데이터 생태계의 출발점이 됐다.

## 내 생각
- 빅데이터분석기사·AWS DEA의 분산 처리 개념(Spark, EMR, Glue)의 원조다.
- "어려운 부분은 런타임이 맡는다"는 추상화 원칙이 SWEBOK 18 공학 기초의 추상화와 연결된다.

## 어디에 쓸까
- [[16 컴퓨팅 기초]]
