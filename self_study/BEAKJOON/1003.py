def fibo_cnt(n):
    global memo
    if len(memo)-1 < n:
        for _ in range(len(memo)-1, n):
            memo.append([memo[-1][0] + memo[-2][0], memo[-1][1] + memo[-2][1]])
        print(memo[n][0], memo[n][1])
        return
    else:
        print(memo[n][0], memo[n][1])
        return


memo = [[1, 0], [0, 1]]
N = int(input())
for _ in range(N):
    fibo_cnt(int(input()))