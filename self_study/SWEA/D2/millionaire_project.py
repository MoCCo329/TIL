T = int(input())
for tc in range(1, T+1):
    days = int(input())
    pr = list(map(int, input().split()))

    sell_p = pr[-1] # 판매가격
    answer = 0
    for p in pr[::-1]: # 뒤로 진행
        if sell_p < p: # 높은 판매가격이 나오면 저장
            sell_p = p
        else: # 아니면 판매수익 저장
            answer += (sell_p - p)

    print(f'#{tc} {answer}')