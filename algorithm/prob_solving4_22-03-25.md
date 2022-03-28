## 문제풀이4

### 1. 정식이의 은행업무

내 답

```python
def cor(i, L):  # 2진수 i번째 수 고치기
    N = 0
    for j in range(L):
        if j == i:
            N += ((int(bi[-j-1]) + 1) % 2) * 2**j
        else:
            N += int(bi[-j-1]) * 2**j
    return N
 
T = int(input())
for tc in range(1, T+1):
    bi = input()
    tr = input()
    L = len(bi)
 
    M = 0
    for i in range(len(tr)):
        M += int(tr[-i-1]) * 3**i
 
    for i in range(L):
        N = cor(i, L)
        dif = abs(N - M)
 
        for j in range(len(tr)):
            if dif == 0 or dif == 3**j or dif == 2 * 3**j:
                print(f'#{tc} {N}')
```

모범 답

```python
def solve(lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i]+1)%2
 
        dec = 0 # 10진수로 변환
        for idx in range(len(lst2)):
            dec = dec*2 + lst2[idx]
 
        s = []  # 3진수로 변환
        ret = dec
        while dec>0:
            s.append(dec%3)
            dec //= 3
        lst = lst3[::-1]
 
        cnt = 0
        for idx in range(min(len(s), len(lst))):
            if s[idx]!=lst[idx]:
                cnt+=1
        cnt += abs(len(s)-len(lst)) # 길이가 다르다면 다른값
 
        if cnt == 1:
            return ret
 
        lst2[i] = (lst2[i] + 1) % 2 # 원래대로 복구
 
 
T = int(input())
for test_case in range(1, T + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve(lst3)
    print(f'#{test_case} {ans}')
```

이진수를 10진수로 바꾸고 다시 3진수로 바꾸어 각 자리수의 차이를 확인하는 방법이 있었다. 나는 좀 더 주관을 도입하여 수학적인 풀이를 했으나 모범답안도 떠올렸어야 했는데, 그렇지 못했다.



### 2. 홈 방범 서비스

내 답

```python
def f(i, j, k):
    cnt = 0
    for ni in range(N):
        for nj in range(N):
            if arr[ni][nj] == 1 and abs(i - ni) + abs(j - nj) < k:
                cnt += 1
    if 2 * k**2 - 2 * k + 1 <= cnt * M:
        return cnt
    else:
        return 0
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
 
    for i in range(N):
        for j in range(N):
            k = 1
            while k <= N+1:
                ans += [f(i, j, k)]
                k += 1
 
    print(f'#{tc} {max(ans)}')
```

모범 답

```python
def solve_loop(): # 단순무식하지만, 꼼꼼하게 따져보면 제일 쉽게 접근하는 방법일수도 있습니다
    sol = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1,2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    for j in range(sj-k+1+abs(i-si), sj+k-abs(i-si)):
                        if 0<=i<N and 0<=j<N and arr[i][j]:
                            cnt += 1
                if k*k+(k-1)*(k-1)<=cnt*M and sol<cnt:
                    sol=cnt
    return sol
 
def BFS(si, sj):    # 루프보다 효율적 => K를 늘려가면서 추가되는 부분만 카운트하기 때문에...
    q = []
    v = [[0]*N for _ in range(N)]
    sol = cnt = old = 0
 
    q.append((si,sj))
    v[si][sj]=1
    if arr[si][sj]:
        cnt+=1
 
    while q:
        ci,cj = q.pop(0)
        if old != v[ci][cj]:
            old = v[ci][cj]
            if cost[v[ci][cj]]<=cnt*M and sol<cnt:
                sol = cnt
 
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                if arr[ni][nj]:
                    cnt += 1
    return sol
 
def solve_bfs():
    sol = 0
    for si in range(N):
        for sj in range(N):
            t = BFS(si, sj)
            if sol<t:
                sol=t
    return sol
 
def solve_tbl():    # 테이블에 저장해놓고 활용하는 가장 좋은 풀이법입니다
    home = []
    sol = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i,j))
 
    for si in range(N):
        for sj in range(N):
            cnts = [0]*40
            for ci,cj in home:
                dist = abs(si-ci)+abs(sj-cj)+1
                cnts[dist]+=1
            for i in range(1,40):
                cnts[i]+=cnts[i-1]
 
            for k in range(1,40):
                if cost[k]<=cnts[k]*M and sol<cnts[k]:
                    sol = cnts[k]
    return sol
 
cost = [0]+[k * k + (k - 1) * (k - 1) for k in range(1, 40)]
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # ans = solve_loop()
    # ans = solve_bfs()
    ans = solve_tbl()
    print(f'#{test_case} {ans}')
```

나는 매 좌표마다 k를 달리하며 전체 배열을 찾았고, 그에따라 시간 복잡도가 늘어났다. 하지만 집들을 먼저 찾아 리스트에 담아두어 활용하면 매번 전체 배열을 순회할 필요가 없었다. 더 효율적인 알고리즘을 짜도록 계속해서 생각하자.
