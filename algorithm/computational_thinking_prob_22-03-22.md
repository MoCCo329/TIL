## Computational Thinking 문제, 문제풀이4 문제

### 1. 재미있는 오셀로 게임

마지막에 보드에 남아있는 W, B 개수를 구하는 과정에서 보드가 가득 차있을거라 가정하고 W = N^2 - B라 하였지만 여기서 문제가 있었다. 시간을 줄이는 것은 이런부분이 아니니까 넘겨짚지 말자.



### 2. 미생물 격리

내 답

```python
def turn():  # K 는 g_list의 길이
    global g_list
    L = len(g_list)
 
    # 모든 군집을 이동시키기
    for idx in range(L):
        i, j, c, d_idx = g_list[idx]
        di, dj = d_list[d_idx]
        i, j = i + di, j + dj
 
        if 0 < i < N-1 and 0 < j < N-1:  # 경계가 아닌 경우 이동만 한다.
            g_list[idx][0] = i
            g_list[idx][1] = j
 
        else:  # 경계인 경우 이동하고, 절반으로 줄어들고, 방향이 바뀐다.
            if d_idx % 2 == 0:
                d_idx -= 1
            else:
                d_idx += 1
            g_list[idx] = [i, j, c//2, d_idx]
 
    # 만나는게 있는경우
    cnt = 0
    i = 0
    while i < L-1 - cnt:
        sumK = g_list[i][2]
        j = i+1
        while j < L - cnt:
            if g_list[i][0] == g_list[j][0] and g_list[i][1] == g_list[j][1]:
                sumK += g_list[j][2]
                if g_list[i][2] < g_list[j][2]:
                    g_list[i][3] = g_list[j][3]
                    g_list[i][2] = g_list[j][2]
                g_list.pop(j)  # 뒤에것은 없앤다
                cnt += 1
            else:
                j += 1
        g_list[i][2] = sumK  # 앞에것의 미생물 수를 sumK로
        i += 1
 
d_list = [0, [-1, 0], [1, 0], [0, -1], [0, 1]]  # 1상 2하 3좌 4우
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    g_list = []
    for _ in range(K):
        g_list += [list(map(int, input().split()))]
 
    for _ in range(M):
        turn()
 
    cnt = 0
    for group in g_list:
        cnt += group[2]
 
    print(f'#{tc} {cnt}')
```

모범 답

```python
T = int(input())
di,dj = (0,-1,1,0,0),(0,0,0,-1,1)
opp = [0,2,1,4,3]
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]
    for _ in range(M):
        # [1] 각각의 미생물 이동 후 경계처리
        for i in range(len(arr)):
            arr[i][0] = arr[i][0]+di[arr[i][3]]
            arr[i][1] = arr[i][1]+dj[arr[i][3]]
            if arr[i][0]==0 or arr[i][0]==N-1 or arr[i][1]==0 or arr[i][1]==N-1:
                arr[i][2]//=2
                arr[i][3] = opp[arr[i][3]]
 
        # [2] 정렬(좌표, 개수) 내림차순
        arr.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)
 
        # [3] 같은 좌표인 경우, 큰 미생물로 합치기
        i = 1
        while i<len(arr):
            if arr[i-1][0]==arr[i][0] and arr[i-1][1]==arr[i][1]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i+=1
 
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][2]
 
    print(f'#{test_case} {ans}')
```

군집들이 만났을 때 어떻게 처리할 지가 어려웠는데, sort를 해서 처리할 수 있었다. sort에서 key를 lambda로 설정하는 방법을 알면 유용하다.



### 3. 디저트 카페

```python
d_list = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
 
def find(i, j, d, s):
    global ans
    # 도착한 경우
    if d == 3 and (i, j) == origin:
        ans += [len(s)]
        return
 
    # 도착 안한경우
    if arr[i][j] in s:
        return
    else:
        s += [arr[i][j]]
        ni, nj = i + d_list[d][0], j + d_list[d][1]
        if 0 <= ni < N and 0 <= nj < N:
            find(ni, nj, d, s[:])
        if d < 3:
            ni, nj = i + d_list[d+1][0], j + d_list[d+1][1]
            if 0 <= ni < N and 0 <= nj < N:
                find(ni, nj, d + 1, s[:])
        return
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
 
    for i in range(N-2):
        for j in range(1, N-1):
            s = []
            origin = (i, j)
            find(i, j, 0, s)
 
    if ans:
        print(f'#{tc} {max(ans)}')
    else:
        print(f'#{tc} -1')
```

모범 답

```python
def DFS(n, ci, cj, v):
    global si, sj, ans
    if n==2 and ans>=len(v)*2:
        return
    if n>3: # 종료조건
        return
    if ci==si and cj==sj and n==3 and ans<len(v):  # 정답 갱신
        ans = len(v)
        return
 
    for k in range(n, n+2):
        ni,nj = ci+di[k], cj+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k, ni, nj, v)
            v.pop()
 
di,dj = (1,1,-1,-1,1),(-1,1,1,-1,-1)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(0, N-2):
        for sj in range(1,N-1):
            DFS(0, si, sj, [])
    print(f'#{test_case} {ans}')
```

함수의 argument, parameter로 리스트를 사용할 때, shallow copy에 주의해야 한다. 이것때문에 디버깅을 못해서 시간을 매우 많이 날렸다. 이를 막기 위해선 slicing을 하여 새로운 리스트를 넘겨주거나 모범 답 처럼 재귀를 거친 뒤 다시 삭제하는 과정이 필요하다.



### 기타

- dfs에서 return으로 구현 가능, 스택 while로도 구현 가능하다. 이 때 큐를 사용하고 맨 앞 값을 꺼낸다면 bfs다.

- visited로 간 거리 알 수 있으며, 인자로 넘겨서도 알 수 있다.
- 하위 재귀에서 올라온 리턴값을 다른 가지에서 올라온 값과 비교해 상위 함수로 넘겨주는 방법도 있다.