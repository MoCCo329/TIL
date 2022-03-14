import sys

arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(9))

def cross_chk(i, j, a):
    for m in range(9):
        if arr[i][m] == a:
            return 0
        if arr[m][j] == a:
            return 0
    else:
        return 1

def sector_chk(i, j, a):
    for k in range(3):
        for l in range(3):
            if arr[i//3 * 3 + k][j//3 * 3 + l] == a:
                return 0
    else:
        return 1

def f(i, j):
    if i == 9:
        for k in range(9):
            print(*arr[k])
        exit(0)
    elif arr[i][j] == 0:
        for l in range(1, 10): # 0자리에 들어갈 수 l
            if cross_chk(i, j, l) and sector_chk(i, j, l):
                arr[i][j] = l
                f(i+((j+1)//9), (j+1)%9)
                arr[i][j] = 0
        else: # 값이 없으면 뒤로
            return
    else:
        f(i+((j+1)//9), (j+1)%9)

f(0, 0)