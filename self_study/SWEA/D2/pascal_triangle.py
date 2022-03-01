def f(n):
    arr = [[1], [1, 1]]

    if n > 2:
        for i in range(2, n):
            arr += [[1]]
            for j in range(1, i):
                arr[i] += [arr[i-1][j-1] + arr[i-1][j]]
            arr[i] += [1]

    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = f(N)
    print(f'#{tc}')
    for i in range(N):
        print(*ans[i])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*(i+1) for i in range(N)]

    if N > 2:
        for i in range(2, N):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])