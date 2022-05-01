## 함수, 문자열, 객체

### 1. JS, JS 함수의 특징

- 객체 타입 중 하나로 function 타입을 갖는다.
- 함수는 일급 객체(First-class citizen)이다. 즉 변수에 할당할 수 있고, 다른 함수를 인자로 받을 수 있으며, 결과값으로 리턴될 수 있다.
- 매개변수와 인자의 개수 불일치를 허용한다. 매개변수보다 인자 수가 많을 경우 남는 인자들은 무시되며, 적을 경우 undefined로 적용된다.
- 기본인자는 python과 마찬가지로 인자 작성 시 '='과 함께 기본값을 지정하면 된다.
- Rest parameter(...)를 사용하면 python의 *args 처럼 여러 개수의 매개변수를 배열로 받는다.
- Spread operator(...)는 배열 인자를 전개하여 전달하는 표현이다.



### 2. 함수 정의

- 함수 선언식(function statement, declaration) : 함수이름, 매개변수, body로 구성된다. 익명함수가 불가능하며 호이스팅이 가능하다.

```javascript
function add(num1, num2) {
    return num1 + num2
}
```

- 함수 표현식function expression) : 함수를 표현식(하나의 값으로 결정되는 코드의 단위) 내에서 정의하는 방식. 함수 이름을 생략하여 익명함수로 정의할 수 있다. (함수이름), 매개변수, body로 구성된다. 호이스팅이 불가하며 변수의 scope를 따른다. var로 변수를 선언했다면 호이스팅이 되지만, function이 아닌 undefind로 정의되어 type에러가 발생한다.

```javascript
const add = function (num1, num2) {
    return num1 + num2
}

```

- 화살표 함수(Arrow Function) : function 키워드를 생략 가능하며, 매개변수가 하나라면 ()도 생략가능, 몸통 표현식이 return한줄이라면 {} 과 return 도 생략 가능하다.

```javascript
const arrow = (name) => { return `hello, ${name}` }
const arrow = name => `hello, ${name}`
```



- IIFE(Immediately Invokable Function Expression) : 함수를 정의와 함께 바로 실행하는 함수 표현식이다.

```javascript
(function() {
    satements
})();
```



### 3. 문자열(String)

- 문자열의 주요 메서드는 다음과 같다.

string.includes(value) : 문자열 안에 특정 문자열(value)의 존재 여부를 참/거짓으로 반환한다.

string.split(value) : value가 없을 경우 기존 문자열을 배열에 담기만 하며, value가 빈 문자열('')일 경우 각 문자를 모두 나눠 배열로 반환한다. 다른 문자열일 경우 해당 문자열로 나눈 배열을 반환한다.

string.replace(from, to) : 문자열 안의 from을 to로 1개만 교체하여 반환한다. replaceAll은 모두 교체한다.

string.trim() : 문자열 시작과 끝의 공백문자(스페이스, 탭, 엔터)를 제거한 문자열을 반환한다. trimStart는 문자열 시작의 공백문자를, trimEnd는 끝의 공백문자를 제거한다.

- 파이썬과 같은 경우에 iterable한 객체들이 많아 join함수가 각 객체들에서 정의돼야 하기에 문자열의 메서드로 사용되었다. JS에서는 join이 배열의 메서드로 존재한다.



### 4. 배열(Arrays)

- 배열은 객체(object)타입이며 키와 속성을 담고 있다. 순서를 보장하며 인덱스로 접근 가능하다. 음의 정수는 접근 불가하기 때문에 array[array.length - 1] 과 같은 방식을 사용해야 한다.
- 배열의 주요 메서드는 다음과 같다.

arr.push(value) : 배열의 가장 뒤에 요소를 추가한다.

arr.pop() : 배열의 마지막 요소를 제거한다.

arr.unshift(value) : 배열의 가장 앞에 요소를 추가한다.

arr.shift() : 배열의 첫번째 요소를 제거한다.

arr.include(value) : 배열에 특정 값(value)가 있는지 확인하여 참/거짓으로 반환한다.

arr.indexOf(value) : 배열의 특정값이 어느 인덱스를 가지는지 반환한다. 값이 없으면 -1을 반환한다.

arr.join(separator) : 배열의 요소를 연결하여 문자열로 반환한다. separator가 없으면 콤마가 들어간 문자열로 반환한다.

- Array Helper Method는 배열을 순회하며 특정 로직을 수행하는 메서드로 메서드 호출 시 인자로 callback 함수를 받는 것이 특징이다. (callback 함수는 함수 내부에서 실행될 목적으로 인자로 넘겨받는 함수를 말한다.)

forEach : 배열의 각 요소에 대해 콜백함수를 실행하며 반환값이 없다.

```javascript
arr.forEach(callback(element[, index[, array]]))
```

map : 콜백함수를 한번씩 실행하며 콜백함수의 반환값을 모아 새로운 배열을 반환한다.

```javascript
arr.map(callback(element[, index[, array]]))
```

filter : 콜백함수의 반환값이 참인 요소들만 모아 새로운 배열을 반환한다.

```javascript
arr.filter(callback(element[, index[, array]]))
```

reduce : 콜백함수의 반환 값들을 하나의 값(acc)에 누적 후 반환한다.

```javascript
arr.reduce(callback(acc, element, [index[, array]]) [, initialValue])
```

find : 반환값이 참인 첫 요소를 반환한다. 찾는 값이 없으면 undefined를 반환한다.

```javascript
arr.fin(callback(element[, index[, array]]))
```

some : 배열 요소 중 하나라도 주어진 판별함수를 통과하면 참을 반환한다.

```javascript
arr.some(callback(element[, index[, array]]))
```

every : 배열의 모든 요소가 판별함수를 통과해야 참을 반환한다.

```javascript
arr.every(callback(element[, index[, array]]))
```



### 5. 객체(Objects)

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현한다. key는 문자열 타입만 가능하며(띄어쓰기가 없으면 따옴표 생략 가능), value는 모든 타입이 가능하다. 객체 요소에 대한 접근은 점이나 대괄호로 가능하다(key이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능하다).

- 메서드는 객체의 속성이 참조하는 함수로 객체.메서드명() 으로 호출 가능하다. 메서드 선언시 function 키워드를 생략 가능하며, 매서드 내부에서는 this 키워드가 객체를 의미한다.

```javascript
const obj = {
    greeting() {
        console.log(`Hi`)
    }
}
```

- key와 value의 이름이 같으면 축약 가능하다

```javascript
const books = ['a', 'b']
const magazines = ['c', 'd']

const bookShop = {
    books,
    magazines,
}
```

- 객체를 정의할 때 key의 이름을 표현식을 이용해서 동적으로 생성 가능하다.

```javascript
const key = 'regions'
const value = ['광주', '대전', '구미', '서울']
const ssafy = {
    [key]: value,  // key가 아닌 regions로 value를 호출하게 된다.
}
```

- 구조분해할당은 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법 구조이다.

```javascript
const name = userInformation.name
const {name} = userInformation
```

- JSON은 key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포멧이다. 문자열 타입으로 JS에서 JSON을 조작하기 위한 내장 메서드를 제공한다.

  JSON.parse() : JSON을 JS객체로 변환한다.

  JSON.stringify() : JS객체를 JSON으로 변환한다.

- 배열도 객체(object)이다. 키를 인덱스로하며 length또한 속성으로 갖는다.