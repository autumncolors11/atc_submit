num = int(input())
arr = list(map(int,input().split()))
count = 0
ans = 1
for i in range(num):
    if arr[i] &gt; ans:
        ans = arr[i]
    
    elif arr[i] == ans:
        pass
    
    elif ans - arr[i] &gt;=2:
        count +=1
        break

if count ==0:
    print("Yes")
else:
    print("No")
