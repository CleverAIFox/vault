---
type: source
created: 2026-11-09
area: [architecture, operations]
tags: [amazon]
source: https://aws.amazon.com/builders-library/
publish: true
---
# Amazon Builders' Library

> 한 줄 요약: 아마존 선임 엔지니어들이 대규모 시스템을 어떻게 설계·배포·운영하는지 직접 쓴 글 모음.

## 출처
- 저자·기관: 아마존 선임 엔지니어·기술 리더들, Amazon Web Services
- 날짜: 2019년 re:Invent에서 공개, 이후 계속 추가
- 링크: https://aws.amazon.com/builders-library/

## 핵심 세 줄
1. 설계 결정의 트레이드오프와 운영에서 얻은 교훈을 글로 남긴다.
2. 주제는 아키텍처, 소프트웨어 전달, 운영이다.
3. 이론보다 실제 사례 중심이라 바로 따라 할 수 있다.

## 절별 요약
- Timeouts, retries, and backoff with jitter: 호출 실패는 반드시 일어난다. 타임아웃·재시도·지수 백오프에 무작위성(지터)을 더해 재시도 폭주를 막는다.
- Static stability using Availability Zones: 장애가 난 뒤 늘리지 말고, 미리 여유를 두어 장애가 나도 그대로 버티게 설계한다.
- 그 밖에 부하 차단(load shedding), 큐 적체 피하기, 헬스 체크, 안전한 자동 배포, 멱등 API 같은 글이 있다.

## 내 생각
- 법제처 API 호출(Maat 수집기)에 타임아웃·재시도·지터를 넣을 때 이 글이 근거가 된다.
- 글 하나가 개념 노트 하나가 될 만큼 밀도가 높다. 읽는 대로 20-concepts로 쪼갠다.

## 어디에 쓸까
- [[02 아키텍처]]
- [[06 운영]]
