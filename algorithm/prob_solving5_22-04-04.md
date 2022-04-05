## 문제풀이5

### 1. 원자 소멸 시뮬레이션

모범 답

```python
d = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2
    ans = 0

    for _ in range(4002):
        for i in range(len(arr)):
            di, dj = d[arr[i][2]]
            arr[i][0] += di
            arr[i][1] += dj

        ext, temp = set(), set()
        for i in range(len(arr)):
            ci, cj = arr[i][0], arr[i][1]
            if (ci, cj) in temp:
                ext.add((ci, cj))
            temp.add((ci, cj))

        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0], arr[i][1]) in ext:
                ans += arr[i][3]
                arr.pop(i)

    print(f'#{tc} {ans}')
```



우수 답

```python
def meet(a, b):  # 만나면 return 시간
    if abs(a[0] - b[0]) == abs(a[1] - b[1]):  # 대각선위치에서 내려와서 만날때
        t = abs(a[0] - b[0])
        if a[0] + t * mode[a[2]][0] == b[0] + t * mode[b[2]][0] and a[1] + t * mode[a[2]][1] == b[1] + t * mode[b[2]][1]:
            return t
    elif a[0] == b[0]:  # x좌표가 같고
        if a[1] < b[1] and a[2] == 0 and b[2] == 1:
            return (b[1] - a[1]) / 2
        elif a[1] > b[1] and a[2] == 1 and b[2] == 0:
            return (a[1] - b[1]) / 2
    elif a[1] == b[1]:  # y좌표가 같고
        if a[0] < b[0] and a[2] == 3 and b[2] == 2:
            return (b[0] - a[0]) / 2
        elif a[0] > b[0] and a[2] == 2 and b[2] == 3:
            return (a[0] - b[0]) / 2
    return 0  # 안만나면 0
 
 
mode = [[0,1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = [0] * N  # 0:x좌표 1:y좌표 2:방향 3:에너지
    for i in range(N):
        atoms[i] = list(map(int, input().split()))

    times = []
    for i in range(N):
        for j in range(i + 1, N):
            time = meet(atoms[i][:3], atoms[j][:3])
            if time > 0:
                times.append([time, i, j])

    times = sorted(times)
    cnt = 0
    v = [0] * N
    pre = -1
    for m in times:
        if pre == m[0]:
            if v[m[1]] == 0:
                cnt += atoms[m[1]][3]
                v[m[1]] = 1
            if v[m[2]] == 0:
                cnt += atoms[m[2]][3]
                v[m[2]] = 1
            pre = m[0]
        elif v[m[1]] == 0 and v[m[2]] == 0 and pre != m[0]:
            cnt += atoms[m[1]][3] + atoms[m[2]][3]
            v[m[1]] = 1
            v[m[2]] = 1
            pre = m[0]

    print(f'#{tc} {cnt}')
```

이동을 반복하고 원소들을 제거해주는 방식을 구현할 수도 있었고, 어렵지만 시간에 따라 소멸하는 원소들을 계산해 줄 수도 있었다. 나는 이동반복을 계속 시도했는데도, 시간초과나 일부 TC에 걸렸다. 반면 교수님의 설명과 풀이는 너무 간단해 좌절감이 들었다.