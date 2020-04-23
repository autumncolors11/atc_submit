#初期地点
h,w = map(int,input().split())
n=[]
a=[]
a.append(["&amp;"]*(w+2))
for i in range(h):
    arrc = list(input())
    arrc = ["&amp;"]+arrc+["&amp;"]
    b = arrc
    for j in range(len(arrc)):
        if b[j] == "#":
            n.append((i+1,j))
    a.append(b)
a.append(["&amp;"]*(w+2))


#方向
p=[[1,0],[0,1],[-1,0],[0,-1]]
#距離のカウント
cnt=-1
#探索
while n:
    cnt +=1
    n2=[]
    #通った所で総当り
    for i,j in n:
        for di,dj in p:
            di +=i
            dj +=j
            if a[di][dj]==".":
                a[di][dj]="#"
                n2.append((di,dj))
    n=n2
print(cnt)
