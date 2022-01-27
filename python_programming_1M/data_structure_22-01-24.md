## 1. 다양한 메서드

- 메서드(method)는 s + v 로 이해하면 좋다.

- string type의 메소드

s.find(x) : x의 첫 번째 위치를 반환, 없으면 -1 반환

s.index(x) : x의 첫 번째 위치를 반환, 없으면 오류 발생

s.isalpha() : 단어(알파벳, 한글 등)인지 특수문자인지

s.isupper() : 대문자 여부

s.islower() : 소문자 여부

s.istitle() : 타이틀 형식 여부. 띄어쓰기 후 대문자 '이후 대문자

isdecimal() < isdigit() < isnumeric() 숫자 검증 메서드



문자열 변경 메소드는 문자열을 변경시키는 것이 아니라 바뀐 결과를 반환한다.(문자열은 불가변하다)

s.replace(old, new[,count]) : (count는 선택사항을 말한다 숫자를 적으면 몇개 바꿀 것인지)

s.strip([chars]) : 특정문자들을 제거 양쪽이나 왼쪽(lstrip), 오른쪽(rstrip)

s.split(sep=None, maxsplit=-1) : 문자열을 특정한 단위로 나눠 리스트로 반환

'separator'.join([iterable]) : 반복가능한 컨테이너 요소들을 separator로 합쳐 문자열 반환



- list type의 메소드

L.append(x) : 리스트 마지막에 항목 x를 추가

L.insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입

L.remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번쨰) x를 제거. 항목이 존재하지 않을 경우 ValueError

L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거

L.pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거

L.extend(m) : 순회형 m의 모든 항목들의 리스트 끝에 추가

L.index(x, start, end) : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환

L.reverse() : 리스트를 거꾸로 정렬. sort처럼 원본 자체를 정렬

L.sort() : 리스트 정렬(매개변수 이용가능)

L.count(x) : 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환

L.clear() : 값을 모두 삭제



- Tuple type의 메소드는 항목을 변경하는 메소드를 제외하고 대부분 동일하다.



- Set type의 메소드

s.copy() : 셋의 얕은 복사본을 반환

s.add(x) : 항목 x가 셋s에 없다면 추가

s.pop() : 셋s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거. set이 비어 있을 경우, KeyError

s.remove(s) : 항목 x를 셋 s에서 삭제. 항목이 존재하지 않을 경우, KeyError

s.discard(x) : 항목 x가 셋 s에 있는 경우, 항목 x를 셋s에서 삭제. 없어도 에러발생 X

s.update(t) : 셋 t에 있는 모든 항목 중  셋 s에 없는 항목을 추가

s.clear() : 모든 항목을 제거

s.isdisjoint(t) : 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환

s.issubset(t) : 셋 s가 셋 t의 하위 셋인 경우, True 반환

s.issuperser(t) : 셋 s가 셋 t의 상위 셋인 경우, True반환



- Dictionary의 메소드

d.clear() : 모든 항목을 제거

d.copy() : 딕셔너리 d의 얕은 복사본을 반환

d.keys() : 딕셔너리 d의 모든 키를 담은 뷰를 반환

d.values() : 딕셔너리 d의 모든 값을 담은 뷰를 반환

d.items() : 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환

d.get(k) : 키 k의 값을 반환하는데, 키 k가 딕셔너리에 없을 경우 None 반환

d.get(k, v) : 키 k의 값을 반환하는데, 키 k가 딕셔너리에 없을 경우 v 반환

d.pop(k) : 키 k의 값을 반환하고 항목을 딕셔너리에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 KeyError

d.pop(k, v) : 키 k의 값을 반환하고 항목을 딕셔너리에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환

d.update([other]) : 딕셔너리 d의 값을 매핑하여 업데이트



## 2. 얕은 복사와 깊은 복사

- 변수에 같은 주소가 입력되도록 하면 저장된 데이터의 값이바뀔 때 여러 변수의 값이 변한다. 하지만 변수를 선언할 때 약간의 처리를 거치게 되면 주소가 달라져 다른 저장소를 참조하게 된다.

- 복잡한 구조. 예를들면 2차 리스트의 경우 1차 리스트는 간단한 처리를 거칠 경우 주소가 달라지지만, 2차 리스트는 여전히 같은 주소를 참조한다. 이를 얕은 복사(shallow copy)라 한다.

- import copy를 하고 b = copy.deepcopy(a)를 하게되면 깊은 복사(deep copy)가 된다.



## 3. 에러

- 

branches

for loops

while loops

function

- print 함수 활용, 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용

- Syntax Error

EOL(End of Line)

EOF(End of File)

- Exception

ZeroDivisionError : 0으로 나누고자 할 때 발생

NameError : namespacae 상에 이름이 없는 경우

TypeError : 연산불가능한 타입의 종류가 있을 때 , 연산전달인자 개수나 타입이 다를때

ValueError : 타입은 올바르나 값이 적절하지 않거나 없는경우

IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우

KeyError : 해당 키가 존재하지 않는 경우

ModuleError : 존재하지 않는 모듈을 import 하는 경우

ImportError : 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

KeyboardInterrupt : 임의로 프로그램을 종료하였을 때

IndentationError : 들여쓰기가 적절하지 않는 경우







## 4. 예외 처리

```python
try:
	try 명령문
except 예외그룹-1 as 변수-1:
    예외처리 명령문 1
except 예외그룹-2 as 변수-2:
    예외처리 명령문 2
Finaly: #선택사항
    finally 명령문


```

예외없는 정상종료 : try - else - Finally

예외처리 할 경우 : try - except - Finally

예외처리 하지 못한 경우 : 오류 메시지 출력