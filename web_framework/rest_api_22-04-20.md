## Rest API

### 1. HTTP

- HyperText Transfer Protocol의 약자로 웹상에서 컨텐츠를 전송하기 위한 프로토콜(규칙, 약속)이다.
- Stateless, Connectionless의 특성을 가지고 있다. 때문에 쿠키와 세션을 통해 서버 상태를 요청과 연결한다.

- Method, Path, Version of the protocol, Headers를 요청하고 Version of the protocol, Status code, Status message, Headers의 응답을 받는다.

- Method는 자원에 대한 행위를 정의한다. 즉 주어진 리소스에 수행하길 원하는 행동을 나타낸다.

  GET은 조회, POST는 작성, PUT은 수정, DELETE는 삭제

- Status code는 HTTP요청이 성공적으로 완료되었는지 여부를 나타낸다.

  Informational responses(1XX)

  Successful responses(2XX)

  Redirection messages(3XX)

  Client error responses(4XX)

  Server error responses(5XX)



- URI(Uniform Resource Identifier)는 리소스는 식별을 위해 HTTP 전체에서 사용되는 통합 자원 식별자이다. URI의 하위 개념으로 URL과 URL이 있으며 URL은 URII와 같은 의미처럼 사용하기도 한다.
- URL(Uniform Resource Locator)는 자원의 위치를 나타낸다. 과거에는 실제 위치를 나타냈지만, 현재는 추상화된 의미론적 구성을 지닌다.(웹 주소, 링크 라고도 한다)
- URN(Uniform Resource Name)은 자원의 위치에 영향을 받지않는 이름 역할을 한다.



- URI의 구조

  Scheme(protocol) : 브라우저가 사용해야 하는 프로토콜로 http, data, file, ftp 등이 있다.

  Host(Domain name) : 요청을 받는 웹 서버의 이름. IP address를 직접 이용할 수도 있다.

  Port : 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문 HTTP 80, HTTPS 443 등이 있다.

  Path : 웹 서버 상의 리소스 경로이다. 초기에는 실제 물리 위치를 나타냈지만, 오늘날은 추상적인 구조로 표현.

  Query(Identifier) : query sting parameters로 웹 서버에 제공되는 추가 매개변수이다. ? 뒤에서 &로 구분되								는 key-value 목록이다.

  Fragment : anchor로 자원 안에서 북마크의 한 종류이다. 해당 문서의 특정 부분만 보여줄 때 사용한다. 서버								에 요청을 보내지는 않으며 브라우저에게 알려주는 요소이다.



### 2. RESTful API

- API(Application Programming Interface)는 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스이다.

  CLI는 명령줄, GUI는 그래픽으로 기능을 수행했다면, API는 프로그래밍을 통해 특정한 기능을 수행하는 것이다.(애플리케이션과 프로그래밍으로 소통하는것)

- REST(REpresentational State Transfer)는 API서버를 개발하기 위한 설계 방법론이다. 네트워크 상에서 자원을 정의하고, 자원에 대한 주소를 지정하는 전반적인 방법이다. REST를 따르는 시스템을 RESTful이라 한다.

  자원은 URI로, 행위는 HTTP Method(GET, HOST, PUT, DELETE)로, 표현은 JSON으로 한다.

- JSON은 JavaScript의 표기법을 따르는 단순 문자열이다. 가볍고 사람이 읽고 쓰기 쉬우며 기계가 파싱(해석, 분석)하고 만들기에도 쉽다.



0421에 정리예정