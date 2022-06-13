## Vue router / Vuex Module

### 1. 404 NOT FOUND

- vue router에 등록되지 않은 routes 일 경우(/no-such-routes => /* 에 걸려서 404로)

- vue router에 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우(/articles/99999990 => catch에서 router.push({ name: 'NotFount404' }))





### 2. Navigation Guard

- .beforEach를 통해 URL을 이동할 때마다, 이동하기 전 모든 경우에 전역 가드를 거치도록 할 수 있다.

  to : 이동하려는 route의 정보를 담은 객체

  from : 직전 route의 정보를 담은 객체

  next : 실제 route의 이동을 조작하는 함수. 반드시 마지막에 next()로 route 이동을 실행해야 한다.

  ```javascript
  const routes = []
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  router.beforeEach((to, from, next) => {
    store.commit("SET_AUTH_ERROR", null)  // 이전 페이지에서 발생한 에러 삭제
  
    const { isLoggedIn } = store.getters
    const noAuthPages = ["login", "signup"]
    const isAuthRequired = !noAuthPages.includes(to.name)  // 가려는 곳이 로그인 필요한경우
  
    if (isAuthRequired && !isLoggedIn) {  // 로그인 안되있는데, login, signup으로 가려하면 홈으로
      next({ name: 'login' })
    } else {
      next()
    }
    next()
  
    if (!isAuthRequired && isLoggedIn) {
      next({ name:'home' })
    }
  })
  
  export default router
  ```





### 3. Vuex Module

- 단일 파일(@/store/index.js)에 모든 state, getters, mutations, actions를 작성할 경우 프로젝트가 커지면 단일 파일의 크기가 너무 커지게 된다.
- 기능에 따라 파일들을 모듈로 분리하여 사용해 가독성과 유지보수 측면을 높힌다.



- 방법

  1. store아래에 각 기능별로 하위 폴더를 만들고(혹은 만들지 않고) 그 안에 모듈 내용을 담는다.

  ```javascript
  // @/store/modules/accounts.js
  
  export default {
    state: {},
    getters: {},
    mutations: {},
    actions: {},
  }
  
  
  // @/store/modules/articles.js
  
  export default {
    state: {},
    getters: {},
    mutations: {},
    actions: {},
  }
  ```

  2. index.js(대표 파일)에 모든 모듈을 통합한다.

  ```javascript
  // @/store/index.js
  import accounts from './modules/accounts'
  import articles from './modules/articles'
  
  ...
  export default new Vuex.Store({
    modules: {
      accounts,
      articles,
    }
  })

- 다른 module에 작성되어도 실제로는 global namespace에 등록된다. 각 모듈 내부에서 namespaced: true를 사용하면 해당 모듈의 모든 내용은 모듈의 경로를 기반으로 네임스페이스가 지정된다.

  accounts 모듈의 경우 getters['accounts/currentUsername'], dispatch('accounts/fetchLogin') 과 같이 사용 가능하다.





### 4. 기타

- Api interceptors : interceptors 를 통해 then이나 catch로 처리되기 전 요청과 응답을 가로챌 수 있다.

  ```javascript
  // 요청 인터셉터 추가하기
  axios.interceptors.request.use(function (config) {
      // 요청이 전달되기 전에 작업 수행
      const token = localStorage.getItem("token")
  	if (!token) return config
      config.headers.Authorization = `Token ${token}`
  	return config
      // 요청 오류가 있는 작업 수행
    }, function (error) {
      return Promise.reject(error)
    });
  
  // 응답 인터셉터 추가하기
  axios.interceptors.response.use(function (response) {
      // 2xx 범위에 있는 상태 코드는 이 함수를 트리거 합니다.
      // 응답 데이터가 있는 작업 수행
      return response
    }, function (error) {
      // 2xx 외의 범위에 있는 상태 코드는 이 함수를 트리거 합니다.
      // 응답 오류가 있는 작업 수행
      return Promise.reject(error)
    });
  ```




- Guard Clauses : Guard란 조건 분기에서 계속 실행되기 위해 true 여야 하는 boolean expression을 의미한다. if절에 return을 사용하고 else절을 없애 code depth 변화 없이 작성하는것들을 Guard Clauses라 한다.

  ```javascript
  if (guard) {
    ...
  } else {
    ...
  }
  
  // 위의 코드를 Guard Clause로 작성하면 아래와 같다.
    
  if (not guard) {
    return ...
  }
  ...
  ```

  if/else문이 중첩될 수록 code depth가 깊어지며, 가독성이 낮아진다. 이를 Guard Clauses로 평탄화(Flattening) 하여 코드의 가독성을 높힐 수 있다.

