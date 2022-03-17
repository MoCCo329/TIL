## 문제풀이3

### 1. 가능한 시험 점수

내 답

```python
def f(i, N, s):
    global scores
    scores += [s]
    if i == N:
        return
    else:
        f(i+1, N, s+arr[i])
        f(i+1, N, s)
        
def f(N):
    global scores
    for i in range(1<<N):
        temp = 0
        for j in range(N):
            if i & (1<<j):
                temp += arr[j]
        scores += [temp]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    scores = []
    f(0, N, 0)
    # f(N)
 
    print(f'#{tc} {len(set(scores))}')
```

우수 답

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    v = [1] + [0] * (sum(arr))
    ans = [0]
 
    for score in arr:
        for i in range(len(ans)):
            temp = ans[i] + score
            if v[temp] == 0:
                ans += [temp]
                v[temp] = 1
 
    print(f'#{tc} {len(ans)}')
```

나는 N개를 원소로 하는 부분집합을 구하기 위해 2^N이 걸리는 방식을 사용하였다. 결과는 당연히 시간초과가 나왔다. 시간 초과를 피하는 방법으로는 N^2가 걸리도록 점수들을 이미 저장된 시험점수들에 더하며 순회하는 것이다. 또한 이미 있는 점수인지 v리스트를 이용해 제외하거나 set()으로의 변환을 통해 중복을 제거할 수 있다.



### 정사각형 방

내 답

```python
```

