## DOM 조작과 Event

### 1. DOM, BOM







- 선택(Selection)과 변경(Manipulation)으로 DOM 조작이 이루어 진다.



### 2. DOM 선택

- querySelector는 제공한 선택자와 일치하는 element 하나를 선택한다.
- querySelectorAll는 제공한 선택자와 일치하는 여러 element를 선택한다.



- getElementByID(id), getElementsByTagName(name), getElementsByClassName(names) 도 사용 가능하지만, querySelector, querySelectorAll을 사용하는 이유는 id, class, tag 를 모두 사용 가능하고 더 구체적으로 유연하게 선택 가능하기 때문이다.



```javascript
const h1 = document.querySelector('h1')  // h1 태그 선택하여 변수 h1에 담기.
const secondH2 = document.querySelector('#location-header')  // 해당 id를 선택
const liTage = document.querySelector('.ssafy-loaction')  // 해당 class를 선택

// CSS에서 id를 잘 쓰지 않았던 것은 JS에서 사용하기 위함이 크다. id는 camelCase로 네이밍한다.
```



### 2. DOM 조작



```javascript
h1.innerText = 'hello world'  // h1의 내용을 변경
```





createElement() 없던 태그 생성

append(), appendChild() 태크 붙이기

```javascript
// append
const newLiTag = document.createElement('li')
const ulTag = document.querySelector('ul')
ulTag.append(newLiTag)
newLiTage.innerText = 'New Tag'  // ul태그 안에 꼭 li태그로 넣지 않아도 append로 넣을 순 있다.

// appendChild
const ulTag = document.createElement('ul')
const newLiTag = document.createElement('li')
newLiTag.innerText = 'New Tag'
ulTag.appendChild(newLiTag)  // appendChild는 타입형식을 맞춰야 하며, 1개씩만 넣을 수 있다.
```





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



remove() 해당 요소를 삭제

```javascript
const parent = document.querySelector('ul')
const child = document.querySelector('ul > li')
const removedChild = parent.removeChild(child)  // 부모로 접근하여 자식 삭제(출력만 사라진다)
removedChild  // 실행
parent.append(child)  // 다시 붙이기
```



setAttribute('class', 'ssafy-location') : 'ssfay-location'이라는 class 추가하기. 수정도 가능하다.

classList = ['ssafy-location', 'hello', 'world'] : 해당 요소의 class를 지정. push, add로 추가도 가능하다.



getAttribute('class') : 해당 요소의 지정된 값을 문자열로 반환한다. 예시는 class를 불러온다.





### 4. Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체를 말한다.
- 사용자의 행동으로 발생할 수도 있으며, 프로그래밍 적으로도 특정 메서드를 호출해 발생시킬 수 있다.



addEventListener() : 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정한다.

```javascript
// 타겟에 특정 타입의 이벤트가 생길 때 실행할 동작을 함수로 명세. 함수 실행값이 아닌 함수가 들어가야 한다.
target.addEventListener(type, listener[, options])  // 익명함수 말고 기명함수도 가능
```



- preventDefault() : Event 취소. 현재 이벤트의 기본 동작을 중단한다.

  check box의 경우 클릭이 
