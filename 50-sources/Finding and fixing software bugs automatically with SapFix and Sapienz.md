---
type: source
created: 2026-11-09
area: [testing, maintenance, quality]
tags: [meta]
source: https://engineering.fb.com/2018/09/13/developer-tools/finding-and-fixing-software-bugs-automatically-with-sapfix-and-sapienz/
publish: true
---
# Finding and fixing software bugs automatically with SapFix and Sapienz

> 한 줄 요약: 메타가 자동 테스트 도구 Sapienz로 충돌 버그를 찾고, SapFix로 수정 패치까지 자동 생성해 사람이 검토 후 배포한 사례.

## 출처
- 저자·기관: Yue Jia, Ke Mao, Mark Harman, Engineering at Meta 블로그
- 날짜: 2018-09-13
- 링크: https://engineering.fb.com/2018/09/13/developer-tools/finding-and-fixing-software-bugs-automatically-with-sapfix-and-sapienz/

## 핵심 세 줄
1. Sapienz는 앱을 자동으로 테스트해 충돌과 원인 코드 줄을 찾는다. 보고의 약 4분의 3이 실제 수정으로 이어졌다.
2. SapFix는 그 버그의 수정 패치 후보를 자동으로 만들고 검증한다.
3. 최종 결정은 언제나 사람이 한다. 스스로 운영에 배포하지 않는다.

## 절별 요약
- SapFix 전략: 원인 변경 되돌리기 → 과거 사람 패치에서 뽑은 템플릿 적용 → 구문 트리를 조금씩 변형.
- 검증: 컴파일, 충돌 재현 여부, 새 충돌 여부를 확인하고 개발자 테스트와 Sapienz 테스트를 돌린다.
- 결과: 페이스북 안드로이드 앱으로 수백만 기기에 자동 생성 수정이 배포됐다.

## 내 생각
- AI가 패치를 만들고 사람이 검토하는 구조가 지금의 AI 코딩 에이전트와 같다. 2018년에 이미 그 원형이 있었다.
- Maat에서 AI 에이전트 PR을 받을 때 "검증 통과 후 사람 승인" 규칙의 근거로 쓴다.

## 어디에 쓸까
- [[05 테스트]]
- [[07 유지보수]]
- [[12 품질]]
