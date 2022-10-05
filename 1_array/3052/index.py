lst = []

for i in range(10) :
    n = int(input())
    lst.append(n % 42)
lst = set(lst)
print(len(lst))

# lst = []
# p = []
# for i in range(10) :
#     lst.append(int(input()))
#     p.append(int(lst[i] % 42))
# p = set(p)
# print(len(p))