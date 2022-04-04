## 분할정복과 백트래킹

### 1. 병합 정렬(Merge Sort)

- 여러개의 정렬된 자료의 집합을 병합하여 한개의 정렬된 집합으로 만드는 방식이다. 자료를 최소 단위까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻는 top-down 방식이다.
- O(n log n)의 시간 복잡도를 갖는다.
- 분할과정과 병합 과정이 존재한다.

```python
def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result += [left.pop(0)]
            else:
                result += [right.pop(0)]
        elif left:
            result += [left.pop(0)]
        elif right:
            result += [right.pop(0)]
    return result
 
 
def merge_sort(M):
    if len(M) == 1:
        return M
 
    mid = len(M) // 2
    left = merge_sort(M[:mid])
    right = merge_sort(M[mid:])
 
    return merge(left, right)
```



### 2. 퀵 정렬

- 병합정렬과의 차이점은 병합정렬은 단지 두 부분으로 나누는 반면에 퀵 정렬은 분할할 때 기준(pivot)을 중심으로 작은편과 큰편을 나눈다. 또한 병합정렬은 정렬 후 병합이란 후처리가 필요하지만 퀵 정렬은 필요하지 않다.

- 맨 왼쪽값을 피봇으로 했는데 해당 값이 가장 작은 경우 분할 효율이 떨어지게 된다. 때문에 맨 왼쪽, 맨 오른쪽, 중앙 값을 비교한 후 중간 값을 왼쪽으로 옮겨 피봇으로 정하기도 한다.

```python
def quick_sort(A, l, r):
    if l < r:  # 정렬할 구간이 있을 때
        s = partition(A, l, r)  # 맨 왼쪽을 피봇으로 하는 경우
        quick_sort(A. l, s-1)
        quick_sort(A, s+1, r)

def partition(A, l, r):
    p = A[l]
    i = l
    j = r
    while i <= j:  # 교차하기 전까지(피봇을 기준으로 정렬되기 전까지)
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:  # 중간에 종료된 경우
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]  # 피봇의 위치를 정확히 정렬된 위치로 이동
```

- Lomuto partition 알고리즘

```python
def partition(A, p, r):  # 리스트 A, 시작값 p, 끝 값 r
    x = A[r]  # 피봇값
    i = p - 1
    
    for j in range(p, r):  # i가 j를 따라가면서 피봇값보다 작으면 i와 j를 바꿔 i쪽을 작은수로 한다.
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
```



### 3. 이진 검색(Binary Search)

- 정렬된 자료 가운데 항목을 키 값과 대소 비교하여 다음 검색 위치를 결정하고 계속 검색을 진행하는 방법이다.

```python
# 반복구조
def binary_search(n, S, key):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == key:
            return mid
        elif S[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# 재귀구조
def binary_search(S, low, high, key):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if S[mid] == key:
            return mid
        elif key < S[mid]:
            return binary_search(S, low, mid - 1, key)
        else:
            return binary_search(S, mid + 1, high, key)
```



### 4. 백트래킹(Back Tracking)

- 상태 공간 트리의 깊이 우선 검색을 하며 각 노드가 유망한지를 점검하여 유망하지 않다면 부모노드로 돌아가며 검색하는 방법이다.
- [stack2_22-02-23.md 참고](./stack2_22-02-23.md)



### 5. 트리(Tree)

- [tree_22-03-16.md 참고](./tree_22-03-16.md)
