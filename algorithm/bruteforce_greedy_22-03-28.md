## 완전탐색과 그리디

### 1. 반복(Iteration)과 재귀(Recursion)

- 해결할 문제를 고려해서 반복이나 재귀의 방법을 선택한다.
- 재귀는 알고리즘 설계가 간단하고 짧지만, 더 많은 메모리와 연산을 필요로 한다. 때문에 입력값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있다.



### 2. 완전탐색(Brute Force)

- 순열

```python
def f(i, k, n):
    if i == k:
        print(p)
    else:
         for j in range(m):
                if used[j] == 0:
                    used[j] = 1
                    p[i] = a[j]
                   	f(i+1, k, m)
                    used[j] = 0
	return

a = [1, 2, 3, 4, 5]
p = [0] * 3
used = [0] * 5
f(0, 3, 5)  # 5개중 3개를 고르는 중복순열을 사전순으로 나열
```



- 부분집합

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print('%d'%arr[j], end='')
    print()
```



- 조합

```python
def nCr(n, r, s, k):  # n개에서 r개를 고르는 조합, s는 선택할 수 있는 구간의 시작, k는 고른 개수
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):  # n-r+k가 선택할 수 있는 구간의 끝. n-r이 처음의 최댓값
            comb[k] = A[i]
            nCr(n, r, i+1, k+1)

def nCr(n, r, s, k):  # k는 원래 r값
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[k-r] = A[i]  # r을 줄여가며 인덱스로 사용
            nCr(n, r-1, i+1, k)

n = 5
r = 3
comb = [0] * 3
A = [i for i in range(1, n+1)]
nCr(n, r, 0, 0)
```



### 3. 탐욕(Greedy)