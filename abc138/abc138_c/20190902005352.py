num = int(input())

value = list(map(int,input().split()))
value.sort()

count = 0
for i in range(1,num):
    value[i] = (value[i-1]+value[i])/2

print(value[-1])
