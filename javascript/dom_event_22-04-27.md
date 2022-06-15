## DOM 조작과 Event

### 1. DOM

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 각 요소를 객체로 취급하며, 주요 객체로는 window(DOM을 표현하는 창, 최상위 객체), document(페이지 컨텐츠의 Entry Poing 역할을 한다), history, navigator등이 있다.
- 접근, 메서드 활용, 프로그래밍 언어적 특성을 활용한 조작이 가능하다.

- 선택(Selection)과 변경(Manipulation)으로 DOM 조작이 이루어 진다.





### 2. DOM 선택

- querySelector : 제공한 선택자와 일치하는 element 하나를 선택한다.

- querySelectorAll : 제공한 선택자와 일치하는 여러 element를 선택한다.

- getElementById(id)

  getElementsByTagName(name)

  getElementsByClassName(names)

  도 사용 가능하지만, querySelector, querySelectorAll을 사용하는 이유는 실시간 반영이 되지 않아 예상치 못한 오류를 막을 수 있으며 id, class, tag 를 모두 사용 가능하고 더 구체적으로 유연하게 선택 가능하기 때문이다.

- 선택 메서드별 반환 타입

  1. 단일 element

     getElementById()

     querySelector()

  2. HTMLCollection (name, id, index 속성으로 각 항목에 접근 가능)

     getElementsByTagName()

     getElementsByClassName()

  3. NodeList (index로만 각 항목에 접근 가능, 배열에서 사용하는 forEach 등 여러 메서드 사용 가능)

     querySelectorAll()
  
  
  
  ```javascript
  const h1 = document.querySelector('h1')  // h1 태그 선택하여 변수 h1에 담기.
  const secondH2 = document.querySelector('#location-header')  // 해당 id를 선택
  const liTage = document.querySelector('.ssafy-loaction')  // 해당 class를 선택
  
  // CSS에서 id를 잘 쓰지 않았던 것은 JS에서 사용하기 위함이 크다. id는 camelCase로 네이밍한다.
  ```





### 2. DOM 조작

- creationElement

  ```javascript
  const newH1 = document.createElement('h1') 없던 태그 생성
  ```

- append, appendChild

  ```javascript
  // append
  const newLiTag = document.createElement('li')
  const ulTag = document.querySelector('ul')
  ulTag.append(newLiTag)  // 동시에 여러개도 가능하다.
  newLiTage.innerText = 'New Tag'  // ul태그 안에 꼭 li태그로 넣지 않아도 append로 넣을 순 있다.
  
  // appendChild
  const ulTag = document.createElement('ul')
  const newLiTag = document.createElement('li')
  newLiTag.innerText = 'New Tag'
  ulTag.appendChild(newLiTag)  // appendChild는 타입형식을 맞춰야 하며, 1개씩만 넣을 수 있다. 추가된 Node 객체를 반환한다.
  ```

- innerText, innerHTML

  Node.innerText : Node 객체와 그 자손의 텍스트 컨텐츠를 표현

  Element.innerHTML : 요소 내 포함된 HTML 마크업을 반환. XSS 공격에 취약하므로 사용이 주의된다.

  ```javascript
  const li1 = document.createElement('li')
  const li2 = document.createElement('li')
  li1.innerText = '<strong>TEXT</strong>'
  li2.innerHTML = '<strong>TEXT</strong>'
  ulTag.append(li1, li2)
  
  // li1은 innerText로 내용을 바꿔 str형태로 저장, 반면 li2는 innerHTML을 사용해서 strong태그를 인식
  ```

- remove

  ```javascript
  const parent = document.querySelector('ul')
  const child = document.querySelector('ul > li')
  const removedChild = parent.removeChild(child)  // 부모로 접근하여 자식 삭제(출력만 사라진다)
  
  parent.append(child)  // 다시 붙이기
  ```

- setAttribute, classList

  ```javascript
  const header = document.querySelector('#location-header')
  header.setAttribute('class', 'ssafy')  // class를 ssafy로
  header.classList = ['ssafy', 'hello', 'world']  // class를 해당 값들로
  header.classList.add('new-class')  // remove, contain, replace 등도 가능하다.
  header.classList.push('new-class')
  ```

- getAttribute 해당 요소의 지정된 값을 문자열로 반환한다. 예시는 class를 불러온다.

  ```javascript
  header.getAttribute('id')
  ```






### 4. Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체를 말한다.
- 사용자의 행동으로 발생할 수도 있으며, 프로그래밍 적으로도 특정 메서드를 호출해 발생시킬 수 있다.



- addEventListener() : 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정한다.

  ```html
  // 타겟에 특정 타입의 이벤트가 생길 때 실행할 동작을 함수로 명세.
  // 함수 실행값이 아닌 함수가 들어가야 한다.
  target.addEventListener(type, listener[, options])  // 익명함수 말고 기명함수도 가능
  
  
  <h2>change my color</h2>
  <label for="change-color-input">원하는 색상을 입력하세요.</label>
  <input id="change-color-input"></input>
  
  <script>
    const colorInput = document.querySelector('#change-color-input')
    const changeColor = function (evnet) {
      const h2Tag = document.querySelector('h2')
      h2Tag.style.color = event.target.value
    }
    colorInput.addEventListener('input', changeColor)
  </script>
  ```



- preventDefault() : Event 취소. 현재 이벤트의 기본 동작을 중단한다.

  ```html
  <input typoe="checkbox" id="my-checkbox">
  <form action="/articles/" id="my-form">
    <input type="text">
    <input type="submit" value="제출">
  </form>
      
  <script>
    const checkBox = document.querySelector('#my-checkbox')
  
    checkBox.addEventListener('click', function (event) {
      event.preventDefault()
    })
  
    const formTag = document.querySelector('#my-form')
    
    formTag.addEventListener('submit', function (event) {
      event.preventDefault()
    })
  </script>
  ```

