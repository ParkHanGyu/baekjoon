N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
L = []
for i in range(N):
    L.append(lst[i] / M * 100)

print(sum(L)/N)