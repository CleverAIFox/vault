---
type: source
created: 2026-11-09
area: [security, operations, maintenance]
tags: [nvidia]
source: https://www.nvidia.com/en-us/security/psirt-policies/
publish: true
---
# NVIDIA PSIRT

> 한 줄 요약: 엔비디아 제품 보안 사고 대응팀(PSIRT)의 정책. 취약점을 받고, 조사하고, 고치고, 조율된 방식으로 공개한다.

## 출처
- 저자·기관: NVIDIA
- 날짜: 상시
- 링크: https://www.nvidia.com/en-us/security/psirt-policies/

## 핵심 세 줄
1. 취약점 접수·조사·조율·수정·공개를 한 팀이 맡는다.
2. 조율된 취약점 공개(CVD): 고치기 전에는 비공개로 다룬다.
3. 심각도는 CVSS v3.1 점수로 매긴다.

## 절별 요약
- 접수: 독립 연구자, 업계, 협력사, 고객의 신고를 받는다.
- 공개: 수정이나 완화책이 나오면 보안 공지(bulletin)로 알린다. 영향 제품, CVE, CVSS, 조치 방법, 신고자 감사.
- 심각도: 치명(9.0~10.0)·높음·중간·낮음·없음.
- 긴급 공지: 공개적으로 주목받거나 악용 가능성이 크면 패치 전이라도 알린다.

## 내 생각
- Maat 저장소의 SECURITY.md(보안 정책)를 쓸 때 이 구조를 본보기로 쓴다.
- GitHub의 비공개 취약점 신고(private vulnerability reporting)가 같은 흐름이다.

## 어디에 쓸까
- [[13 보안]]
- [[06 운영]]
- [[07 유지보수]]
