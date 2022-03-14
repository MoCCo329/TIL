# def f(x):
#     global memo
#     if len(memo)-1 < x:
#         D_sum = 0
#         for i in range(len(memo)-1, x):
#             for D in K_list[i+1]:
#                 D_sum += D_list[D]
#             D_sum += D_list[i+1]
#             memo.append(D_sum)
#     return memo[x]
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     D_list = [0] + list(map(int, input().split())) # 인덱스 번호의 건물 건설시간
#     K_list = [[0] for _ in range(K+1)] # 인덱스 번호의 건물을 지을 수 있는 조건들이 해당 인덱스에 담김
#     for _ in range(K):
#         need, i = map(int, input().split())
#         if K_list[i] == [0]:
#             K_list[i] = [need]
#         else:
#             K_list[i] += [need]
#
#     F = int(input())
#
#     K_list 조건들을 set으로 모아서 해당 D_list값 + 본인건설시간을 더한다
#
#     memo = [0, D_list[1]]
#     print(f(F))
#     print(K_list)
#     print(memo)


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
    for j in range(2, len(K_list)):
        temp = [1]
        for K in K_list[j]:
            temp += K_list[K]
        temp += [j]
        K_list[j] = list(set(temp))

    temp = 0
    for K in K_list[F]:
        temp += build_times[K]
    temp += build_times[F]
    print(temp)