404에러가 나면 router.push({ name: 'notFound404' })



beforeEach((to, from, next) => {})를 통해서 URL을 이동할때마다 검문 가능

from에서 to로 갈 때 각 위치에 따라 다른 결과를 나타낼 수 있다.

ex)

```vue
router.beforeEach((to, from, next) => {
  // 로그인 여부 확인
  const { isLoggedIn } = store.getters
  // Auth가 필요한 router들
  const authPages = ['articleNew', 'articleEdit']
  // 현재 이동하고자 하는 페이지가 Auth가 필요한가?
  const isAuthRequired = authPages.includes.(to.name)  // 인자 to의 정보
  // Auth가 필요한데, 로그인 되어있지 않다면?
  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'login' })
  } else{
    next()
  }
})
```





### Vuex Module

- store아래에 각 기능별로 하위 폴더를 만들고(혹은 만들지 않고) 그 안에 모듈 내용을 담는다.
- index.js(대포 파일)에 모든 모듈을 통합한다.





새로고침할 때 토큰 사라지는것을 방지 => localstorage에 token이 있으면 그 값, 아니면 ''