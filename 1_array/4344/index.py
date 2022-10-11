n = int(input())

for i in range(n):
    p_list = list(map(int, input().split()))
    p_list = p_list[:p_list[0] + 1]
    del p_list[0]
    listMean = sum(p_list) / len(p_list) # 점수 평균
    mean_over = [] # 평균을 넘는 값

    for a in range(len(p_list)):
        if p_list[a] > listMean:
            mean_over.append(p_list[a] / 100.0 * 100.0)

    print("%.3f%%" % (len(mean_over) / len(p_list) * 100.0))