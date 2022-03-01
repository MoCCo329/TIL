T = int(input())
for tc in range(1, T+1):
    word = input().strip()
    ans = 0

    if str(word) == str(word[::-1]):
        ans = 1

    print('#'+str(tc), ans)