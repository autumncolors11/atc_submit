
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

count = 0

for a in range(n-2):
    k = a+2
    for j in range(a+1,n):
        while (k &lt; n and arr[a] + arr[j] &gt; arr[k]):
            k+=1
        
        if k&gt;j:
            count += k-j-1
        
print(count)
