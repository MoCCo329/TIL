## Start 문제

### 1. 양수, 음수 차이

int(7//2) = 3, int(-7//2) = -4 가 된다(내림)

ceil(-0.4) = 0 이 된다. 크거나 같은 최소 정수(올림)

floor(-0.4) = -1 이 된다. 작거나 같은 정수 중 가장 큰 정수(내림)

trunc(-0.4) = 0 이 된다. 소수를 제외하고 정수만 반환한다(버림)

round(-0.5) = 0, round(-0.6) = -1 이 된다. 소수점 이하의 값이 0.5보다 크면 입력값보다 큰 정수 반환(반올림)



### 2. RGB거리(1149)

내 답

```python
def color(i, tot):  # i번째 집 색칠
    global ans

    if i == N+1:  # 끝까지 색칠했을때 tot가 작으면 저장
        if ans:
            if ans > tot:
                ans = tot
        else:  # tot가 처음 저장될 때
            ans = tot
        return
    elif ans:  # 중간에 tot이 ans 보다 커지면 백
        if ans < tot:
            return

    for j in range(1, 4):  # 색 1,2,3을 정하고 비용을 합쳐 다음 i로 넘긴다
        if v[i-1] != j:
            v[i] = j
            color(i+1, tot + arr[i-1][v[i]])

N = int(input())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
v = [0] * (N+1)
ans = 0
color(1, 0)

print(ans)
```

모범 답

```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

print(min(arr[-1]))
```

단순히 재귀와 백트래킹을 통해 최소값을 찾는것 보다 DP로 단계를 저장하면서 하는게 훨씬 빠르다. 다만 어떤식으로 DP를 구현 할 지 떠오르기가 쉽지 않았다. 너무 컴퓨터만 믿고 완전탐색에 가깝게 하는것 보다, 처음부터 고민을 많이해보고 접근해야 겠다. 이 문제는 각 단계별로 세가지 경우를 모두 고려해 DP를 구현하였다.



### 3. 암호코드 스캔

내 답

```python
ciper = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

def f(code):
    bi = []
    for i in range(8):
        temp = code[i*7:(i+1)*7]
        for j in range(10):
            if ciper[j] == temp:
                bi += [j]
                break
        else:
            return 0
    return bi


def erase(i, j, k, N):
    while i < N and arr[i][j-1] != '0':
        for l in range(j - 56 // 4 * k - 1, j):
            arr[i][l] = '0'
        i += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    codes = []
    result = 0

    for i in range(N):
        for j in range(M - 1, 6, -1):
            if arr[i][j] != '0':
                for k in range(1, 6):
                    temp = ''.join([f'{int(x, 16):04b}' for x in ''.join(arr[i][:j + 1])]).rstrip('0')[-56 * k::k]
                    t = f(temp)
                    if t:
                        codes += [t]
                        erase(i, j+1, k, N)
                        break
                break

    for code in codes:
        if (sum(code[::2]) * 3 + sum(code[1::2])) % 10 == 0:
            result += sum(code)

    print(f'#{tc} {result}')

```

모범 답

```python
h2b = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
 
pwd = {211:0, 221:1, 122:2, 411:3, 132:4, 231:5, 114:6, 312:7, 213:8, 112:9}
 
def erase(r, c, x, N):
    i = r
    j = c - 56*x
    while i<N and bit[i][c-1]==1:
        for k in range(j, c):
            bit[i][k] = 0
        i += 1
 
def f(N, M):
    s = 0
    for i in range(N):
        j = 0
        k = 0
        p = [0]*8
        while j<M:
            cnt = [0]*3
            while j < M and bit[i][j] == 0:
                j += 1
            while j < M and bit[i][j] == 1:
                cnt[0] += 1
                j += 1
            while j < M and bit[i][j] == 0:
                cnt[1] += 1
                j += 1
            while j < M and bit[i][j] == 1:
                cnt[2] += 1
                j += 1
            if cnt[2]>0:  # 암호 패턴이 화면 맨 오른쪽에서 끝나는 경우는???
                x = min(cnt)  # 배율
                r = cnt[0]//x*100 + cnt[1]//x*10 + cnt[2]//x
                p[k] = pwd[r]
                k += 1
                if k == 8: # 암호패턴 완성
                    if ((p[0]+p[2]+p[4]+p[6])*3 + p[1]+p[3]+p[5]+p[7]) % 10 == 0:  # 검증코드가 10의 배수이면
                        s += sum(p)
                    erase(i, j, x, N)  # 마지막 1인 열+1, 현재 i, 배율 x
                    k = 0
 
    return s
 
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]
    bit = [[0]*(M*4) for _ in range(N)]
    for i in range(N):
        for j in range(M): # i행, j열 16진수
            # code[i][j]
            bit[i][j*4+0] = int(h2b[code[i][j]][0])
            bit[i][j*4+1] = int(h2b[code[i][j]][1])
            bit[i][j*4+2] = int(h2b[code[i][j]][2])
            bit[i][j*4+3] = int(h2b[code[i][j]][3])
 
    print(f'#{tc} {f(N, 4*M)}')
```

확인한 것을 지울 생각하지 못해 디버깅하는데 시간이 매우 오래걸렸다. 지우지 않더라도 불가능한것은 빠르게 포기하도록 while과 if문을 짰어야 했다. 나는 비율을 따질때 index slicing으로 하였지만, 정말 말 그대로 비율을 따지는 구현은 위와 같이 0-1-0-1의 반복구조임을 이용해 1, 0, 1의 개수를 세어 확인할 수 있었다.
