---
type: source
created: 2026-11-09
area: [construction, computing, process]
tags: [nvidia]
source: https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/
publish: true
---
# CUDA C++ Best Practices Guide

> 한 줄 요약: 엔비디아 GPU에서 최고 성능을 내기 위한 개발 지침. 평가 → 병렬화 → 최적화 → 배포(APOD)를 반복하는 주기를 제시한다.

## 출처
- 저자·기관: NVIDIA, CUDA 문서
- 날짜: 문서 기준 v13.5
- 링크: https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/

## 핵심 세 줄
1. 먼저 측정해서 시간을 가장 많이 쓰는 곳을 찾고, 거기부터 병렬화한다.
2. 평가·병렬화·최적화·배포(APOD)를 한 번에 끝내지 않고 반복한다.
3. 부분만 빨라진 버전이라도 일찍 운영에 내보낸다.

## 절별 요약
- 평가(Assess): 실행 시간을 가장 많이 먹는 부분을 찾고 속도 향상의 상한을 추정한다.
- 병렬화(Parallelize): GPU 최적화 라이브러리, 컴파일러 지시문, 코드 재구성으로 병렬성을 드러낸다.
- 최적화(Optimize): 바꿀 때마다 테스트·검증하며 조금씩 개선한다.
- 배포(Deploy): 일부만 빨라진 버전이라도 일찍 내보내고 주기를 다시 돈다.
- 권고마다 우선순위(높음·낮음 등)를 붙여 무엇부터 할지 알려 준다.

## 내 생각
- 엔비디아는 회사 공학 프로세스를 공개하지 않는다. 대신 개발자 문서에 담긴 방법론(APOD)을 관점으로 쓴다.
- "측정 먼저, 최적화는 나중, 작게 자주 배포"는 GPU가 아니어도 통하는 원칙이다. 테슬라 5단계 알고리즘의 순서와도 닮았다.

## 어디에 쓸까
- [[04 구축]]
- [[16 컴퓨팅 기초]]
- [[10 공학 프로세스]]
