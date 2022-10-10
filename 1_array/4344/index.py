from tkinter import scrolledtext


n = int(input())

for i in range(n):
    p_list = list(map(int, input().split()))
    p_list = p_list[:p_list[0] + 1]
    del p_list[0]
    listSum = sum(p_list) # 점수 합
    listMean = listSum / len(p_list) # 점수 평균
    u = listMean / 100.0 * 100.0 # 평균 점수 백분율
    z = [] # 각 점수별 백분율

    for a in range(len(p_list)):
        z.append(p_list[a] / 100.0 * 100.0)
    else:
        break
# print(u)