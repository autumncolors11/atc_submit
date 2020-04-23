n = int(input())

arr = list(map(int,input().split()))

count = 0

for i in range(n-1):
    
    for j in range(i+1,n):
        count += arr[i]*arr[j]


print(count)
        
