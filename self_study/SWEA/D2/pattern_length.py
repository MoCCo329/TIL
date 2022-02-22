T = int(input())
for tc in range(1, T+1):
    text = input().strip()
    size = len(text)
    ans = []

    for i in range(10, 1, -1): # i는 길이
        for j in range(size-i): # j는 확인할 text 인덱스
            if text[j] != text[j + i]:
                break
        else: # 모두 겹치는 경우 길이 저장
            ans += [i]

    print(f'#{tc} {ans[-1]}') # 가장 마지막에 나온 결과 출력