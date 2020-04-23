x,y = map(int,input().split())

cnt=0

p=x

while p &lt;= y:
    cnt+=1
    p=2*p


print(cnt)
