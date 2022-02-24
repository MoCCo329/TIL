



### 기타

함수 내에서 배열 요소에 접근할 때에는 global로 취급(여기서 LEGB를 따르는것이 아니다), 배열 선언은 local로 취급

```python
def f1():
    a[1] = 4

def f2():
    a = [1,2,3,4,5,6]
    f3()

def f3():
    print(a)

a = [1,2,3]
print(a)
f1()
print(a)
f2()

#[1, 2, 3]
#[1, 4, 3]
#[1, 4, 3]
```

