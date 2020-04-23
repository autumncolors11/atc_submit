num = int(input())

arr = list(map(int,input().split()))

a=[arr[0]]
for i in range(1,num-1):
    a0 = min(arr[i],arr[i-1])

    a.append(a0)
a.append(arr[-1])

print(sum(a))
