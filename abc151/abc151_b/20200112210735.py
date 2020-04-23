n,k,m=map(int,input().split())

arr = list(map(int,input().split()))

a=sum(arr)

b = n*m - a

if k &gt;= b&gt;0:
    print(b)
elif b &lt;=0:
    print(0)
else:
    print(-1)



