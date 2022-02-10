## List1 문제

### 1. Day1-view (빌딩 조망권)

내 답

```python
for T in range(10):
    N = int(input())
    field = list(map(int, input().split()))
 
    cnt = 0
    for i in range(N-4):
        for j in range(field[i+2], 0, -1):
            if field[i] < j and field[i+1] < j and field[i+3] < j and field[i+4] < j:
                cnt += 1
            else:
                break
 
    print(f'#{T+1} {cnt}')
```

주석을 달아 가독성을 늘리는 것이 좋다.

굳이 리스트 앞 뒤에 [0]을 붙일 필요 없이 주어진 조건과 N으로 인덱싱 할 수 있었다. 또 중복되는 계산을 피하기 위해 주변 건물과의 높이차 4개를 리스트에 담아 최솟값을 찾는 방법으로 하는게 정석이였다.



### 2. 숫자 카드

내 답

```python
for T in range(int(input())):
    N = int(input())
    num = input()
    counts = [0] * 10
    for i in range(N):
        counts[int(num[i])] += 1
 
    cnt_max = 0
    idx_max = 0
 
    for idx, cnt in enumerate(counts):
        if cnt >= cnt_max:
            cnt_max = cnt
            idx_max = idx
 
 
    print(f'#{T+1} {idx_max} {cnt_max}')
```

우수답

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    # print(card)
    # card 숫자의 갯수 기록
    cnt = [0] * 10
    for x in card:
        cnt[x] += 1
    # for i in range(N):
    #     cnt[card[i]] += 1
    # 최대 cnt값과 인덱스 찾기 -> 배열 최대원소의 인덱스 찾기.
    maxIdx = 0
    for i in range(10):
        if cnt[maxIdx] <= cnt[i]:    # <= 최대값과 같거나 크면..
            maxIdx = i
    print(f'#{tc} {maxIdx} {cnt[maxIdx]}')
```

idx만 알면 언제든 자료에 접근할 수 있다. enumerate 같은건 최대한 사용하지 말자.



### 3. 구간합

내 답

```python
for T in range(int(input())):
    n, m = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    maxV = arr[0]
    minV = 0
    for num in arr:
        minV += num
         
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += arr[i+j]
        if maxV < sum:
            maxV = sum
        if minV > sum:
            minV = sum
     
    print(f'#{T+1} {maxV-minV}')
```

우수 답 형식

```python
for T in range(int(input())):
    n, m = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    sum_temp = 0
    sum_max = 0
    sum_min = 0
    for i in range(m):
        sum_temp += arr[i]
        sum_max += arr[i]
        sum_min += arr[i]
 
    for i in range(n-m):
        sum_temp -= arr[i]
        sum_temp += arr[i+m]
 
        if sum_temp > sum_max:
            sum_max = sum_temp
        if sum_temp < sum_min:
            sum_min = sum_temp
 
    print(f'#{T+1} {sum_max - sum_min}')
```

모든 부분합을 구하는 것 보다, 앞 수를 더하고 뒷 수를 빼는 방법이 N이 커질수록 유리하다.



### 4. 전기버스

내 답

```python
for T in range(int(input())):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split())) + [n]
 
    charge_cnt = 0
    battery_now = k
    m_idx = 0
    for i in range(1, n):
        if m_list[m_idx] == i and battery_now-1 < m_list[m_idx+1]-i:
            m_idx += 1
            charge_cnt += 1
            battery_now = k
        elif m_list[m_idx] == i and battery_now-1 >= m_list[m_idx+1]-i:
            m_idx += 1
            battery_now -= 1
        else:
            battery_now -= 1
 
        if battery_now == 0:
            charge_cnt = 0
            break
 
    print(f'#{T+1} {charge_cnt}')
```

우수 답

```python
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())     # K 운행거리, N 종점, M 충전기 갯수
    charger = [0] + list(map(int, input().split())) + [N]
    #print(charger)
    cnt = 0
    last = 0    # 마지막 충전위치
    for i in range(1, M+2):     # 도착확인할 정류장 인덱스
        if charger[i]-charger[i-1] > K:     # 운행불가 ( 충전소 사이 거리 초과)
            cnt = 0
            break
        elif charger[i] - last > K:         # 이전 충전소 부터 너무 먼경우
            last = charger[i-1]             # 직전 충전소에서 충전
            cnt += 1                        # 충전 횟수 기록
    print(f'#{tc} {cnt}')
```

```python
T = int(input())
 
for i in range(1, T + 1):
    go, last, char = map(int, input().split())
    chars = list(map(int, input().split()))
    pos = answer = 0
 
    while pos < last:
        if pos + go >= last: # last에 도착할 수 있으면 바로 break
            break
 
        for j in range(pos + go, pos, -1): # 충전기가 있을시 현위치 pos 변경
            if j in chars:
                pos = j
                answer += 1
                break
        else: # pos + go에서 pos 사이에 충전기가 없을시 이동 불가
            print(f'#{i} 0')
            break
 
    if pos + go >= last:
        print(f'#{i} {answer}')
```

한 역별로 따지지 않고, 충전소 단위로 따질 수 있었다. 복잡하게 생각하지 말자.



### 5. 기타  

- 결과에 영향을 주지 않는경우 >보다 >= 이 연산을 한번 더하게 되므로 고려하자.
- 급하게 문제를 풀지 말고, 최적의 방법을 더 생각해 보자. 급하면 오히려 이상한 방법에 빠질 수 있다.