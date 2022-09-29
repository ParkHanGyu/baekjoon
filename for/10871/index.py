import sys

N, X = map(int, sys.stdin.readline().split())
A = list(int(input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")