N, M = map(int, input().split())
ans = [0] * M

def f(i, c, N, M):
    if c == M:
        for a in ans:
            print(a, end=' ')
        print()
    else:
        for j in range(i, N):
            ans[c] = j + 1
            f(j, c+1, N, M)

f(0, 0, N, M)