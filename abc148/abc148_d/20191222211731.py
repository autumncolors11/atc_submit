n = int(input())

arr = list(map(int,input().split()))

count = 0
ans = 0
for i in range(n):
    if arr[i] == count +1:
        count +=1
    
    else:
        ans +=1

if ans &lt;n:
    print(ans)
else:
    print("-1")
