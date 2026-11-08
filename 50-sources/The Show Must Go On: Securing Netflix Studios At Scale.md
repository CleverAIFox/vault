---
type: source
created: 2026-11-09
area: [security, architecture, design]
tags: [netflix]
source: https://netflixtechblog.com/the-show-must-go-on-securing-netflix-studios-at-scale-19b801c86479
publish: true
---
# The Show Must Go On: Securing Netflix Studios At Scale

> 한 줄 요약: 넷플릭스가 보안 요구사항을 체크리스트 대신 공용 프록시(Wall-E)의 필터로 옮겨, 보안을 기본값으로 만든 사례.

## 출처
- 저자·기관: Netflix Technology Blog(원문 접근 실패, 재게시본으로 확인)
- 날짜: 2021-09
- 링크: https://netflixtechblog.com/the-show-must-go-on-securing-netflix-studios-at-scale-19b801c86479

## 핵심 세 줄
1. Zuul 기반 프록시 Wall-E에 SSO 인증 필터를 넣어, 뒤에 있는 모든 서비스가 인증을 보장받게 했다.
2. 보안 체크리스트 항목을 하나씩 Wall-E 필터로 옮겨, 앱 개발자 책임에서 플랫폼 책임으로 바꿨다.
3. 결국 외부 공개 체크리스트가 "Wall-E를 쓰는가" 한 줄로 줄었다.

## 절별 요약
- 방식: 보안 요구사항을 프록시 필터로 추가하는 패턴.
- 도입: 처음엔 보안 팀이 골라 권했고, 설정 마법사와 선언형 설정으로 몇 분 안에 붙게 했다.
- 효과: 보안 때문이 아니라 "더 빨리 출시할 수 있어서" 다른 팀들이 스스로 채택했다.

## 내 생각
- 보안 paved road의 대표 사례다. 강제보다 "쓰면 더 편한 길"을 만드는 게 Thoth 생태계 설계 원칙과 같다.
- 원문 주소는 「확인 필요」(넷플릭스 블로그 접근이 막혀 재게시본으로 확인).

## 어디에 쓸까
- [[13 보안]]
- [[02 아키텍처]]
- [[03 설계]]
