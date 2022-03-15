T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    build_times = [0] + list(map(int, input().split()))
    K_list = [[0] for _ in range(K + 1)]
    for _ in range(K):
        need, i = map(int, input().split())
        if K_list[i] == [0]:
            K_list[i] = [need]
        else:
            K_list[i] += [need]
    F = int(input())

    for j in range(2, K+1):
        temp = []
        for k in K_list[j]:
            temp += K_list[k]
            print(temp)
        temp += K_list[j]
        temp += [j]
        K_list[j] = list(set(temp))
    print(K_list)

    temp = 0
    for K in K_list[F]:
        temp += build_times[K]
    print(temp)