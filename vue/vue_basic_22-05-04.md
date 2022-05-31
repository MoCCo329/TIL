## Vue.js

### 1. Intro

- Vue.js는 사용자 인터페이스를 만들기 위한 자파스크립트 프레임워크이다.

  다양한 라이브러리를 통해 SPA(Single Page Application)을 지원한다.



- SPA는 단일 페이지로 구성되며 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성한다. 연속되는 페이지로 사용자 경험(UX)을 향상하며 동작의 일부가 CSR의 방식를 따른다.



- CSR(Client Side Rendering)은 클라이언트에서 화면을 구성한다. 최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 리소스를 받고, 이후 클라이언트는 필요한 데이터만 요청해 JS로 DOM을 렌더링하는 방식이다. SPA가 사용하는 렌더링 방식이다.

  서버와 클라이언트간 트래픽이 감소하며 사용자 경험 향상의 장점을 가진다

  최종 렌더링 시점이 SSR에 비해 느리다. SEO(Search Engine Optimization)에 어려움이 있다는 단점이 있다.

- SSR(Server Side Rendering)은 서버에서 화면을 모두 구성하여 전달하는 방식이다. JS이전부터 사용하던 방식.

  초기 구동속도가 빠르고, SEO에 적합하다는 장점을 가진다.

  모든 요청마다 새로운 페이지를 구성해야 하기 떄문에 새로고침이 많고, 트래픽이 많아 서버 부담이 크다.





### 2. Concepts of Vue.js

- Vanilla JS vs Vue.js

  vanilla JS와 달리 Vue는 DOM과 Data와의 연결성이 좋다. 즉 Data가 변경되면 DOM의 내용도 알아서 변경되므로 Data에 대한 관리에 집중할 수 있다.

- MVVM pattern(Model, View, ViewModel)

  사용자에게 보여지는 부분인 View(DOM, 즉 HTML)와 data인 Model(JS Object)을 View Model이 중개하는 패던

  ViewModel은 모든 Vue Instance를 말하며 DOM Listeners와 Directives로  data와 Model을 중개한다.





### 3. Vue 구조(CDN 이용시)

- Vue instance

  Vue앱은 Vue함수로 새 인스턴스를 만드는 것으로 시작한다. 여러 옵션(el, data 등)들로 원하는 동작을 구현한다.

  ```html
  // 선언적 렌더링
  <div id="app1">  <!-- View -->
    {{ message }}
  </div>
  
  
  <script>
    const app = new Vue({  // Vue instance 생성. ViewModel
        el: '#app1',
        data: {  // Model
            message: 'Hello Vue',
        },
        methods: {
            greeting: function () {
                console.log('hello')
            }
        }
    })
  </script>
  ```

- el : Vue 인스턴스와 DOM요소를 연결할때 사용한다.
- data : Vue 인스턴스의 상태 데이터를 정의하는 곳이다. 정의된 데이터는 template에서 interpolation이나 v-bint, v-on과 같은 directive를 통해 사용 가능하며, 동일 객체 내에서는 this 키워드로 접근 가능하다.
- methods : Vue 인스턴스에 추가할 메서드를 정의하는 곳이다. data와 같은 방식으로 접근 가능하며 마찬가지로 this를 Vue 인스턴스로 사용하기 위해 화살표함수로 정의하지 않는다.

- computed: computed에 정의된 함수들은 값이 return값으로 계산되어 존재한다. html에서 함수 실행이 아닌 함수만 선언적으로 적어서 사용 가능하다. method는 화면이 랜더링 될때마다 모두 갱신되어 계산되는 반면 computed는 관련 데이터가 변화할 때에만 계산된다. 선언형 프로그래밍 방식이다.(목표를 정의)

- watch: 변수가 변하는 것을 계속 확인하고 있다가 행동을 취하도록 한다. 명령형 프로그래밍 방식이다.(num이 바뀌면 f를 하라는것처럼 과정을 정의)

  ```html
  watch: {
    num: function (newValue, oldValue) {
  	console.log(`${this.num}이 ${oldValue}에서 ${newValue}로 변경되었습니다.`)
    }
  }
  ```

- filters : filter에서 정의된 함수는 장고에서의 filter 처럼 template에서 사용할 수 있게한다. 따라서 리턴값이 필요하다.

  ```html
  <p>{{ numbers | getOddNumbers | getUnderTen }}</p>
  ```





### 4. Template syntax

- 랜더링된 DOM에서 Vue 인스턴스에 접근하기 위해 HTML 기반 템플릿 구문을 선언적으로 사용할 수 있다.



