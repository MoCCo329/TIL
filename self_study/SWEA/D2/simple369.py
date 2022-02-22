T = int(input())
for i in range(1, T+1):
    cnt = 0
    for n in str(i):
        if n == '3' or n == '6' or n == '9':
            cnt += 1

    if cnt > 0:
        print('-'*cnt, end=' ')
    else:
        print(str(i), end=' ')