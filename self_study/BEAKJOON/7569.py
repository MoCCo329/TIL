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

    if cnt == 0 and len(q)>0:
        return 0

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