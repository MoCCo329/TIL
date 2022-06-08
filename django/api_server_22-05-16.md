## API Server

### 1. SOP, CORS

- Same-Origin Policy(SOP, 동일 출처 정책) : 특정 출처에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는것을 제한하는 보안 방식으로, 잠재적으로 해로울 수 있는 문서를 분리함으로써 안전성을 높힌다. (서버는 작동하지만, 브라우저단에서 막는 것이다.)

- URL의 Protocol, Port, Host가 모두 같아야 동일한 출처로 본다.

  ```
  http://localhost:3000/posts/3
  
  http는 Scheme/Protocol
  localhost는 Host
  3000은 Port
  posts/3은 Path
  ```



- Cross-Origin Resource Sharing Policy(CORS, 교차 출처 리소스 공유) : 추가 HTTP header를 사용하여 특정 출처에서 실행중인 웹 애플리케이션이 다른 출처의 자원에 접근 할 수 있는 권한을 부여하도록 서버가 브라우저에 알려주는 체제이다.
- 즉, 클라이언트와 서버간 통신 사이에 적철한 출처로부터 리소스를 받고 있는지 브라우저가 확인하는 것이다.
- 예를 들어 요청 해더의 "Origin: localhost:8080"과 서버에서 응답으로 받은 "Access-Control-Allow-Origin: *"을 확인하고 승인하는것.



- django-cors-headers 라이브러리 사용

  ```bash
  $ pip install django-cors-headers
  ```

  ```python
  INSTALLED_APPS = [
      ...
      'corheaders',
  ]
  
  MIDDLEWARE = [
      # CommonMiddleware보다 위에 위치해야 한다.
      'corsheades.middleware.CorsMiddleware',
      ...
      'django.middleware.common.CommonMiddleware',
  ]
  
  CORS_ALLOWED_ORIGINS = [
      # 교차 출처 자원 공유를 허용할 Domain 등록
      'http://localhost:8080',
  ]
  ```





### 2. Authentication & Authorization

- Authentication(인증)은 본인이 누구인지(김모씨인지 이모씨인지) 확인하는 행위이다.

  관련된 에러코드로는 401 Unauthorized(미승인이란 단어를 쓰지만 의미상 비인증)

- Authorization(권한 부여, 허가)은 사용자에게 리소스나 기능에 대한 액세스 권한을(일반 사용자인지, 관리자인지) 알맞게 부여하는 과정이다.

  관련된 에러코드로는 403 Forbidden이 있다.

- 일반적으로 사용하는 인증 방식은 다음과 같다.

  - ID/Password : 가장 기본이 되는 방식으로 대부분 password를 암호화하여 DB와 대조

  - Coolie/Session : 서버에서 사용자의 정보를 세션에 기록하여 인증. Stateful하다.

    - Base Auth : Http 헤더에 <id\>:<password\> 값을 담아 전송하는 방식

      로그인시 서버의 authtoken_token 테이블에 레코드가 생기고 토큰값이 담긴다. 생긴 토큰값을 응답하면, 클라이언트에선 토큰값을 저장했다가 매 요청마다 헤더에 넣어 사용자를 인증한다.

      ```html
      Authorization : Basic Base64(id:password)
      ```

  - Web-Token : 토큰 자체로 정보가 있어 별도 인증 서버가 필요 없다
    - JWT
    - OAuth : Gooble, Facebook 같은곳의 정보를 이용해 다른 웹사이트나 애플리케이션의 접근 권한을 부여받는 방식



- dj-rest-auth & django-allauth(signup) 라이브러리 이용

  ```bash
  $ pip install django-allauth
  $ pip install dj-rest-auth
  ```

  ```python
  INSTALLED_APPS = [
  	...
      'rest_framework',
      # token authentication
      'rest_franework.authtoken',
      ...
      # DRF auth 담당
      'dj_rest_auth',  # sing up 제외 모든 Auth 담당
      'dj_rest_auth.registration',
      
      # django allauth
      'allauth',
      'allauth.account',
      ...
      # allauth 사용을 위해 필요
      'django.contrib.site',
      ...
  ]
  
  # django.contrib.sites에서 등록 필요
  SITE_ID = 1
  
  # drf 설정
  REST_FRAMEWORK = {
      # 기본 인증방식 설정
  	'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ],
      
      # 기본 권한 설정
      'DEFAULT_PERMISSION_CLASSES': [
          # 'rest_framework.permissions.AllowAny',  # 기본적으로 모두에게 허용
          'rest_framework.permissions.IsAuthenticated',  # 기본적으로 인증받아야 사용
      ],
  }
  ```

  ```python
  urlpatterns = [
  	...
      path('api/v1/accounts/', include('dj_rest_auth.urls')),  # 패턴은 자유롭게 설정 가능
      path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
  ]
  ```





### 3. JWT

- JSON 포맷을 활용하여 요소 간 안전하게 정보를 교환하기 위한 표준 포맷이다.
- 암호화된 JWT 자체로 검증 가능하기 때문에 self-contained하다.

```html
Authorization : JWT <header>.<payload>.<signature>
```





- DB에서 토큰의 유효성을 검사할 필요가 없다는 장점을 가진다.
- One Source(JWT) Multi Use에 좋다.
- 토큰을 탈취당하면 서버 측에서 토큰 무효화가 불가능하다(블랙리스팅 테이블, 매우 짧은 유효기간이나 Refresh 토큰을 활용하여 보완한다.)

