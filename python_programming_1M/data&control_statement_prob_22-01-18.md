## 데이터&제어문 응용

### 1. 최댓값 구하기

내 답

```python
numbers = [7, 10, 22, 4, 3, 17]

max_temp = 0

for i in numbers:
    if max_temp < i:
        max_temp = i
        
print(max_temp)
```

우수 답

```python
numbers = [7, 10, 22, 4, 3, 17]

max = numbers[0]
for i in range(1, len(numbers)):
    if max < numbers[i]:
        max = numbers [i]
print(max)
```

주어진 리스트가 모두 양수인 것을 보고 0을 초기 최대값으로 잡았지만, 그래선 안되며 항상 모든상황을 고려하여 문제를 풀어야 한다는 점을 느꼈다.

또 1로 시작하는 range를 통해 0의 경우를 예외시키는 섬세함이 돋보였다.



### 2. 최댓값과 등장 횟수 구하기

내 답

```python
numbers = [7, 10, 22, 7, 22, 22]

max_temp = numbers[0]

for i in range(1, len(numbers)):
    if max_temp < numbers[i]:
        max_temp = numbers[i]
        
print(max_temp)


count = 0

for i in numbers:
    if max_temp == i:
        count += 1
        
print(count)
```

우수 답

```python
numbers = [7, 10, 22, 7, 22, 22]
        
max_num = numbers[0]
max_cnt = 0

for num in numbers:
    if num > max_num:
        max_num = num
        max_cnt = 0    
    if num == max_num:
        max_cnt += 1

    
print(max_num, max_cnt)
```

2O와 O, 한번에 카운팅까지 할 수 있었다.



### 3. 5의 개수 구하기

우수 답

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

numbers_cnt = [i for i in numbers if i == 5]

print(len(numbers_cnt))
```

comprehension 구문을 써서 깔끔히 표현해야겠다는 생각이 들었다.



### 4. 'a'가 싫어

내  답

```python
word = input()

wo_a = []

for i in word:
    if i != "a":
        wo_a.append(i)
        
for i in wo_a:
    print(i, end="")
```

우수 답

```python
word = input()

for char in word:
    if char == 'a':
        continue
    print(char, end='')
```

if 에서 continue와 break를 잘 사용해야겠다.

문자열도 + 가 된다.

다른 문제를 풀며 느낀점도 많지만 대부분 중복되거나, 모르는 함수를 쓰는 내용이였다.



### 5. 기타

- 변수명 i나 idx는 주로 range 에서, 실제 값을 나타내면 그 의미를 알 수 있도록 변수명을 짓자
- str로 이루어진 리스트를 "사이글자".join으로 한 문자열로 만들 수 있다
- list2 = list1.sort() 하면 None이 저장된다. List.sort()는 List를 정렬시키는 것. .sort(reverse=True)로 내림차순 가능, list2 = sorted(list1)로 list1의 변화없이 다른 변수에 저장 가능
- 이외에 01-17, 01-18 과제를 풀었다.