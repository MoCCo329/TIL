## Vue.js

### 1. Intro

- Vue.js는 사용자 인터페이스를 만들기 위한 자파스크립트 프레임워크이다.

  다양한 라이브러리를 통해 SPA(Single Page Application)을 지원한다.



- SPA는 단일 페이지로 구성되며 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성한다. 연속되는 페이지로 사용자 경험(UX)을 향상하며 동작의 일부가 CSR의 구조를 따른다.



- CSR(Client Side Rendering)은 클라이언트에서 화면을 구성한다. 최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 리소스를 받고, 이후 클라이언트는 필요한 데이터만 요청해 JS로 DOM을 렌더링하는 방식이다. SPA가 사용하는 렌더링 방식이다.

  서버와 클라이언트간 트래픽이 감소하며 사용자 경험 향상의 장점을 가진다

  최종 렌더링 시점이 SSR에 비해 느리다. SEO(Search Engine Optimization)에 어려움이 있다는 단점이 있다.

- SSR(Server Side Rendering)은 서버에서 화면을 모두 구성하여 전달하는 방식이다. JS이전부터 사용하던 방식.

  초기 구동속도가 빠르고, SEO에 적합하다는 장점을 가진다.

  모든 요청마다 새로운 페이지를 구성해야 하기 떄문에 새로고침이 많고, 트래픽이 많아 서버 부담이 크다.



### 2. 



```javascript
<div id="app1">  // View
</div>


new Vue({  // ViewModel
    el: '#app1',
    data: {  // Model
        message: 'Hello Vue'
    }
})
```





v-show

v-if (Reactive)

v-else-if

v-for="(value, idx) in iterator"

v-bind: (줄여서 :)  ( :class="{ active: isRed}" : isRed값에 따라 active가 설정)





\<div v-for="(fruit, idx) in fruits" :key="idx"\> : key가 꼭 필요하며 이는 바인딩하여 독립적인 값으로 설정하는것이 좋다.



v-on:click="alertHello" (줄여서 @click)

preventDefault는 @event.prevent="이벤트시 콜백함수"

@keyup.sapce="f" (space칠때만 f 실행 마찬가지로 .enter

추가인자는 "f /args => ('추가인자')"



method에 함수 작성시 this를 이용해 객체.변수에 접근하지만, 태그에 작성시 바로 변수명으로 접근 가능하다.



input -> Data 단방향

```html
\<input type="text" @input="onInputChange"\>


data: {
  msg1: '1',
}
methods: {
  onInputChang (event) {
    this.msg1 = event.target.value  // input값이 msg1으로 저장된다.
  }
}
```



input <-> Data 양방향

```html
<input type="text" v-model="msg2">


data: {
  msg2: '1',
}
methods: {
  onInputChang (event) {
    this.msg2 = event.target.value  // input값이 msg1으로 저장된다.
  }
}
```



computed: { } 내부 함수들은 값이 계산되어 존재한다. 따라서 html에서 함수 실행이 아닌 함수만 적어야 한다. 즉 종속 대상을 따라 저장(캐싱)된다.



watch: { } 는 변수가 변하는 것을 계속 확인하고 있다가 행동을 취하도록 하는 명령형 구역



{{ numbers | getOddNumbers | getUnderTen }} 장고에서 filter 처럼 함수를 사용할 수 있다.





vue instance life cycle



created ....





정리는 나중에..
