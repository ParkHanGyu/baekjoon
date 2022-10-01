import sys

# sum = 0
# while True:
#     A, B = map(int, sys.stdin.readline().split())
#     print(A + B)
#     sum += 1
#     if sum == 5:
#         break

# try:
#     while True:
#         a, b = map(int, input().split())
#         print(a+b)
# except:
#     exit()

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
