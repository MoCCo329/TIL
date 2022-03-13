N = int(input())
arr = list(map(int, input().split()))
pmmd = list(map(int, input().split()))
c_list = []

for i in range(4):
    while pmmd[i]:
        c_list += [i]
        pmmd[i] -= 1

ans = []

def f(i, N):
    global ans
    if i == N:
        sub_ans = arr[0]
        for j in range(1, N+1):
            if c_list[j-1] == 0:
                sub_ans += arr[j]
            elif c_list[j-1] == 1:
                sub_ans -= arr[j]
            elif c_list[j-1] == 2:
                sub_ans *= arr[j]
            else:
                sub_ans = int(sub_ans / arr[j])
        ans += [sub_ans]
        return
    else:
        for j in range(i, N):
            c_list[i], c_list[j] = c_list[j], c_list[i]
            f(i+1, N)
            c_list[i], c_list[j] = c_list[j], c_list[i]

f(0, N-1)
ans.sort()
print(ans[-1])
print(ans[0])