## 분할정복과 백트래킹 문제

### 1. 전기버스2

배터리를 충전소의 값만큼 충전하는것이 아닌 교체하는 것이였다. 무턱대고 문제풀이를 시작하지 말고, 문제부터 잘 읽어서 시간낭비를 줄이자.



### 2. 보급로

DFS로 할 지 BFS로 할 지 확실히 생각해 보고 접근하자. 처음에 BFS로 구현했을때 DFS로 바꾸지 않고 조금만 디버깅했으면 바로 맞췄을 문제인데, 알고리즘 선택과 안틀리고 구현하는 능력이 둘 다 부족했다.



### 3. 벌꿀채취

내 답

```python
def f(k, M, C, p):
    global ans, temp_ans
 
    if k == 2:
        if ans < p:
            ans = p
        return
    else:
        for i in range(N):
            for j in range(N-M+1):
                if sum(v[i][j:j+M]) == 0:
                    for l in range(M):
                        v[i][j+l] = 1
                    temp = arr[i][j:j+M]
                    if sum(temp) > C:
                        temp_ans = 0
                        ff(0, M, C, [], temp[:])
                    else:
                        temp_ans = sum([l**2 for l in temp])
                    f(k+1, M, C, p + temp_ans)
                    for l in range(M):
                        v[i][j+l] = 0
 
 
def ff(i, M, C, s, temp):
    global temp_ans
 
    if i == M:
        if sum(s) <= C:
            a = sum([j**2 for j in s])
            if a > temp_ans:
                temp_ans = a
            return
    elif sum(s) > C:
        return
    else:
        ff(i+1, M, C, s[:] + [temp[i]], temp[:])
        ff(i+1, M, C, s[:], temp[:])
 
 
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    ans = 0
    temp_ans = 0
    f(0, M, C, 0)
    print(f'#{tc} {ans}')
```

우수 답

```python
def dfs(level, cnt, temp_total, temp_lst):
    global total
    if cnt > C:
        return
      
    if level == M:
        if cnt <= C and temp_total > total:
            total = temp_total
        return
  
    dfs(level + 1, cnt + temp_lst[level], temp_total + temp_lst[level] ** 2, temp_lst)  # 포함하는 경우
    dfs(level + 1, cnt, temp_total, temp_lst) # 포함하지 않는 경우
  
T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split()) # 벌통 크기, 선택 벌통 개수, 꿀 채취 최대 양
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
      
    memo = [[0] * N for _ in range(N)] # 해당 위치에서의 값을 미리 구해서 저장, 그때마다 구할 필요 없이 탐색만 하면 됨
    for i in range(N):
        for j in range(N - M + 1):
            total = 0
            dfs(0, 0, 0, lst[i][j:j + M])
            memo[i][j] = total
  
    for i1 in range(0, N): # 일꾼 1의 행
        for j1 in range(0, N - M + 1): # 일꾼 1의 열
            for i2 in range(i1, N): # 일꾼 2의 행
                sj = 0
                if i1 == i2: # 일꾼 1과 2가 같은 행에 있다면 일꾼 1 이후부터 탐색
                    sj = j1 + M
                for j2 in range(sj, N - M + 1): # 일꾼 2의 열
                    max_v = max(max_v, memo[i1][j1] + memo[i2][j2])
  
    print(f'#{t} {max_v}')
```

나는 두 단계의 최댓값 찾기 과정을 진행하며 둘 다 모든 배열을 계산했지만, 처음 최댓값을 찾을 때 값을 저장해 놓았다면 두번째 단계에서 겹치지만 않게 해준다면 더 빠르게 찾을 수 있었을 것이다.

