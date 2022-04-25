## JavaScript 데이터 & 제어문

### 1. JavaScript란

- 브라우저를 조작할 수 있는 유일한 언어
- 브라우저에서 JavaScript Core(ECMAScript)를 이용해 DOM(Document Object Model, HTML의 문서구조), BOM(Browser Object Model, 브라우저) 조작이 가능하다.

- JS는 세미콜론을 선택적으로 사용 가능하다. 세미콜론을 적지 않아도 Automatic Semicolon Insertion에 의해 자동으로 세미콜론이 삽입된다.

- 일반적으로 Airbnb, Google JS style guide를 따라 작성한다. 또한 변수, 객체, 함수명은 camelCase로 클래스, 생성자는 PascalCase, 상수는 SNAKE_CADE로 작성한다.



### 2. 변수

- 선언(Declaration) : 변수를 생성하는 행위
- 초기화(Initializer) : 선언된 변수에 처음으로 값을 저장하는 행위
- 할당(Assignment) : 선언된 변수에 값을 저장하는 행위



- let은 재할당이 가능하지만 const는 불가능하다.

```javascript
let number = 10  // 선언 및 초기화
number = 10  // 재할당 가능

const number = 10  // 선언 및 초기화
number = 10  // 재할당 불가능(할당이 아닌 내용 조작은 가능)  => Uncaught TypeError발생
```

- let, const 는 블록 스코프(block scope)를 가진다. 즉 중괄호 내부에서 사용 가능하다.



- var는 재선언까지 가능하며, 함수 스코프(function scope)를 가진다. 하지만 Hoisting(할당 전 언급)으로 인해 예기치 못한 문제가 발생할 수 있으며 사용이 지양된다.



### 3. 데이터 타입

- 원시타입 : 객체가 아닌 기본 타입, 변수에 해당 타입의 값이 담기며, 다른 변수에 복사할 때 실제 값이 복사된다. (Primitive type : Number, String, Boolean, null, undefined 등)
- 참조타입 : 객체타입의 자료형으로 변수에 해당 객체의 참조 값이 담긴다. 다른 변수에 복사할 때 참조 값이 복사된다. (Reference type : Array, Function 등)



- Number type : 정수 실수 구분없는 하나의 숫자 타입, 부동소수점 형식을 따르며 NaN이라는 계산 불가능한 경우 반환하는 값과 무한대인 Infinity를 포함하는 타입이다.
- String type : 텍스트 데이터를 나타내는 타입이다. Template Literal은 따옴표가 아닌 backtick(``)으로 감싸야 하며, 중괄호 앞에 달러표시를 붙여야 한다.

- Undefined : 빈 값을 표현하기 위한 데이터 타입. 변수 선언 시 아무 값도 할당하지 않을때 자동으로 할당되는 값.
- Null : 빈 값을 표현하기 위한 데이터 타입. 개발자가 의도적으로 필요한 경우 할당한다.
- Boolean : 논리적 참, 거짓을 나타내는 타입. 주의할 점은 object의 경우 항상 참의 boolean 값을 가진다.



### 4. 연산자

- 할당 연산자 : 오른쪽에 있는 피연산자의 평가결과를 왼쪽 피연산자에 할당하는 연산자. ++, -- 보단 +=, -=가 권고된다.

- 비교 연산자 : 피연산자들을 비교하여 boolean의 결과값을 반환하는 연산자. 문자열도 유니코드 값을 기반으로 비교한다.

- 동등 연산자 : '=='는 두 피 연산자가 같은 값인지 암묵적 타입 변환을 통해 타입을 일치 시킨 후 비교한다. 그렇기 때문에 예상치 못한 결과를 야기할 수 있으므로 잘 사용하지 않는다.

- 일치 비교 연산자 : '==='는 타입변환 없이 비교한다. 두 피연산자가 객체일 경우 메모리의 같은 객체를 바라보는지 확인한다.
- 논리 연산자 : 파이썬에서 and 는 JS에서 &&로, or은 ||로, not은 !으로 사용한다.

- 삼항 연산자 : a ? b : c 에서 a가 참이면 b, 거짓이면 c를 반환한다.



### 5. 조건문

- if statement

```javascript
const nation = 'Korea'

if (nation === 'Korea') {
  console.log('안녕하세요!')
} else if (nation === 'France') {
  console.log('Bonjour!')
} else {
  console.log('Hello!')
}
```

- switch statement

```javascript
const nation = 'Korea'

switch(nation) {
  case 'Korea': {
    console.log('안녕하세요!')
    break  // case 통과시 break가 없으면 다른 case는 자동으로 통과해서 모두 수행한다.
  }
  case 'France': {
    console.log('Bonjour!')
    break
  }
  default: {
    console.log('Hello!')
    break
  }
}
```

- while

```javascript
while (i < 5) {
  console.log(i)
  i++
}
```

- for(for, for in, for of)

```javascript
for (let i = 0; i < 6; i++) {  // 매번 i가 6보다 작은지 확인한다.
  console.log(i)
}
```

```javascript
const capitals = {
  korea: 'seoul',
  france: 'paris',
  USA: 'washington D.C.'
}

for (let nation in capitals) {
  console.log(nation)  // 키 값이 나온다.
  console.log(`${nations}의 수도는 ${capitals[nation]}이다`)
}

// JS에서 말하는 객체는 보통 dictionary를 말한다.
```

```javascript
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {  // 객체값을 반복한다. const로 선언해도 for문이 작동하지만, 재할당 불가
  fruit = fruit + '!'
  console.log(fruit)
}
```

