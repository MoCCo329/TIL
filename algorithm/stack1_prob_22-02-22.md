## Stack1 문제

### 1. 파스칼의 삼각형

정상적으로 작동해 pass된 코드들을 교수님께서 리뷰해 주셨는데, 생각보다 잘못된 인덱싱이나, 더 좋은 형태로 수정 가능한 경우가 많았다.

특히 배열의 초기값 arr[0], arr[1]을 부여하는 경우에 주의하자.



### 2. 회문2

다중 for 문을 나오기 위해서 가장 큰 수부터 차례대로 찾으며, if문으로 값을 찾았으면(maxV > 1) break를 걸어 빠져나올 수 있다.



### 3.  반복 문자 지우기

내 답

```python
def eraser(word):
	for i in range(len(word)-1):
    	if word[i] == word[i+1]:
        	word.pop(i)
            word.pop(i+1)
        return eraser(word)
    else:
        return len(word)

T = int(input())
for tc in range(1, T+1):
    word = input()

    print(f'#{tc} {eraser(word)}')
 
#############################################################
 
T = int(input())
for tc in range(1, T+1):
    word = list(input())

    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]: # 같으면
            word.pop(i+1) # 뒤에꺼 빼고
            word.pop(i) # 앞에꺼 빼고
            i = 0 # i 초기화
        else:
            i += 1

	print(f'#{tc} {len(word)}')
    
#############################################################
 
T = int(input())
for tc in range(1, T+1):
    word = input()
    size = len(word)
    stack = [''] * size
    stack[0] = word[0]
    top = 0
 
    for i in range(1, size):
        top += 1
        if stack[top-1] == word[i]:
            top -= 2
        else:
            stack[top] = word[i]
 
    print(f'#{tc} {top+1}')
```

우수 답

```python
T = int(input())
for tc in range(1, T+1):
    S = input()
    stack = []
    cnt = 0
 
    for s in S:
        if cnt != 0 and stack[-1] == s:
            stack.pop()
            cnt -= 1
        else:
            stack.append(s)
            cnt += 1
 
    print(f'#{tc} {cnt}')
```

처음 재귀함수로 풀어보려 했으나 최대 재귀 깊이에 걸려 오류가 발생했다.

다음으로 일반적인 반복문으로 풀어보았으나, 스택을 이용해 풀어보는 문제였기에 다시 풀었다.

append, pop함수를 이용하는 방법보단, stack point를 통해 제어하고 싶었다. 배운데로 top을 -1로 초기화 하고, top에 +1을 하는 것으로 반복문을 시작하는 것을 시도했지만 쉽지 않았다.

결국 stack[0]을 직접 입력하고 top = 0으로 시작하는 지저분한 형태가 되었다. 만약 if top != 0 and stack[top-1] == word[i]: 로 조건을 달았다면 stack[0]을 지정 안하고, top = -1로 시작 가능했다.



### 4. 괄호 검사

모범 답

```python
T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = [0]*len(s)
    top = -1
    ans = 1
    for x in s:
        if x=='{' or x=='(': # 여는괄호 push
            top += 1
            stack[top] = x
        elif x=='}' or x==')':
            if top == -1: # 스택이 비어있으면 오류
                ans = 0
                break
            else: # 스택이 비어있지 않으면 짝 확인
                if x=='}' and stack[top]=='(':  # 짝이 맞지 않으면
                    ans = 0
                    break
                elif x==')' and stack[top] == '{':
                    ans = 0
                    break
                top -= 1    # 짝이 맞으면 pop
    if top != -1:   # 여는 괄호가 남아있는 경우
        ans = 0
    print(f'#{tc} {ans}')
```

