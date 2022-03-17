## Queue 문제

### 1. 토마토

```python
def bfs(N, M):
    visited = [[0]*M for _ in range(N)]
    q = [0] * (M*N)
    front = -1
    rear = -1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                rear += 1
                q[rear] = (i, j)
                # q.append((i, j))
                visited[i][j] = 1
            elif tomato[i][j] == 0:
                cnt += 1
    if cnt == 0 # and len(q)>0:
        return 0

    # 토마토 숙성 진행
    while rear != front:
        front += 1
        i, j = q[front]
        # i, j = q.pop(0)
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and tomato[ni][nj]==0 and visited[ni][nj]==0:
                rear += 1
                q[rear] = (ni, nj)
                # q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    # 걸린 날짜 찾기
    maxV = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                if visited[i][j] == 0:
                    return -1
                else:
                    if maxV < visited[i][j]-1:
                        maxV = visited[i][j]-1
    return maxV

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(bfs(N, M))
```

큐 사용시 pop, append 뿐 아니라 인덱스로 조종, enQ함수 deQ함수 생성 등의 방법도 자유자재로 다뤄야 한다.



### 2. 단지번호붙이기

```python
def bfs(i, j, N):
    q = []
    q.append((i, j))
    v[i][j] = 1
    h = 0 # 단지에 속한 집의 수

    while q:
        i, j = q.pop(0)
        h += 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = 1
    return h

def dfs(i, j, N):
    v[i][j] = 1
    h = 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
            h += dfs(ni, nj, N)
    return h

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

cnt = 0 # 단지 수
num = [] # 단지에 속한 집의 수
v = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            cnt += 1
            r = dfs(i, j, N) # r = bfs(i, j, N)
            num.append(r)

num.sort()
print(cnt)
for x in num:
    print(x)
```

재귀 상황에서 return값을 이용해서 값들을 계속 사용할 수 있으며, global을 이용할 수도 있다.
