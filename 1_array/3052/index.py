lst = []
p = []
cnt = 0
for i in range(10) :
    lst.append(int(input()))
    p.append(int(lst[i] % 42))
p = set(p)
print(len(p))