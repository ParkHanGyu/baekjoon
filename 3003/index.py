cp = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-li[i], end=' ') # 결과 값을 한줄로 찍어주기 위해 end를 사용