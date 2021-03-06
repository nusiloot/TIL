# 01. SSR & CSR

<br>

## 1. SSR(Server Side Rendering)

- 전통적인 웹 어플리케이션 방식으로, 브라우저에서 서버측으로 요청할 때마다 서버에서 처리하여 해당 페이지에 관련된 HTML, CSS, JS 파일 및 데이터를 받아오고 새로고침으로 페이지를 응답하여 렌더링 시킨다.
- 웹에서 기능과 데이터가 많아지면서 SPA가 생김
- 장점
  - 초기 로딩 속도가 빠르므로 사용자가 컨텐츠를 빨리 볼 수 있다.
  - JS를 이용한 렌더링이 아니므로 검색엔진 최적화(SEO)가 가능
- 단점
  - 매번 페이지를 요청할 때마다 새로고침되기 때문에 사용자 경험이 다소 좋지 않다.
  - 서버에 매번 요청을 하므로 서버의 부하가 커진다.

<br>

## 2. CSR(Client Side Rendering)

- 클라이언트에서 Javascript를 통해 렌더링 하는 방식
- 브라우저가 서버에 HTML과 JS 파일을 요청한 후 로드되면 사용자의 상호작용에 따라 JS를 이용해서 동적으로 렌더링을 시킨다.
- SPA 형식의 대부분 프론트엔드 프레임워크가 CSR 방식으로 시작됨
- 초기 렌더링 시간 비용, SEO, 메타 데이터 동적 생성의 한계를 극복하기 위해 SSR 프레임워크를 모두 보유하고 있음
- 장점
  - 첫 로딩만 기다리면, 동적으로 빠르게 렌더링 되므로 사용자 경험(UX)이 좋다.
  - 서버에게 요청하는 횟수가 훨씬 적어지므로 서버의 부담이 덜하다.
- 단점
  - 모든 스크립트 파일이 로드될 때까지 기다려야 한다.
    - 리소스를 청크(chunk) 단위로 묶어서 요청할 대만 다운받게 하는 방식으로 완화시킬 수 있지만 완벽히 해결할 수는 없다.
  - 검색엔진의 검색 봇이 크롤링을 하는데 어려움을 겪기 때문에 검색엔진 최적화(Search Engine Optimization)의 문제가 있다.
    - 구글 봇의 경우는 JS를 지원하지만, 다른 검색엔진의 경우 그렇지 않기 때문에 문제가 된다.

<br>

## 3. SPA

- 서버로부터 완전한 새로운 페이지를 불러오지 않고 현재의 페이지를 동적으로 다시 작성함으로써 특정 부분만 사용자와 소통하는 웹 애플리케이션이나 웹 사이트

- SPA의 가장 중요한 목표이자 핵심가치는 <b><u>사용자 경험(UX) 향상</u></b>이다.
  - 부가적으로 속도의 향상도 기대할 수 있다.
- <b>초기 구동 속도가 다소 느리다</b>는 단점이 있다.
  - 웹 애플리케이션에 필요한 모든 정적 리소스를 최초에 한번 다운로드하므로 초기 구동 속도가 상대적으로 느리다.
- 같은 페이지에서 필요한 부분만 변경되기 때문에 URL 주소가 변경되지 않는다.

---

:heavy_check_mark: (참고) MPA(Multiple Page Application)

- 사용자가 페이지를 요청할 때마다, 웹 서버가 요청한 UI와 필요한 데이터를 HTML로 파싱해서 보여주는 방식의 웹 어플리케이션이다.
- 전통적인 방식을 이용한다면, SPA가 사용하는 렌더링 방식은 CSR이고, MPA가 사용하는 렌더링 방식은 SSR이다.

<br>

---

:book: <b>Reference</b>

- https://yunzema.tistory.com/103
- https://github.com/baeharam/Must-Know-About-Frontend/blob/master/Notes/frontend/csr-ssr.md