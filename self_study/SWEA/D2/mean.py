T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    L = len(numbers)
    temp = numbers[0]
    minV = maxV = numbers[0]
    for i in range(1, L):
        if minV < numbers[i]:
            minV = numbers[i]
        elif maxV > numbers[i]:
            maxV = numbers[i]
        temp += numbers[i]

    temp -= maxV + minV
    print(f'#{tc} {round(temp / (L-2))}')