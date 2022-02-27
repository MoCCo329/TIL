## Stack2 문제

### 1. 계산기3 (후위연산자)

내 답

```python
for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''
    stack = [0] * N
    top = -1
    isp = {'+': 1, '*': 2, '(': 0}  # 연산자 우선순위
    for i in range(N):
        if '0' <= infix[i] <= '9':  # 피연산자인 경우
            postfix += infix[i]
             
        elif infix[i] == '(': # 여는 괄호일 경우 스택에 집어넣기
            top += 1
            stack[top] = infix[i]
             
        elif infix[i] == ')': # 닫는 괄호일 경우 여는 괄호가 나올 때까지 스택 pop
            while True:
                if stack[top] == '(':
                    top -= 1
                    break
                else:
                    postfix += stack[top]
                    top -= 1
             
        else:  # 연산자일 경우
            while top > -1 and isp[stack[top]] >= isp[infix[i]]:  # stack[top] 우선순위가 																	같거나 높으면 pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]
    while top > -1:
        if stack[top] != '(':
            postfix += stack[top]
        top -= 1
 
#후위연산자 계산
    op1 = 0
    op2 = 0
    stack = [0] * len(postfix)
    for i in range(len(postfix)):
        if postfix[i] == '+': # +일 때
            op2 = int(stack[top])
            top -= 1
            op1 = int(stack[top])
            top -= 1
 
            top += 1
            stack[top] = op1 + op2
 
        elif postfix[i] == '*': # *일 때
            op2 = int(stack[top])
            top -= 1
            op1 = int(stack[top])
            top -= 1
 
            top += 1
            stack[top] = op1 * op2
 
        else: # 숫자일 때
            top += 1
            stack[top] = int(postfix[i])
 
    print(f'#{tc} {stack[top]}')
```

후위 연산자에 대한 완전한 이해를 마치고 문제풀이에 들어가야 했다. 코드가 일관되지 않고 지저분하다. 쓸데없이 길지 않도록 짧게 표현할 방법이 많이 있었다.



### 2. 미로

내 답

```python
def f(i, j, direction):
    global top
    i += direction[0]
    j += direction[1]
    temp_stack = [i, j, []]
 
    for di, dj in didj:
        if 0<=i+di<N and 0<=j+dj<N and maze[i + di][j + dj] == 3: # 끝지점을 만나면 1 반환
            return 1
        if 0<=i+di<N and 0<=j+dj<N and maze[i + di][j + dj] == 0 and [-di, -dj] != direction: # 갈 수 있는 방향이 있고, 그것이 왔던 방향이 아니라면
            temp_stack[2] += [[di, dj]] # 임시 스택에 저장
 
    if len(temp_stack[2]): # 갈 수 있는 방향이 있으면 스택에 저장
        top += 1
        stack[top] = temp_stack
 
    if len(stack[top][2]): # 갈 방향이 있으면
        return f(stack[top][0], stack[top][1], stack[top][2].pop()) # 갈 수 있는 길 중 하나를 빼서 함수 실행
    else: # 없으면
        while top > 0 and len(stack[top][2]) == 0: # 방향이 나올때까지 top 감소
            top -= 1
        if top == 0 and len(stack[top][2]) == 0: # 스택이 비면 return 0
            return 0
        else: # 방향이 나오면 함수 실행
            return f(stack[top][0], stack[top][1], stack[top][2].pop())
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    didj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    stack = [[]] * N**2 # 스택에는 위치 정보[i, j, [갈 수 있는 방향들]]가 담긴다.
    top = 0
 
    for i in range(N): # stack[0] 찾기 [시작i, j, [갈 수 있는 방향들]]
        for j in range(N):
            if maze[i][j] == 2:
                stack[top] = [i, j, []]
                for di, dj in didj:
                    if 0<=i+di<N and 0<=j+dj<N and maze[i+di][j+dj] == 0:
                        stack[top][2] += [[di, dj]]
        if stack[top]:
            break
    if stack[top][2]:
        ans = f(stack[top][0], stack[top][1], stack[top][2].pop())
    else:
        ans = 0
 
    print(f'#{tc} {ans}')
```

탐색한 지역을 체크하는 리스트를 사용할 생각을 하지 못했다. 이 방법으로 문제를 하결하려다 보니 재귀를 사용했음에도 코드가 매우 길어졌다. 에러를 수정하려다 보니 조건문이 지저분해 졌다. 시작점을 찾는것을 함수로 뺄 수 있었다. 교수님 조언대로 후보지를 저장하는 방식으로 접근했으면 더 깔끔해졌을것 같다.



모범 답

```python
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def dfs1(i, j, N):  # 스택 사용
    stack = []      # 스택생성
    visted = [[0]*N for _ in range(N)]  # visited생성
    while (1):
        # i, j 칸 방문
        visted[i][j] = 1
        if maze[i][j] == 3:  # 목적지면
            return 1
        # 현재 위치 i, j에서 갈 수 있는 곳 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 미로 내부, 벽이 아니고(통로 or 도착칸), 방문하지 않은 칸
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visted[ni][nj]==0:
                stack.append((i, j))    # 현재 위치 스택에 저장
                i, j = ni, nj           # ni, nj로 이동
                break                   # ni, nj 방문
        else: # 갈수있는 칸이 없으면
            if stack:                   # 뒷걸음질
                i, j = stack.pop()
            else:                       # 출발지까지 되돌아온경우
                break                   # 3번칸에 도착할 수 없는 상황
    return 0

def dfs2(i, j, N):      # 재귀
    visited[i][j] = 1
    if maze[i][j]==3:
        return 1
    else:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                if dfs2(ni, nj, N):
                    return 1
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)

    # 미로 탐색
    #ans = dfs1(sti, stj, N)
    #print(f'#{tc} {ans}')
    visited = [[0]*N for _ in range(N)] # dfs2 용
    print(f'#{tc} {dfs2(sti, stj, N)}')
```

탐색한 곳을 기록하는 리스트를 썼을 때 이렇게 간단하게 구현될 수 있다는것에 놀랐다. 또 if 조건문에 재귀함수를 넣어 return 1을 하는 방법이 재미있었다.



### 3. 토너먼트 카드게임

모법 답

```python
def f(i, j):
    if i == j:
        return i
    else:
        left = f(i, (i+j)//2)
        right = f((i+j)//2+1, j)
        return rsp(left, right)

def rsp(A, B):
    if (arr[B] == 1 and arr[A] == 3) or arr[B]-arr[A] == 1:
        return B
    else:
        return A

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(f'#{tc} {f(1, N)}')
```

재귀로 분할하는 연습이 더 되어야 할 것 같다. 언제 어떻게 return할 것인지 확 와닿지 않았다. 분할하여 최하위 층까지 내려가고 if i == j:로 다시 한 층 올라가게 되면 그때부터 rsp()가 시작된다. 이러한 구현을 기억하자.



### 4. 기타

- 함수 내에서 배열 요소에 접근할 때에는 global로 취급(여기서 LEGB를 따르는것이 아니다), 반면 배열 선언은 local로 취급한다.

```python
def f1():
    a[1] = 4

def f2():
    a = [1,2,3,4,5,6]
    f3()

def f3():
    print(a)

a = [1,2,3]
print(a)
f1()
print(a)
f2()

#[1, 2, 3]
#[1, 4, 3]
#[1, 4, 3]
```

