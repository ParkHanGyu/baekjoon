import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)

# for i in range(6):
#     A,B = map(int, sys.stdin.readline().split())
#     if A + B == 0:
#         pass
#     else:
#         print(A + B)