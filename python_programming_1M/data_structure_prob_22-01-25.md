## 데이터 구조 및 활용 문제

### 1. 혈액형 분류하기

내 답

```python
def count_blood(blood_types):
    result = {}
    
    for blood_type in blood_types:
        result[blood_type] = blood_types.count(blood_type)
        
    return result
```

우수 답

```python
result = {}
# blood_type : 'A', 'O', ... 
for blood_type in blood_types:
    # 딕셔너리에 키가 있으면
    if blood_type in result:
        result[blood_type] += 1
    # 딕셔너리에 키가 없으면:
    else:
        result[blood_type] = 1

result = {}
# blood_type : 'A', 'O', ... 
for blood_type in blood_types:
    result[blood_type] = result.get(blood_type, 0) + 1
```

만든 사전에 혈액형을 대조하여 항목이 있으면 값에 +1 없으면 항목을 추가하는 방식이다. .get으로 항목의 value를 불러오고 없으면 0으로 부를 경우 코드가 깔끔해 진다.



### 2. 정사각형만 만들기

내 답

```python
def only_square_area(lengths, widths):
    square_area_set = set()    
    for length in lengths:
        for width in widths:
            if length == width:
                square_area_set.add(length*width)
                
    return square_area_set
```

우수 답

```python
def only_square_area(list1, list2):
    square_list = []
    for num in list1:
        if num in list2:
            square_list.append(num ** 2)
    return square_list

def only_square_area(a, b):
    c = list(set(a) & set(b))
    for i in range(len(c)):
        c[i] *= c[i]
    return c
```

중복을 줄이려고 집합을 사용했는데, 다시 생각해보니 정사각형이라 중복 될 일이 없었다. 교집합을 이용하는 것이 인상 깊었다.



### 3. 무엇이 중복일까

내 답

```python
def duplicated_letters(word):
    duplicated_words = [char for char in word]
    duplicated_chars = set()
    
    for i in range(len(duplicated_words)):
        temp = duplicated_words[-1]
        duplicated_words.pop()
        if temp in duplicated_words:
            duplicated_chars.add(temp)
            
    return duplicated_chars
```

우수 답

```python
result = []
# word : 'apple'
# char : 'a', 'p', ...
for char in word:
    # 만약에 여러번 등장했다면, 
    # 그리고 char가 result 통에 없다면, (조건 추가)
    if word.count(char) > 1 and char not in result:
        result.append(char)

print(result)
```

순서대로 나와야 한다는 명시가 없으므로 집합을 사용하거나 두 조건으로 char를 append할 수 도 있다.



### 4. 솔로 천국 만들기

내 답

```python
def lonely(numbers):
    new_numbers = []
    
    while len(numbers) > 1:
        temp = numbers.pop(0)
        
        if temp == numbers[0]:
            continue
        else:
            new_numbers.append(temp)
            
    new_numbers.append(numbers[0])
            
    return new_numbers
```

우수 답

```python
def lonely(num_list):
    solo = [num_list[0]]
    for i in range(1, len(num_list)):
        if num_list[i] != num_list[i-1]:
            solo.append(num_list[i])
    return solo
```

edge case를 잘 생각한 예로 복잡하게 할 필요없이 len(numbers) - 1 만큼의 길이를 순환시키면 됐었다.



### 5. 기타

간단한 알고리즘문제라도 계산반복이 제곱이나 팩토리얼 등 중복되지 않고 O(1)만큼만 계산되도록 풀어보자.

sort()없이 중앙값문제를 풀어보려다가 1시간을 날렸다.