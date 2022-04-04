## 완전탐색과 그리디 문제

### 1. 최소합

내 답

```python
def f(i, j, N, ans):
    global minV
    if i == N-1 and j == N-1:
        ans += arr[i][j]
        if minV > ans:
            minV = ans
        return
    else:
        if i >= N or j >= N:
            return
        else:
            ans += arr[i][j]
        if i < N-1:
            f(i+1, j, N, ans)
        if j < N-1:
            f(i, j+1, N, ans)
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = sum(arr[0] + arr[1:N][-1])
    f(0, 0, N, 0)
    print(f'#{tc} {minV}')
```

우수 답

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = arr[0][0]
    for i in range(0, N):
        for j in range(0, N):
            if i == 0 and 0 <= j-1 < N:
                dp[i][j] = arr[i][j] + dp[i][j-1]
            elif j == 0 and 0 <= i-1 < N:
                dp[i][j] = arr[i][j] + dp[i-1][j]
            elif 0 <= j-1 < N and 0 <= i-1 < N:
                dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])
 
    print(f'#{tc} {dp[N-1][N-1]}')
```

물론 교수님께서 재귀로 푸는게 목적이라 말씀하시긴 했지만, DP로 푸는 방법도 떠올리긴 했어야 됐다.



### 2. 컨테이너 운반

내 답

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    v = [0] * N
    ans = 0
 
    for tt in t:
        idx = -1
        for i in range(N):
            if tt - w[i] >= 0 and v[i] == 0:
                if idx == -1:
                    idx = i
                else:
                    if w[idx] < w[i]:
                        idx = i
 
        if idx != -1:
            ans += w[idx]
            v[idx] = 1
 
    print(f'#{tc} {ans}')
```

우수 답

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cont = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    res = i = 0
 
    for t in truck:
        while i < N and t < cont[i]:
            i += 1
        if i == N:
            break
        res += cont[i]
        i += 1
    print(f'#{tc} {res}')
```

정렬할 생각을 왜 안했지?



### 3. 화물 도크

내 답

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    schedule.sort(key = lambda x: (x[1] - x[0], x[0]))
    v = [0] * 24
    cnt = 0
 
    for i in range(N):
        if not 1 in v[schedule[i][0]:schedule[i][1]]:
            for j in range(schedule[i][0], schedule[i][1]):
                v[j] = 1
            cnt += 1
 
    print(f'#{tc} {cnt}')
```

모범 답

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 1  # 첫번째 활동은 무조건 선택
    j = 0
    for i in range(1, N):
        if arr[i][0] >= arr[j][1]:
            cnt += 1
            j = i
    print(f'#{tc} {cnt}')
```

나는 작업들을 걸리는 시간순으로 나열하고 겹치지 않게 채워 넣느라 v리스트를 사용했다. 하지만 끝나는 시간 기준으로 한번의 정렬만 하면 조건에 맞게 답을 구할 수 있었다.



### 4. 베이비진 게임

내 답

```python
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
 
    tr = [1, 1]
    ru = [1, 1]
    ans = 0
    for i in range(3, 7):
        A = sorted(arr[0:i*2:2])
        B = sorted(arr[1:i*2:2])
 
        for j in range(1, i):
            if A[j] - A[j-1] == 1:
                tr[0] += 1
            elif A[j - 1] == A[j]:
                ru[0] += 1
            else:
                tr[0] = 1
                ru[0] = 1
            if tr[0] == 3 or ru[0] == 3:
                ans = 1
                break
 
            if B[j] - B[j - 1] == 1:
                tr[1] += 1
            elif B[j - 1] == B[j]:
                ru[1] += 1
            else:
                tr[1] = 1
                ru[1] = 1
            if tr[1] == 3 or ru[1] == 3:
                ans = 2
                break
 
        if ans:
            break
    print(f'#{tc} {ans}')
```

우수 답

```python
def bg(l):
    global state
    for j in range(10):
        if l[j] == 3:
            state = 1
            return
        if l[j] and l[j+1] and l[j+2]:
            state = 1
            return
 
T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = [0]*12
    p2 = [0]*12
    state = 0
    for i in range(12):
        if i%2:
            p2[cards[i]] += 1
            bg(p2)
            if state:
                print(f'#{tc} 2')
                break
        else:
            p1[cards[i]] += 1
            bg(p1)
            if state:
                print(f'#{tc} 1')
                break
    else:
        print(f'#{tc} 0')
```

카운트 정렬처럼 배열을 만들어 triplelet과 run을 확인하는 방법이 가장 간결했다. 또 플레이어1, 2 에게 동시에 카드가 나눠지는 줄 알았는데 순서대로 한장씩 나눠 갖는 것이였다. 문제를 잘 읽자. 그리고 베이비 진은 학기초에 배웠던 것인데 왜 카운트 배열을 생각 못했을까... 카운트 배열사용이 자료구조는 아니지만 문제에 접근할 때 어느 자료구조를 활용 할 지  생각해봤다면 카운트 배열이 떠올랐을 것 같다.
