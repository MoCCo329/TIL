## Python 데이터 & 제어문

### 1. 변수(Variable)

- a = 123에서 a를 변수라고 한다.

- type()으로 변수의 형태를, id()로 메모리 주소를 알 수 있다.

- 같은 값을 동시에 할당 가능 x = y = 1004 ( x, y = 1004 는 불가)

- 동시에 다른 값을 할당 할 수 있다. x, y = 1, 2

- 두 값을 서로 바꿀 수 있다. y,  x = x, y (pythonic)

- 변수 이름은 알파벳, 언더스코어, 숫자로 구성되지만 첫글자로 숫자 불가, 대소문자 구별, 몇 예약어(reserved words)는 변수명으로 사용 불가하다. 예를들면 False. None, and, as, assert, form, in , not, or, pass, try, class, lambda 등등 또 내장함수느 모듈 등의 이름으로도 만들지 않는것이 좋다. (Local Enclosed Global Built-in)



### 2. 데이터 형태

- Boolean, Numeric(int, float, complex), String, None의 데이터 형태가 존재한다.

- None은 없다는 의미

- bool은 True, False이다. bool()함수 bool(0) => False 지만, bool([0]) => True

- 파이썬은 오버플로우가 발생하지 않는다.
- 2진수 0b, 8진수 0o, 16진수 0x

- 실수는 Floating point rounding error가 일어난다.  라운딩 에러 처리는 abs(a - b) <= 1e-10 같은 식으로 거르거나 import sys;	print(abs(a - b)) <= sys.float_info.epsilon 시스템 실수 정보중 입실론보다 작은가 확인 가능하다. 또 import math;	math.isclose(a, b)로 True False확인 할 수 있다.

- 문자열은 ' ' or "  ''로 통일하여 표기. 문자열은 바꿀 수 없고(immutable), 반복 가능하다(iterable)

- String interpolation은 아래 세가지 방법이 있다.
  - %-formatting - %s변수 %d정수 %f실수
  - str.format() - '{}'.format()
  - f-string - f'{}'



### 3. 컨테이너(Container)

- 데이터들을 담는 컨테이너에는 다음 종류가 있다.

​	시퀸스형 - 리스트(가변), 튜플(불변), 레인지(불변)

​	비시퀸스형 - 세트(가변), 딕셔너리(가변)

- a = [], a = list()로 리스트를 만들 수 있다.

- 튜플은 순서를 가지는 불변 자료형. 소괄호로 표현 a = (1, 2, 3), a = tuple((1, 2, 3)) 을 통해 생성. 단일 항목의 경우 끝에 쉼표를 붙이면 된다. 튜플은 보통은 파이썬 내부에서 처리할 때 사용된다. x, y = 1, 2 도 사실 x, y = (1, 2) 로 순서대로 넘겨주는것

- 범위 range(시작값:끝값:간격)
- 세트(Set) 중복과 순서없는 가변 자료형. 중괄호{} 혹은 set()을 통해 생성. 인덱스 접근 등 특정한 값에 접근할 수 없다.

- 딕셔너리(Dictionary)는 key-value로 이루어진 자료. key 는 변경 불가능한 데이터만 활용 가능(string, integer, float, boolean, tuple, range)

- 자료형 변환(Typecasting)

  - 암시적 형 변환 : 사용자가 의도치 않고, 파이썬 내부적으로 자료형을 변환 하는 경우

    True + 2, 3 + 5.0

  - 명시적 형 변환

    str, float 를 int로

    str, int 를 float로

    int, float, list, tuple, dict를 str로

- 연산자

산술, 비교, 논리(단축평가 하기 떄문에 결과과 확실하면 두번째 값은 확인하지 않는다), 복합, 멤버쉽(in, not in), 식별(is), 시퀸스형(+이지만 숫자가 아닌 다른 자료형끼리 더해준다, *로 반복시킨다), 인덱싱(시퀸스의 특정 값에 접근), 기타(슬라이싱, set연산자(|합집합 &교집합 - 여집합 ^대칭자(합집합에서 교집합 뺀것)))



### 5. 제어문

- 순서도로 표현 가능, indentation(4space)과 :주의

  - 조건문

    if elif복수조건 else

  - 반복문

    - for 문은 시퀸스를 포함한 순회가능한 객체 요소를 모두 순회한다. 별도 종료조건이 필요하지 않다.
    - 딕셔너리를 순회 할 때 .keys() .values() .items() (key, value)튜플 로 쓸 수 도 있다.
    
    - dictionary comprehension 은 {i : i*3 for i in range(1,4)} 식으로 작성
    
    - enumerate 순회는 enumerate(list)로 for 반복조건을 주면 (idx, value)로 반환한다. enumerate(list, start=1)이면 idx가 1부터 value는 0부터
    
    - while 은 조건을 사용해서 반복실행한다.
    
    - 반복문 제어는 break, continue, pass로 한다.
    
      break 는 루프 종료 break를 이용하여 for else문을 만들 수 있다.
    
      continue는 이후 코드 블록을 수행하지 않고 다음 반복을 수행.
    
      pass는 특별이 할 일이 없을 떄 자리 채우는 용도.



### 6. 기타

- jupyter notebook에서 m은 markdown, y는 python코드입력, a와 b는 각각 위 아래에 칸 생성, dd는 칸 삭제,  in은 실행횟수 out은 마지막 줄을 표현해 준다.
- 코드 스타일 가이드 PEP8을 따라 같은사람이 짠 코드처럼 통일성을 갖추는게 좋다.

