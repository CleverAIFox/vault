---
type: source
created: 2026-11-09
area: [operations, quality, engineering]
tags: [amazon]
source: https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/
publish: true
---
# Correction of Error

> 한 줄 요약: 장애가 끝난 뒤 영향·타임라인·다섯 번의 왜·재발 방지 조치를 문서로 남기는 아마존의 사후 분석 방식(COE).

## 출처
- 저자·기관: Luis Caro, Juan Ossa, Johnny Hanley, AWS Cloud Operations 블로그
- 날짜: 2022-02-18
- 링크: https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/

## 핵심 세 줄
1. 실패를 기록하는 데서 그치지 않고 바로잡는 조치에 초점을 둔다.
2. 누구 탓인지가 아니라 왜 일어났는지를 묻는다(비난 없는 분석).
3. 장애의 영향을 먼저 줄인 뒤에 시작한다.

## 절별 요약
- 사건 요약: 비기술 임원도 읽을 수 있게 누가·언제·어디서·어떻게 영향을 받았고 언제 감지·완화했는지.
- 영향: 고객과 사업에 미친 영향을 숫자로.
- 타임라인: 첫 계기부터 정상화까지 시간순, 시간대와 근거 링크 포함.
- 지표: 영향을 정의하고, 문제를 발견하고, 감시하는 데 쓴 측정값.
- 사건 질문: 감지·진단·완화에 관한 질문.
- 예방(다섯 번의 왜): 증상이 아니라 근본 원인에 닿을 때까지 왜를 묻는다.
- 조치 항목: 우선순위·담당자·기한이 있는 재발 방지 작업.
- 관련 항목: 관련 COE와 문서 링크.

## 내 생각
- 볼트의 incident 템플릿(왜 다섯 번, 재발 방지 표)이 이 구조를 줄인 것이다. 템플릿의 근거로 링크해 둔다.
- "오류를 바로잡는다"는 이름이 사람의 실수를 탓하는 느낌을 준다는 비판도 있다. 쓸 때는 비난 없는 원칙을 꼭 같이 지킨다.

## 어디에 쓸까
- [[06 운영]]
- [[12 품질]]
- [[18 공학 기초]]
