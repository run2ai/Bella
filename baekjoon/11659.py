import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))

#시간초과
for _ in range(M):
    i, j = map(int,input().split())
    print(sum(num[i-1:j]))