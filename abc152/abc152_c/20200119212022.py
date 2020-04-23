n=int(input())
p=list(map(int,input().split()))
ans = 10**10
cnt=0
for i in range(n):
    if p[i]&lt;= ans:
        ans=min(p[i],ans)
        cnt+=1
    else:
        ans =min(p[i],ans)
        
print(cnt)
