h,w = map(int,input().split())

ys,xs=2,2
yg,xg =h+1,w+1

a= []

a.append("".join(["#"]*(w+2)))
cnt=0
for i in range(h):
    arrc = input()
    #迷路中の黒の数
    m = int(list(arrc).count("#"))
    cnt +=m
    
    arrc = "#"+arrc+"#"
    a.append(arrc)

a.append("".join(["#"]*(w+2)))

n=[(ys-1,xs-1)]
route={n[0]:0}
p=[[1,0],[0,1],[-1,0],[0,-1]]
count=1
while route.get((yg-1,xg-1),0)==0 and count != 10000:
    n2=[]
    for i in n:
        for j in p:
            np=(i[0]+j[0],i[1]+j[1])
            if a[np[0]][np[1]]=='.' and route.get(np,-1)==-1:
                n2.append(np)
                route[np]=count
                
    n=n2
    count+=1
if list(route.keys()).count((h,w)) == 1:
    vv = h*w - max(list(route.values())) - cnt -1
    print(vv)
else:
