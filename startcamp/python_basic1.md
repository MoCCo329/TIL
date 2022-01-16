# Python의 기본1

## 1. print문과 변수개념

```python
print(123)
print("hello")

print("hello" * 3)

greeting = "Guten Tag!!!"
print(greeting * 3)

number = "3"
print(number * 2)
=> 33
```

print 문을 이용해서 출력을 할 수 있다.

나중에 내용을 수정하는 등의 유지보수 측면에서 반복되는 것들은 변수를 통해 저장하는 것이 좋다.

이때 변수에 저장되는 형태가 int 인지 str인지에 따라 결과가 달라지거나 오류가 날 수 있다. 따옴표 사이의 것은 str로 저장되어 사칙연산이 불가하다.



## 2. 변수, 리스트, 딕셔너리

|          | 저장하는 법                             | 불러오는 법      | 출력값 |
| -------- | --------------------------------------- | ---------------- | ------ |
| 변수     | dust = 40                               | dust             | 40     |
| 리스트   | dust = [40, 50, 60]                     | dust[0]          | 40     |
| 딕셔너리 | dust = {'영등포구' : 40, '마포구' : 50} | dust['영등포구'] | 40     |

단일 변수는 상자에 값을 넣는 것이라면, 리스트는 이어진 상자들에 값을 저장하는것고, 딕셔너리는 견출지를 붙인 박스들이라 볼 수 있다.

리스트의 경우 대괄호로 저장, 대괄호의 박스번호로 불러오며, 딕셔너리의 경우 중괄호로 저장, 대괄호의 key로 value를 불러온다.



## 3. if, else, elif

python은 들여쓰기(indentaion)로 층을 나누기 때문에 중요하다.

```python
if 조건문:
	실행문
	
elif 두번째 조건문:
	실행문
	
else
	실행문
```



## 4. for과 while

```python
for i in range(10):
    반복문
    
    
while i < 10:
    반복문
```

for문은 지정한 범위(리스트)에 있는것을 하나하나 변수(보통i)에 저장하며 실행문을 반복한다.

while문은 조건이 만족하지 않을때까지 그냥 반복한다. 따라서 무한이 반복되지 않도록 장치가 필요하다. 예를 들면 i = i + 1

range(10)의 경우 리스트 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]와 같다. 0이상 지정숫자 미만의 범위를 갖는 리스트이다.



## 5. 내장함수

파이썬에는 다양한 내장함수가 존재하며, 성능도 좋다.

```python
import random

lunch_box = ["kfc". "맥도날드", "버거킹", "맘스터치"]
print(random.choice(lunch_box))

numbers = range(1, 46)
print(random.sample(numbers, 6))
```

import random 을 통해 random 모듈을 불러오고, random.choice, random.sample 을 사용한 모습.

우리는 어떤 함수가 존재하고 어떤식으로 사용할 수 있는지 모르는 경우가 많기에 [링크](https://docs.python.org/ko/3.9/tutorial/index.html)와 같은 문서나, 구글링이 중요하다.



## 기타 내용

- [링크](https://www.speedcoder.net)에서 코딩 타자속도 측정결과 words per minutes 가 31이 나왔다. 같은 반 분들에 비해 중간 혹은 낮은 속도이다 :(

- 변수이름은 코드를 검토하거나 다른사람과 공유할 때 알아보기 쉽도록 일정한 규칙성과 의미를 나타내야 좋다. 예를 들면 단일 변수의 경우 단수형으로, 리스트의 경우 복수형 명사를 사용

  개발자들이 매번 변수이름을 짓는데 가장 고민이 깊다고 한다... [링크1](https://meetup.toast.com/posts/106) [링크2](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)

- 오늘 배운 내용을 통해 파이썬 챗봇을 만들었다. 인사, 점심매뉴, 로또, 미세먼지



