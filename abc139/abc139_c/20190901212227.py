masu = int(input())
height = list(map(int,input().split()))

count = 0
n = 0
for i in range(1,masu):
    if height[i-1] - height[i] &gt;=0:
        n +=1
        if n &gt;= count:
            count = n
    
    elif height[i-1] - height[i] &lt; 0:
        if n &gt;= count:
            count = n
        
        n = 0

print(count)
