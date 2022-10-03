n = int(input())
#26
num = n
cnt = 0

while 1 :
    if n < 10 :
        num = int("0" + str(num))
    plus = (num % 100 // 10) + (num % 10)
    num = int(str(num % 10) + str(plus % 10))
    cnt += 1
    if num == n :
        print(cnt)
        break



# n = input()
# #26
# num = n
# cnt = 0

# while 1:
#     if len(num) == 1:
#         num = "0" + num
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     cnt += 1
#     if num == n:
#         print(cnt)
#         break


