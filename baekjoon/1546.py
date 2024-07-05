N = input()
num = list(map(int,input().split(" ")))
new =[i/max(num)*100 for i in num]

print(float(sum(new)/int(N)))