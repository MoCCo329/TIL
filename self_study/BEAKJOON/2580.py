import sys

arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(9))

def f(i, j):
    if i == 9:
        for i in range(9):
            print(*arr[i])
        exit(0)
    elif arr[i][j] == 0:
        for l in range(1, 10): # 0자리에 들어갈 수 l
            chk = 0
            for m in range(9):
                if arr[i][m] == l:
                    chk = 1
                    break
                if arr[m][j] == l:
                    chk = 1
                    break
            for n in range(3):
                for o in range(3):
                    if arr[i//3 * 3 + n][j//3 * 3 + o] == l:
                        chk = 1
                        break
                if chk == 1:
                    break
            if chk == 0:
                arr[i][j] = l
                f(i+((j+1)//9), (j+1)%9)
                # arr[i][j] = 0
    else:
        f(i+((j+1)//9), (j+1)%9)

f(0, 0)