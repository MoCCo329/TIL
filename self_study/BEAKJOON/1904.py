N = int(input())

n1 = 1
n2 = 2
for i in range(3, N+1):
    n1, n2 = n2, (n1+n2)%15746

# if N == 1:
#     print(1)
# else:
#     print(n2)

print([n2 if N != 1 else 1][0])