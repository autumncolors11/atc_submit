n,m = map(int,input().split())

ans = 0
clear = 0

chk = [0]*(n+1)

for i in range(m):
    p,s = input().split()
    p = int(p)
    if chk[p] &gt;=0:
        if s=="WA":
            chk[p]+=1
        elif s =="AC":
            ans += chk[p]
            chk[p]=-1
            clear+=1

print(str(clear)+" "+str(ans))
