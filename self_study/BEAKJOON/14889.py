N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
chk_list = [0] * (N+1)
team = [i for i in range(N)] # 0~N//2까지 1팀 나머지 2팀
ans = []

def f(i, c, N):
    global ans

    if c == N//2: # team1이 완성되면 점수차를 구해 ans에 넣어둔다.
        team1 = 0
        team2 = 0
        for j in range(N//2):
            for k in range(N//2):
                team1 += arr[team[j]][team[k]]
                team2 += arr[team[j + N//2]][team[k + N//2]]
        ans += [abs(team1 - team2)]
        return
    else: # 팀을 섞는다.
        for j in range(i, N):
            if chk_list[j] == True:
                continue
            else:
                team[c], team[j] = team[j], team[c]
                chk_list[j] = True
                f(j+1, c+1, N)
                team[c], team[j] = team[j], team[c]
                chk_list[j] = False

f(0, 0, N)
print(min(ans)) # ans 중 최솟값 출력