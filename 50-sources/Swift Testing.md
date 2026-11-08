---
type: source
created: 2026-11-09
area: [testing]
tags: [apple]
source: https://developer.apple.com/documentation/testing
publish: true
---
# Swift Testing

> 한 줄 요약: 애플의 Swift용 테스트 프레임워크. 속성(attribute) 하나로 테스트를 정의하고, 매개변수화·태그·병렬 실행을 기본으로 지원한다.

## 출처
- 저자·기관: Apple, Apple Developer 문서(오픈소스)
- 날짜: WWDC 2024 공개
- 링크: https://developer.apple.com/documentation/testing

## 핵심 세 줄
1. 거의 어디서나 속성 하나로 테스트 함수를 정의한다.
2. 하나의 테스트 함수를 여러 입력으로 돌리는 매개변수화 테스트를 지원한다.
3. 기존 XCTest 테스트를 옮겨 올 수 있다.

## 절별 요약
- 구성: 타입 시스템으로 테스트를 계층화(suite), 태그로 분류.
- 실행: Swift 동시성과 통합, 프로세스 안 병렬 실행, 실행 조건에 따른 활성화.
- 추적: 버그를 그 버그를 검증하는 테스트와 직접 연결.
- 검증: 기대값·결과·비동기 이벤트 확인, 알려진 이슈 표시, 첨부 파일.

## 내 생각
- pytest의 parametrize·marker와 거의 같은 개념이다. Maat 테스트 규칙(태그로 느린 테스트 분리 등)을 정할 때 비교한다.

## 어디에 쓸까
- [[05 테스트]]
