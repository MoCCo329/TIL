# Python 함수

### 1. 내장함수

- 함수는 어떤 값을 넣었을 때 특정 값이 나오는 것처럼 (사물이 지니고 있는 여러가지 측면 가운데서, 특정한 측면만을 가려내어 포착하는) 추상화 장치라고 볼 수 있다. 특정한 기능을 하는 코드 조각을 말하며, 필요시에 호출하여 간편히 사용할 수 있다.





### 2. 사용자 정의 함수



- 함수는 def 키워드로 선언하며 호출은 함수명() 으로 호출한다.



- return과 print의 차이에 주의한다. return은 프린팅 되지 않는다.







- 여러값을 리턴할 시 튜플로 묶여 하나의 튜플로 나온다. 리턴값이 없으면 None이 나온다

- parameter는 함수를 정의할 때 쓰이는 변수명, argument 는 함수를 호출할 때 넣는 값들

- argument가 여러개일 때 일반적으로 순서대로 전달된다. 변수의 이름(키워드)으로도 직접 전달할 수 있다. 하지만 키워드로 전달하는 순간 위치가 의미 없어진다. 따라서 키워드로 전달한 뒤 위치로 전달할 수 없다.(반대 순서는 가능)

- def f(x, y=0): 처럼 기본값을 지정하여 호출시 argument값을 적게 입력해도 되도록 만들 수 있다.

  여러 값을 받을 경우 parameter 앞에 *을 붙여 튜플로 받을 수 있다.

   **을 사용할 경우 dictionary로 받을 수 있다. f(a = 'apple', b = 'banana'). '='임에 주의하자. 또 key에 ''를 안쓰도록 한다.



- 함수 내부범위의 local scope와 함수 밖의 global scope로 구분한다. 따라서 함수안에서의 변수를 함수 밖에서 호출할 수 없다.
- bulit-in scope는 파이썬이 실행된 이후부터 유지, global scope는 모듈(해당 파이썬 파일)이 실행된 이후 부터 인터프리터가 끝날 때까지, local은 함수가 호출될 떄부터 함수가 종료될 떄까지 유지된다.
- 변수나 함수 명이 동일할 시 LEGB (local -> enclosed -> global -> built-in) 순서대로 불러온다. global 키워드로 함수 밖 global 변수를 함수 안에서 쓸 수 있다. nonlocal 키워드는 해당 함수 밖의 스코프(해당 함수를 포함하는 함수)에 영향을 미치지만, global에 영향을 줄 순 없다.
- 해당 스코프 안에 검색하는 변수명이 없을 경우 LEGB rule에 의해 검색을 하지만, 값을 바꿀 순 없다.



### 재귀함수

- 자기 자신을 호출하는 함수
- 1개 이상의 base case 가 존재하고 수렴하도록 작성한다.
- 메모리 스택이 넘치게 되면 stack overflow가 발생해 프로그램이 동작하지 않게 된다.
- 파이썬의 최대 재귀 깊이는 1000번 이다.
- 변수 수가 줄어들지만, 메모리를 많이 먹고 연산 속도가 오래 걸린다.



### 4. 모듈

라이브러리 > 패키지 > 모듈 



- *import* module / *from* module *import* var, function, class / *import* module *
- *from* pacage *import* module / *from* package.modult *import* var, function, class
- *import* pprint 로 불러오면 pprint.pprint()로 사용하면 되고, *from* pprint *import* pprint 로 부르면 그냥 pprint()로 사용할 수 있다.
- 패키지는 여러 모듈/ 하위 패키지를 구조화 한 것으로 모든 폴더에는 \__init__.py를 만들어 패키지로 인식시키는 것이 좋다.



### 기타

- n, m = [1, 2]로 변수 지정 시 n = \[1, 2][0], m = \[1, 2][1] 의 과정을 거쳐 저장된다.
- 상수처럼 값을 바꾸지 않을 변수명은 대문자로 쓴다.
- map(function, iterable) iterable 데이터 값들을 function에 적용하여 반환. 리스트를 주는게 아니라 값을 차래대로 꺼내주는 통(iterater)을 만든다고 생각하면 된다. 따라서 직접 볼 수 없다. filter(function, iterable)는 function 결과가 True인 것들만 반환
- zip(*iterable) 복수의 iterable 데이터들을 순서대로 모아 튜플을 원소로 하는 리스트로 묶어준다.
- 익명함수로도 불리는 lambda 함수는 return문을 가지지 않으며 lambda parameter : 표현식
- Docstring은 함수 설명을 주석으로 써놓은 것으로 함수 사용시 shift+tab으로 정보를 얻을 수 있다.
- \<venv> 는 가상환경을 포함하는 디렉토리 경로로 활성화 시키면 패키지, 모듈, 다른버전의 프로그램 등 파일들이 이곳에 설치된다. 

