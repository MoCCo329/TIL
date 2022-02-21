## String1 문제

### 1. 문자열 비교

내 답

```python
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
 
    # for i in range(len(str2)-len(str1)):   # 인덱싱
    #     if str2[i:i+len(str1)] == str1:
    #         print(f'#{tc} 1')
    #         break
    # else:
    #     print(f'#{tc} 0')
 
    answer = 0
    for i in range(len(str2)-len(str1)+1):   # for문 사용
        cnt = 0
        for j in range(len(str1)):
            if str1[j] == str2[i+j]:
                cnt += 1
 
            if cnt == len(str1):
                answer += 1
 
    print(f'#{tc} {answer}')
```

for 문 사용방식에서 마지막 if 문은 for 문 밖에 적어서 매번 확인하지 않도록 해야됐다.



### 2. 쇠막대기 자르기

내 답

```python
T = int(input())
for tc in range(1, T+1):
    s = input()
 
    answer = 0
    floor = [0] * 50000 # 층별 레이저 수
    f = 0 # 층
 
    for i in range(len(s)):
        if s[i] == '(': # 층 증가
            f += 1
        else: # s[i] == ')'
            if s[i-1] == '(': # 레이저이면 해당 층까지 레이저 수 1씩 증가
                f -= 1
                for i in range(1, f+1):
                    floor[i] += 1
            else: # 레이저가 아니라 층이 사라지는 것이면 레이저 수 + 1 만큼 답 증가
                answer += floor[f] + 1
                floor[f] = 0
                f -= 1
 
    print(f'#{tc} {answer}')
```

우수 답

```python
T = int(input())
for t in range(1, T+1):
    check = input()
    cnt = 0 # 조각의 수
    result = []
    for i in range(len(check)):
        if check[i] == '(':
            result.append('(')
        else:
            if check[i-1] =='(':
                result.pop()
                cnt += len(result)
            else:
                result.pop()
                cnt += 1
    print(f'#{t} {cnt}')
```

나에게는 접근하기 어려운 문제였는데, 다른 분들은 어떻게 간단하고 빠르게 접근했는지 놀랐다. 테스트의 최대 길이가 100000이여서 길이가 50000이나 되는 리스트를 만들었는데, 그러지 않고 단순하게 문자열을 읽으며 풀 수도 있었다. 레이저와 쇠막대, 그리고 조각이 생기는 경우를 더 잘 고민해보고 문제를 풀었으면 좋았을것 같다.



### 3. 숫자 배열 회전

내 답

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    new_arr = [[0]*N for _ in range(N)]
    answer = [[0]*3 for _ in range(N)]
 
    for d in range(3):
        for i in range(N): # N*N 돌면서 new_arr에 90도 회전해서 담기
            for j in range(N):
                new_arr[i][j] = arr[N-1-j][i]
 
        for i in range(N): # 정답 담기
            answer[i][d] = ''.join(map(str, new_arr[i]))
 
        for i in range(N): # 다음 90도 돌리기를 위해 arr에 new_arr deep copy
            for j in range(N):
                arr[i][j] = new_arr[i][j]
 
    print(f'#{tc}')
    for i in range(N):
        print(*answer[i])
```

우수 답

```python
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case}')
    for j in range(N):
        str1 = ''
        str2 = ''
        str3 = ''
        for k in range(N):
            str1 += str(arr[N-k-1][j])
            str2 += str(arr[N-j-1][N-k-1])
            str3 += str(arr[k][N-j-1])
        print(str1, end=' ')
        print(str2, end=' ')
        print(str3)
```

```python
for tc in range(1, int(input()) + 1):
    n = int(input())
    lst = [list(input().split()) for i in range(n)]
    new_lst = ['' for i in range(3*n)] # 빈 문자열 3*n개 리스트
 
    dt = []
    for i in range(n):
        for j in range(n): # str 형태로 덧셈
            new_lst[3 * i] += lst[n - j - 1][i] # 90도 회전
            new_lst[3 * i + 1] += lst[n - i - 1][n - j - 1] # 180도 회전
            new_lst[3 * i + 2] += lst[j][n - i - 1] # 270도 회전
 
    print(f'#{tc}')
    for j in range(n):
        for i in range(3):
            print(new_lst[i + 3 * j],end=' ') # 3개씩 끊어 출력
        print()
```

90, 180, 270회전에서 i, j를 어떻게 제어해야 하는지 더 빠르게 생각해보자. 또 숫자 하나하나를 다루는게 아니라 str로 다루고, +로 붙이는 방법도 있었다.



### 4. 회문2

내 답

```python
for tc in range(1, 11):
    tc = int(input())
    arr = [input() for _ in range(100)]
    answer = 0
 
    for i in range(100): # 가로
        for j in range(100):
            for k in range(100-j, 0, -1):
                for l in range(k//2):
                    if arr[i][j+l] == arr[i][j+k-1-l]:
                        pass
                    else:
                        break
                else: # for문 잘 수행되면 답저장
                    for l in range(k):
                        if answer < k:
                            answer = k
 
    for j in range(100): # 세로
        for i in range(100):
            for k in range(100-i, 0, -1):
                for l in range(k//2):
                    if arr[i+l][j] == arr[i+k-1-l][j]:
                        pass
                    else:
                        break
                else:
                    for l in range(k):
                        if answer < k:
                            answer = k
 
    print(f'#{tc} {answer}')
```

가장 긴 회문의 길이를 찾는 것이므로 회문길이 for 문을 밖으로 빼고, 찾을때 바로 break하는 방법이 가장 빠를 것 같다.