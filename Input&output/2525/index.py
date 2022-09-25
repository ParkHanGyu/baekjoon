# A, B = map(int, input().split())
# C = int(input())

# if B + C > 119 :
#     A + 2
#     if A > 23 :
#         print(A - 24, (B + C) - 120)
#     else :
#         print(A + 2, (B + C) - 120)

# elif B + C > 59 and B + C < 120 :
#     A + 1
#     if A > 23 :
#         print(A - 24, (B + C) - 60)
#     else :
#         print(A, (B + C) - 60)
# else :
#     print(A, B + C);


H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)