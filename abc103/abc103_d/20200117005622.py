n,m = map(int,input().split())

arr=[]

for i in range(m):
    b = list(map(int,input().split()))
    arr.append(b)

arr.sort(key=lambda x: x[1])

#print(arr)

ans=1
start=0
fin=10**10
for i,j in arr:
    if fin &gt; i &gt;= start:
        start = max(i,start)
        if j&lt;=fin:
            fin = min(j,fin)
            #print(i,j)
    elif i &gt;= fin:
        ans+=1
        start = i
        fin = j

print(ans)
        
        
