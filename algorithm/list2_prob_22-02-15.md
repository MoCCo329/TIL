



### 1. Flatten

카운트 정렬의 count 함수에서 맨 오른쪽 값을 1 줄이고 그 왼쪽값을 1 증가시켜 풀 수 있다.



### 2. Snail number

내 답

```python
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    NN = N**2                                       #최대 숫자
    new_arr = [[0]*N for _ in range(N)]             #새로운 배열을 담을 arr
 
    d_list = [[0, 1], [1, 0], [0, -1], [-1, 0]] * N #4가지 방향. 넉넉히 N곱해준다. 원래 필요한 dk 수는 (N*2-1)/4
    dk = 0
    ni = 0
    nj = 0
    k = 1
 
    while k <= NN:
        if 0<=ni+d_list[dk][0]<N and 0<=nj+d_list[dk][1]<N and new_arr[ni+d_list[dk][0]][nj+d_list[dk][1]] == 0: #다음 칸이 범위를 안넘어가면 그대로 new_arr에 k입력
            new_arr[ni][nj] = k
            k += 1
            ni += d_list[dk][0]
            nj += d_list[dk][1]
 
        else: #다음 칸이 범위를 넘어가면 dk += 1 하여 방향을 전환
            new_arr[ni][nj] = k
            k += 1
            dk += 1
            ni += d_list[dk][0]
            nj += d_list[dk][1]
 
    print(f'#{tc}')
    for i in range(N):
        print(*new_arr[i])
```

우수 답

```python
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    
    d = 1
    i = 0
    j = 0
    k = 0    
    while d <= N*N:
		if 0<=i<N and 0<=j<N and arr[i][j]==0:
            arr[i][j] = d
            i, j = i + di[k], j + dj[k]
            d += 1
        else:
            i, j = i - di[k], j - di[k]
            k = (k+1)%4 # 방향 바꾸기
            i, j = i + di[k], j + dj[k]
            
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
```

d를 이용해서 방향으로 접근 할 수 있고, index를 계산해서 풀 수 있다(2*N - 1).

비슷한 방법이여도 훨씬 깔끔하게 구현할 수 있었다.



### 3. 이진 탐색

-7/2 = -3.5, -7//2 = -4, int(-7/2) = -3의 서로 다른 값을 가진다. 즉 int는 절댓값에서 버림하고 부호를 씌운다.

middle 값을 버리지 않는다는 것을 잘 캐치했어야 했다.



### 4. 특별한 정렬

선택정렬을 이용하되 최대 최소를 번갈아 총 10번 정렬하면 된다.



### 5. 기타

- diff 사이트를 이용해 결과값 확인가능
- list(map(list), zip(*arr)) 를 통해 2차원 정사각형 배열을  전치시킬 수 있다.