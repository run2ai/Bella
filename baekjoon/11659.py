#누적합 기법 사용
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))

temp =[]
sum_ = 0

for i in num:
    sum_ +=i
    temp.append(sum_)

for _ in range(M):
    i, j = map(int,input().split())
    print(temp[j]-temp[i-1])