- Interpolation(보간법) : Vue 인스턴스의 데이터를 DOM에 바인딩 할 수 있는 html기반 탬플릿 문법이다. 이 중 몇가지는 디렉티브(v-)가 사용된다.

  1. Text : Mustache(이중 중괄호)를 이용한다. message값이 변경될 때 마다 갱신된다.

     ```html
     <span>메시지: {{ message }}</span>
     <span v-text="message"></span>  // 바인딩 안해도 된다.
     ```

  2. Raw HTML : v-html 디렉티브를 이용한다. 문자열의 html 문법이 적용된 상태로 표시된다.

     ```html
     <span v-html="rawHtml"></span>
     ...
     data: {
       rawHtml: '<string>message</string>'  // v-html을 쓰면 strong 태그가 적용되어 나온다.
     }
     ```

  3. Attributes : v-bind를 통해 data의 key값으로 value를 불러와 태그속성을 부여할 수 있다.

     ```html
     <div v-bind:id="dynamicId"></div>
     ```

  4. JS 표현식 : Mustache 구문 안에서 JS의 표현식을 사용 가능하다.

     ```html
     {{ number + 1 }}
     {{ message.split('').reverse().join('') }}
     ```

- Directive(디렉티브) : DOM을 제어하기 위한 지시(Directive)를 말한다. v-접두사가 있는 특수 속성으로 일부 디렉티브는 ':'를 통해 전달인자(Arguments)를 받을 수 있으며, '.'을 통해 수식어(Modifiers)를 추가로 표현할 수 있다.

  1. v-text : interpolation의 Mustache문법이 v-text로 컴파일 되며 같은 결과를 얻는다.

  2. v-html : 엘리먼트의 innerHTML을 업데이트한다. XSS공격에 취약하다.

  3. v-show : 엘리먼트에 style="display: none;"을 추가/삭제하며 속성을 토글한다. 요소는 항상 렌더링되고 DOM에 남아있는다. 화면에 토글(전환)하는 비용이 v-if에 비해 적다.

  4. v-if, v-else-if, v-else : 조건이 true일 때 요소를 렌더링한다. 렌더링 자체가 되지 않으므로 자주 바뀌지 않는다면 렌더링 비용을 낮춘다.

  5. v-for : 반복 가능한 원본 데이터를 기반으로 엘리먼트를 반복하여 렌더링한다. 반드시 각 item별로 다른 값을 가지는 key 속성을 작성해야한다. v-if와 사용시 v-for의 우선순위가 더 높다. idx도 함께 표현 가능하다.

     ```html
     <div v-for="(fruit, idx) in fruits" :key="idx">{{ fruit }}</div>
     ```

  6. v-on : 엘리먼트에 이벤트 리스너를 연결한다. 이벤트 유형은 전달인자(':') 로 표시한다. 'v-on:'을 줄여 '@'로 표현 가능하다. .prevent 수식어를 통해 해당 이벤트를 막을수도 있다. 이벤트 발생시 = 뒤의 함수를 불러오며 기본으로 event인자가 넘어가지만 다른 인자를 적을 경우 적은 인자가 1번으로 넘어간다.

     ```html
     <button v-on:click="alertHello"></button>
     <form @submit.prevent>
     <input @keyup.enter="f('hello')">
     ```

  7. v-bind : HTML요소의 속성에서 Vue의 상태 데이터를 사용할 수 있게한다. 'v-bind:'를 줄여 ':'로 사용 가능하다. Object 형태로 사용시 Object의 value가 참일 경우 key값이 들어간다.

     ```html
     <img v-bind:src="imageSrc">
     <div :class="{ active: isRed }"></div>
     <p :style="{ fontSize: fontSize + 'px' }"
     ```

  8. v-model : HTML form 요소의 값과 data를 양방향 바인딩 한다. .lazy(input 대신 change 이벤트 이후에 동기화), .number(문자열을 숫자로 변경), .trim(입력에 대해 trim을 진행) 등의 수식어가 존재한다.

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





### 5. Life Cycle Hocks

- 각 Vue 인스턴스는 생성될 때 일련의 과정을 거친다. 특정 과정들을 거칠 때 사용자 정의 로직을 실행할 수 있는 Lifecycle Hooks가 호출된다.
- created(Vue 인스턴스 생성시 호출) - mounted(DOM에 인스턴스가 모두 마운트 된 후 호출) - updated(데이터가 변경되어 DOM이 다시 랜더링 된 후 호출) - destoryed(Vue 인스턴스가 제거된 후에 호출)
