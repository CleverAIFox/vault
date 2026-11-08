---
type: source
created: 2026-11-09
area: [computing, architecture]
tags: [netflix]
source: https://openconnect.netflix.com/en/
publish: true
---
# Netflix Open Connect

> 한 줄 요약: 넷플릭스가 자체 캐시 서버(OCA)를 인터넷 사업자 망 안에 무상으로 두어 영상 트래픽을 지역화하는 콘텐츠 전송 프로그램.

## 출처
- 저자·기관: Netflix, openconnect.netflix.com
- 날짜: 상시
- 링크: https://openconnect.netflix.com/en/

## 핵심 세 줄
1. 넷플릭스 트래픽을 ISP 망 안에서 처리해 중계 구간을 줄인다.
2. 자격을 갖춘 ISP에는 캐시 서버(OCA)를 무상으로 제공한다.
3. 1,000곳 넘는 ISP와 협력한다.

## 절별 요약
- 내장형 OCA: ISP 망 안에 넣는 넷플릭스 서버. BGP로 트래픽을 조정하고 넷플릭스가 감시·유지한다.
- 직접 연결(SFI): IXP 피어링이나 전용 연결로 넷플릭스 데이터센터와 잇는다. 야간 콘텐츠 채우기에도 쓰인다.
- 도입 절차: 요청 → 요건 확인 → 망 설계 → 계약 → 현장 조사 → 설정. 미리 채우는 데 1~2주.

## 내 생각
- SWEBOK 16 컴퓨팅 기초의 네트워크가 사업 구조가 된 예다. 정보처리기사 네트워크 공부와 연결된다.

## 어디에 쓸까
- [[16 컴퓨팅 기초]]
- [[02 아키텍처]]
