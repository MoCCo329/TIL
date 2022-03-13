N, M = map(int, input().split())
chk_list = [0] * (N+1)
ans = [0] * M


def f(i, c, N, M):
    if c == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return
    elif M-c > N-i:
        return
    else:
        for j in range(i, N):
            if chk_list[j] == True:
                continue
            else:
                ans[c] = j+1
                chk_list[j] = True
                f(j, c+1, N, M)
                chk_list[j] = False

f(0, 0, N, M)