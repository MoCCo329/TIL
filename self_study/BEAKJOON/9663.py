N = int(input())

arr = list([0]*N for _ in range(N))
ans = 0

def f(i, N):
    global ans
    if i == N:
        ans += 1
        return
    else:
        for j in range(N):
            if arr[i][j] != 0:
                pass
            else:
                arr[i][j] += 1
                for k in range(N):
                    arr[i][k] += 1
                    arr[k][j] += 1
                for l in range(-N+1, N):
                    if 0 <= i+l < N and 0 <= j+l < N:
                        arr[i+l][j+l] += 1
                    if 0 <= i+l < N and 0 <= j-l < N:
                        arr[i+l][j-l] += 1

                f(i+1, N)

                arr[i][j] -= 1
                for k in range(N):
                    arr[i][k] -= 1
                    arr[k][j] -= 1
                for l in range(-N+1, N):
                    if 0 <= i+l < N and 0 <= j+l < N:
                        arr[i+l][j+l] -= 1
                    if 0 <= i+l < N and 0 <= j-l < N:
                        arr[i+l][j-l] -= 1
        else:
            return

f(0, N)
print(ans)