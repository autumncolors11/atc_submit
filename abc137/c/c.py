import collections
num = int(input())

arr = []

for i in range(num):
    arr.append("".join(sorted(input())))


c = collections.Counter(arr)


cnt = 0
for i in list(c.values()):
    if i ==1:
        continue
    
    cnt += (i-1)*(i)//2

print(cnt)

