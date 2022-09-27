X = int(input()) #토탈금액
N = int(input()) #물건 종류 수
sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum += a * b
if X == sum:
    print('Yes')
else:
    print('No')