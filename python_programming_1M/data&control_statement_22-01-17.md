# Python 데이터 & 제어문





파이썬 개발환경 파이썬 기본 IDLE, pycham, jupyter notebook, vscode

코드 스타일 가이드 PEP8 추천



- 변수(variable)

type()

id() 메모리 주소

같은 값을 동시에 할당 가능 x = y = 1004 ( x, y = 1004 는 불가)

동시에 다른 값을 할당 할 수 있다. x, y = 1, 2

두 값을 서로 바꿀 수 있다. y,  x = x, y (pythonic)



변수 이름은 알파벳, 언더스코어, 숫자로 구성

but 첫글자로 숫자 불가, 대소문자 구별, 몇 키워드는 예약어(reserved words) 예를들면 False. None, and, as, assert, form, in , not, or, pass, try, class, lambda 등등

내장함수나 모듈 등의 이름으로도 만들면 안된다.



data type - Boolean, Numeric(int, float, complex), String, None

None은 없다는 의미

bool()함수 bool(0) => False 지만, bool([0]) => True

정수는 오버플로우가 발생하지 않는다.

2진수 0b, 8진수 0o, 16진수 0x

실수는 Floating point rounding error가 일어난다. 

라운딩 에러 처리는 abs(a - b) <= 1e-10 같은 식으로 거르거나

​	import sys

​	print(abs(a - b)) <= sys.float_info.epsilon 시스템 실수 정보중 입실론보다 작은가?

​	

​	import math

​	math.isclose(a, b) # => true



문자열은 'or "로 통일하여 표기

문자열은 immutable 하다 (바꿀 수 없다)

문자열은 반복 가능하다 iterable

String interpolation

​	%-formatting - %s변수 %d정수 %f실수

​	str.format() - '{}'.format()

​	f-string - f'{}'



- 컨테이너(container)

시퀸스형 - 리스트(가변), 튜플(불변), 레인지(불변)

비시퀸스형 - 세트(가변), 딕셔너리(가변)



a = [], a = list() 로 만들 수 있다.

튜플은 순서를 가지는 불변 자료형. 소괄호로 표현 a = (1, 2, 3), a = tuple((1, 2, 3)) 을 통해 생성. 단일 항목의 경우 끝에 쉼표를 붙이면 된다.

파이썬은 동적 타이핑 언어이다.

보통은 파이썬 내부에서 처리 x, y = 1, 2 도 사실 x, y = (1, 2) 로 순서대로 넘겨주는것

범위 range(시작값:끝값:간격)



세트(Set) 중복과 순서없는 가변 자료형. 중괄호{} 혹은 set()을 통해 생성. 인덱스 접근 등 특정한 값에 접근할 수 없다.

딕셔너리(Dictionary)는 key-value로 이루어진 자료. key 는 변경 불가능한 데이터만 활용 가능(string, integer, float, boolean, tuple, range)



- 자료형 변환(Typecaasting)

암시적 형 변환 : 사용자가 의도치 않고, 파이썬 내부적으로 자료형을 변환 하는 경우

​	True + 2, 3 + 5.0

명시적 형 변환

​	str, float 를 int로

​	str, int 를 float로

​	int, float, list, tuple, dict를 str로



- 연산자

산술, 비교, 논리(단축평가 하기 떄문에 결과과 확실하면 두번째 값은 확인하지 않는다), 복합, 멤버쉽(in, not in), 식별(is), 시퀸스형(+이지만 숫자가 아닌 다른 자료형끼리 더해준다, *로 반복시킨다), 인덱싱(시퀸스의 특정 값에 접근), 기타(슬라이싱, set연산자(|합집합 &교집합 - 여집합 ^대칭자 합집합에서 교집합 뺀것))



- 제어문

  - 조건문

    순서도로 표현 가능, 4space 쓰기

    if elif else

  - 반복문

    for 문은 시퀸스를 포함한 순회가능한 객체 요소를 모두 순회한다. 별도 종료조건이 필요하지 않다
