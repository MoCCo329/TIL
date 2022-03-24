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

------------------------------------------------------------------------

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

print(min(arr[-1]))