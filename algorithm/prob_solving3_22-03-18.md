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



### 2. 정사각형 방

내 답

```python
def f(i, j):
    global ans, cnt
    origin = [i, j]
    while True:
        cnt += 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[i][j] == 1:
                i, j = ni, nj
                break
        else:
            if cnt > ans[0]:
                ans[0] = cnt
                ans[1] = [origin[0], origin[1]]
            elif cnt == ans[0]:
                if arr[ans[1][0]][ans[1][1]] > arr[origin[0]][origin[1]]:
                    ans[1] = [origin[0], origin[1]]
            cnt = 0
            return
                 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [0, []]
    cnt = 0
 
    for i in range(N):
        for j in range(N):
            f(i, j)
             
    print(f'#{tc} {arr[ans[1][0]][ans[1][1]]} {ans[0]}')

```

우수 답

```python
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*(N*N+1)
     
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j+ dj[k]
                if 0<=ni<N and 0<=nj<N and arr[i][j]+1 == arr[ni][nj]:
                    check[arr[i][j]] = 1
                    break
     
    num = max_cnt = cnt = 1
    for i in range(N*N+1):
        if check[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                num = i-cnt+1
            cnt = 1
             
    print(f'#{tc} {num} {max_cnt}'
```

DFS로 모든 경우를 확인하는 것이 아니라 정사각형 안의 숫자가 겹치지 않는다는 점을 이용해 각 숫자 옆에 이어지는 숫자가 있는지를 확인하고, 최대 이어지는 수를 세는것이 시간복잡도를 줄이면서 제일 좋은 접근이였다.



### 3. 세제곱근을 찾아라

모범 답

```python
def f(N):
    s = 0
    e = 1000000
    while s <= e:
        m = (s + e) // 2
        if arr[m] == N:  # 찾음
            return m
        elif arr[m] < N:
            s = m+1
        else:
            e = m-1
    return -1
 
T = int(input())
arr = [x*x*x for x in range(1000001)]
for tc in range(1, T+1):
    N = int(input())
 
    print(f'#{tc} {f(N)}')
```

파이썬에서만 풀리는 풀이가 아닌 범용적인 답안을 찾아야 한다. 전체 세제곱 리스트를 만들고 이진탐색으로 해를 찾을 수도 있다.
