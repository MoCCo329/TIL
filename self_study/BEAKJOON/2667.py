# def bfs(i, j, N):
#     q = []
#     q.append((i, j))
#     v[i][j] = 1
#     h = 0 # 단지에 속한 집의 수
#
#     while q:
#         i, j = q.pop(0)
#         h += 1
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
#                 q.append((ni, nj))
#                 v[ni][nj] = 1
#     return h

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
            num.append(r) # new.append(r)

num.sort()
print(cnt)
for x in num:
    print(x)