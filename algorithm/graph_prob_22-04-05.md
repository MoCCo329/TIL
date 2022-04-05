## 그래프 문제

### 1. 그룹 만들기

내 답

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    adjL = [[i] for i in range(N + 1)]
    for i in range(M):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)
 
    v = [0] * (N + 1)
    for i in range(1, N + 1):
        if v[i] == 0:
            v[0] += 1  # v[0]은 cnt
            q = [i]
            while q:
                j = q.pop(0)
                v[j] = 1
                for k in adjL[j]:
                    if v[k] == 0:
                        q.append(k)
    print(f'#{tc} {v[0]}')
```

여기서 q 의 초깃값을 [i]가 아닌 adjL[i]로 두었더니 원하는 답이 나오지 않았다. 이는 얕은 복사로 인한 문제로 q와 adjL이 같은 주소를 가르켜 생기는 간단한 이유였다. 이걸 못 알아차리고 한참동안 왜 안되는지 생각했다.



### 2. 숫자 만들기

숫자는 자리가 고정되는데, 또 문제 제대로 안보고 숫자들도 조합하여 푸는 뻘짓을 했다. 시간이 너무 오래걸리고 답도 다르게 나왔는데도 문제를 정독할 생각을 않고 코드에서 답을 찾으려 했다.



### 3. 홈 방범 서비스

내 답

```python
def f(i, j, k):
    global ans
    cnt = 0
    for hi, hj in house:
        if abs(hi - i) + abs(hj - j) < k:
            cnt += 1
    if 2 * k**2 - 2 * k + 1 <= cnt * M:
        if ans < cnt:
            ans = cnt
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house = []
    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append((i, j))

    for i in range(N):
        for j in range(N):
            for k in range(2 * N - 1):
                f(i, j, k)

    print(f'#{tc} {ans}')
```

우수 답

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # 도시의 크기, 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    home = []
    for i in range(N):      # 배열에서 집의 위치를 home 리스트에 저장
        for j in range(N):
            if arr[i][j]:
                home.append((i,j))
    ans = 0
    for i in range(N):      # 도시의 각 지점을 순회하면서 
        for j in range(N):
            count = [0] * 2 * N
            for hi, hj in home:     # 각 지점별로 집과의 거리를 구하고 count 리스트에 같은 거리의 집 수를 저장
                K = abs(i - hi) + abs(j - hj) + 1
                count[K] += 1
            for k in range(1, 2 * N):   # count 리스트를 누적합으로 바꿔줌
                count[k] += count[k - 1]
            for k in range(1, 2 * N):   # count 리스트의 인덱스가 서비스 영역 K이고, 값이 서비스 영역에 있는 집의 수
                if k ** 2 + (k - 1) ** 2 <= count[k] * M and ans < count[k]:
                    ans = count[k]
    print(f'#{tc} {ans}')
```

각 좌표에서 집들의 거리에 따른 방범 범위에 드는지 확인하고 비용이 타당하다면 최댓값과 비교하고 최댓값을 갱신하였다. 더 빠른 방법이 있었는데, counts 배열에 k값 인덱스로 범위 내 집의 수를 넣고 중첩하면 k값 for문을 하지 않더라도 해당 좌표에서의 최댓값을 구할 수 있었다.