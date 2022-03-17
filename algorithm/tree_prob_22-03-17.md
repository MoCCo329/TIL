## Tree 문제

### 1. 노드의 합

내 답

```python
def post_order(n, N):
    global chk
    if n > N:
        chk += 1
    else:
        post_order(n*2, N)
        post_order(n*2+1, N)
        if chk == 2:
            chk = 0
        elif chk == 1:
            tree[n] = tree[n*2]
            chk = 0
        else:
            tree[n] = tree[n*2] + tree[n*2+1]
 
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
 
    chk = 0
    post_order(1, N)
    print(f'#{tc} {tree[L]}')
```

우수 답

```python
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
    for i in range(M):
        node, n = map(int, input().split())
        arr[node] = n
     
    for i in range(N-M, 0,-1):
        if arr[i] == 0 :
            if i*2+1 <= N :
                arr[i] = arr[i*2] + arr[i*2+1]
            else:
                arr[i] = arr[i*2]
 
    print(f'#{tc} {arr[L]}')
```

말단노드의 값이 주어지고 부모가 자식노드 값들의 합인 완전이진트리에서, 나는 중위순회 함수를 만들어 cnt로 말단 개수를 세고, 그 말단수를 고려하여 자식노드값들의 합을 구하였다. 하지만, 완전이진트리임을 더 잘 이용하여 반복문으로 자식노드값들의 합을 구할 수 있었다. 또한 아래와 같이 리턴값을 이용할 수도 있었다.

참고

```python
def f(v): # 리턴값을 이용한 순회
    if v == 0:
        return 0
    else:
        r = 1 # 임시값
        r += f(ch1[v])
        r += f(ch2[v])
        return r
```



### 2. 장훈이의 높은 선반

내 답

```python
def f(i, c, N, M):  # N개 중에서 M개를 선택하는 조합. c는 현재 저장된 답안 개수, i는 진행된 인덱스
    global ans, chk, B
    if c == M:
        tot = sum(ans_temp)
        if B <= tot < ans:
            ans = tot
    elif M-c > N-i:
        return
    else:
        for j in range(i, N):
            if v[j] == True:
                continue
            else:
                ans_temp[c] = t_list[j]
                v[j] = True
                f(j+1, c+1, N, M)
                v[j] = False
 
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    t_list = sorted(list(map(int, input().split())))
    ans = 2*B
    ans_temp = [0] * N
    v = [0] * (N + 1)
 
    M = 2
    while M <= N:
        f(0, 0, N, M)
        M += 1
 
    print(f'#{tc} {ans-B}')
```

우수 답

```python
def boo(i, n, s, rs):
    global res
    if s >= B:
        if s < res:
            res = s
    elif i == n:
        return
    elif s + rs < B:
        return
    else:
        boo(i + 1, n, s + staff[i], rs - staff[i])
        boo(i + 1, n, s, rs)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    staff = list(map(int, input().split()))
    res = sum(staff)
    boo(0, N, 0, res)
    print(f'#{tc} {res - B}')
```

```python
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
 
    minV = sum(arr)
    for i in range(1<<N):
        cnt = 0
        for j in range(N):
            if i & (1<<j):
                cnt += arr[j]
        if cnt >= B and minV > cnt-B:
            minV = cnt - B
 
    print(f'#{tc} {minV}')
```

내가 구현한 부분집합을 구하는(조합) 함수는 지저분하고, 수행시간도 오래걸렸다. 하지만 나머지를 고려해서 백트래킹을 하면 시간이 단축되며 코드도 깔끔해 진다. 또 비트연산자를 이용해 부분집합들을 구할 경우 더 깔끔해졌다. 조합(부분집합) 구하는 다양한 방법들을 익혀두자.