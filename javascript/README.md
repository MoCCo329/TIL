| 파일명             | 링크                             |
| ------------------ | -------------------------------- |
| 1. 자료형          | [링크1](./1. 자료형.md)          |
| 2. 제어문          | [링크2](./2. 제어문.md)          |
| 3. 비동기 처리     | [링크3](./3. 비동기 처리.md)     |
| 4. DOM조작과 Event | [링크4](./4. DOM조작과 Event.md) |





### cf or Not Classified Yet

- NaN == NaN 은 false이다. isNaN(x) 만으로 알 수 있다. 

- 객체 분해 할당 시 이름 비꾸기 { name: username }

- 생성자 함수:

  - ```javascript
    function User(name, age) {
        // this = {}
        
        this.name = name
        this.age = age
        
        // return this
    }
    ```

    new User처럼 new를 붙여 실행 할 때 주석부분이 있는 것 처럼 작동한다.

- setTimeout(f, 1000, f의 인자), clearTimeout(), setInterval()

- prototype chain

- constructor.prototype 을 한번에 정의할 때 constructor가 덮어져 사라지지 않도록 주의한다.

- 클래스 메소드는 property로 들어간다.

- 클래스와 생성자함수의 차이. for in 시 클래스 메소드는 보이지 않는다. 클래스는 new 없이 쓸 수 없다. constructor에 class라고 명시가 된다.

- 클래스 상속은 extend 키워드를 사용한다.

- generator 는 function* 으로 정의된 함수 내부의 yield 로 만든다. next(), return(), throw() 메소드를 가지며 throw()는 에러를 일으키며 종료되게 한다. yield* iterable객체 는 객체의 모든 값들을 generator 화 한다.

  const a = yield "메시지" 처럼 yield 를 통해 값을 순차적으로 받을 수 도 있다.

  iterable 한 객체는 Symbol.iterator 라는 메소드를 가지며 이는 generator를 반환한다. 따라서 generator1[Symbol.iterator\](\) === generator1 은 true를 반환한다.
