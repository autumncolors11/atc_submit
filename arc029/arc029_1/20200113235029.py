import itertools
n=int(input())
arr=[]
for i in range(n):
    p=int(input())
    arr.append(p)
    

ans=10**10
for i in list(itertools.product((0,1),repeat=n)):
    p0=0
    p1=0
    
    for j in range(n):
        if i[j]==0:
            p0+=arr[j]
        else:
            p1+=arr[j]
    
    ans = min(ans,max(p0,p1))

print(ans)
