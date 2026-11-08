---
type: source
created: 2026-11-09
area: [testing, quality]
tags: [nvidia]
source: https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html
publish: true
---
# Compute Sanitizer

> 한 줄 요약: CUDA 툴킷에 포함된 정확성 검사 도구 모음. GPU 코드의 메모리 오류·경쟁 상태·초기화 누락·동기화 오용을 찾는다.

## 출처
- 저자·기관: NVIDIA, CUDA 문서
- 날짜: 문서 기준 v2026.3.0
- 링크: https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html

## 핵심 세 줄
1. CUDA 애플리케이션을 네 가지 도구 중 하나로 감싸 실행하며 검사한다.
2. GPU 코드는 디버깅이 어려워서 이런 동적 검사가 필수다.
3. CUDA 툴킷에 기본으로 들어 있다.

## 절별 요약
- Memcheck: 범위 밖·정렬 안 된 메모리 접근, 하드웨어 예외, 메모리 누수.
- Racecheck: 공유 메모리 데이터 경쟁.
- Initcheck: 초기화 안 된 전역 메모리 읽기.
- Synccheck: 동기화 기본 요소의 잘못된 사용.

## 내 생각
- 엔비디아의 품질 관점은 "정확성 검사 도구를 툴킷에 기본 탑재"다. 메타의 Infer(정적)와 대비되는 동적 분석 예시.

## 어디에 쓸까
- [[05 테스트]]
- [[12 품질]]
