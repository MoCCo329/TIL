## 함수 문제

### 1. abs() 직접 구현하기

내 답

```python
def my_abs(x):
    if type(x) == complex:
        return((x.real**2 + x.imag**2)**0.5)
    elif type(x) == int:
        return(int((x**2)**0.5))
    else:
        return((x**2)**0.5)
```

우수 답

```python
def my_abs(n):
    # 복소수 자료일 때, 
    if type(n) is complex:
        return (n.imag**2 + n.real**2) ** 0.5
    else:
    # 숫자형 자료일 때, 
        if n < 0:
            return -n
        elif n > 0:
            return n
        else:
            return n ** 2
```

-0.0의 경우 0.0이 나와야해서 제곱하여 다시 제곱근으로 표현했으나, 정수가 실수형으로 나타났다. 때문에 int일떄 조건을 추가해 주었으나 그럴 필요없이 부호를 + 로 바꾸고 0인경우 **2를 해주는 방법이 있었다.

켤레복소수로 복소수.real, 복소수.imag 없이도 풀 수 있을것 같다.



## 2. all() 직접 직접 구현하기

내 답

```python
def my_all(elements):

    for i in elements:
        if type(i) == type([]) and len(i) == 0:
            return False
        elif i == 0:
            return False
        
    return True
```

우수 답

```python
def my_all(elements):
    # 통의 모든 요소 => for
    is_true = True
    for element in elements:
        # 조건 : 요소가 참인지 확인 => True
        if not element:
            return False
    return is_true
```

나는 1. 빈 element 2. 빈 리스트를 원소로 갖음 3. 0을 갖는다 4. 나머지 True 의 경우로 나눠 생각했는데, if의 조건문에서 원소 자체로 True False를 구분할 수 있었다. is_true 변수로 주어진 list나 range가 비었을 때 True를 반환할 수 있었다.



## 3. 자릿수 더하기

내 답

```python
def sum_of_digit(number):
    num_str = str(number)
    
    return sum(int(i) for i in num_str)
```

우수 답

```python
def sum_of_digit(number):
    
    digits = 0
    while number > 0:
        digits += number % 10
        number = number // 10
    return digits
```

나는 파이썬식으로 접근하였고, 정석은 문제만을 보고 접근하는 것이다. 파이썬을 첫 언어로 배워서 어느방법이 정석인지 헷갈릴 수 있지만, 출제자의 의도대로 풀고, 이후에 다양한 방법을 생각해보자.



## 4. 정중앙 문자

내 답

```python
def get_middle_char(char):
    
    if len(char) % 2 == 1:
		return char[int((len(char)-1) / 2)]
    else:
    	return (char[int(len(char)/2 - 1)] + char[int(len(char)/2)])
```

우수 답

```python
def get_middle_char(n):
    if len(n) % 2:
        result = n[len(n)//2]
    else:
        result = n[len(n)//2 - 1], n[len(n)//2]
    return result
```

몫으로 조건을 만들면 int를 넣거나 1을 빼는 등 복잡하게 풀지 않아도 됐다.

여기서 q, r = divmod(len(word). 2) 를 통해 나누는 계산표현을 줄일 수도 있었고 if의 조건문에서 꼭 "== 1"을 넣지 않아도 됐다.



## 5. 2차원 List의 전체 합 구하기

내 답

```python
def all_list_sum(all_list):
    sum = 0
    for i in range(len(all_list)):
        for j in all_list[i]:
            sum += j
        
    return sum
```

i, j, k(?)는 인덱스를 나타내는 변수로 사용하자! j 가 잘못되었다.



## 6. 기타

- dir() : 해당 객체가 어떤 변수와 메소드를 가지고 있는지를 나열
- 교수님 풀이방식을 보며 배운것은 복잡하지 않게 단계단계 생각하여 코드를 완성시키고, 나중에 최적화 하면 편하다.

