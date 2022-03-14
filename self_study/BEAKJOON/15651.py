N, M = map(int, input().split())
ans = [0] * M

def f(i, N, M):
    if i == M:
        for a in ans:
            print(a, end=' ')
        print()
    else:
        for j in range(N):
            ans[i] = j + 1
            f(i+1, N, M)

f(0, N, M)