h,w = map(int,input().split())

a= []

for i in range(h):
    arrc = input()
    a.append(arrc)
ans = 0
for gg in range(1,h+1):
    for bb in range(1,w+1):
        if a[gg-1][bb-1] == ".":
            ys=gg
            xs=bb
            n=[(ys-1,xs-1)]
            route={n[0]:0}
            p=[[1,0],[0,1],[-1,0],[0,-1]]
            count=1
            while count != 401:
                n2=[]
                for i in n:
                    for j in p:
                       
                        np=(i[0]+j[0],i[1]+j[1])
                        if 0&lt;=np[0]&lt;=h-1 and 0&lt;=np[1]&lt;=w-1:
                            if a[np[0]][np[1]]=='.' and route.get(np,-1)==-1:
                                n2.append(np)
                                route[np]=count
                n=n2
                count+=1
            
            ll= max(list(route.values()))
            if ll &gt; ans:
                ans = ll

print(ans)
