T = int(input())
memo = [1, 1, 1, 2, 2]

for tc in range(1, T+1):
    N = int(input())
    L = len(memo)
    if L < N:
        for i in range(L, N):
            memo += [memo[i-1] + memo[i-5]]

    print(memo[N-1])