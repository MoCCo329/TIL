def w(a, b, c):
    global memo
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        temp1 = memo.get((a, b, c))
        if temp1:
            return temp1
        else:
            temp2 = [memo.get((a, b, c-1)) if memo.get((a, b, c-1)) else w(a, b, c-1) for _ in range(1)]
            temp3 = [memo.get((a, b-1, c-1)) if memo.get((a, b-1, c-1)) else w(a, b, c-1) for _ in range(1)]
            temp4 = [memo.get((a, b-1, c)) if memo.get((a, b-1, c)) else w(a, b, c-1) for _ in range(1)]
            memo[(a, b, c-1)] = temp2[0]
            memo[(a, b-1, c-1)] = temp3[0]
            memo[(a, b-1, c)] = temp4[0]
            memo[(a, b, c)] = temp2[0]+temp3[0]-temp4[0]
            return memo[(a, b, c)]
    else:
        temp1 = memo.get((a, b, c))
        if temp1:
            return temp1
        else:
            temp2 = [memo.get((a-1, b, c)) if memo.get((a-1, b, c)) else w(a-1, b, c) for _ in range(1)]
            temp3 = [memo.get((a-1, b-1, c)) if memo.get((a-1, b-1, c)) else w(a-1, b-1, c) for _ in range(1)]
            temp4 = [memo.get((a-1, b, c-1)) if memo.get((a-1, b, c-1)) else w(a-1, b, c-1) for _ in range(1)]
            temp5 = [memo.get((a-1, b-1, c-1)) if memo.get((a-1, b-1, c-1)) else w(a-1, b-1, c-1) for _ in range(1)]
            memo[(a-1, b, c)] = temp2[0]
            memo[(a-1, b-1, c)] = temp3[0]
            memo[(a-1, b, c-1)] = temp4[0]
            memo[(a-1, b-1, c-1)] = temp5[0]
            memo[(a, b, c)] = temp2[0]+temp3[0]+temp4[0]-temp5[0]
            return memo[(a, b, c)]

memo = {(0, 0, 0): 1}
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')