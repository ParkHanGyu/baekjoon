N = int(input())
N_list = list(map(int, input().split()[:N]))

print(min(N_list), max(N_list))