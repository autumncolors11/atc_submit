from collections import deque
h,w = 10,10
#map(int,input().split())
a = []
for i in range(h):
    m =list(input())
    a.append(m)

cnt =1
for i in range(h):
    for j in range(w):
        if a[i][j] == "o" and cnt==1:
            sy,sx=i,j
            cnt+=1
        elif a[i][j]=="o":
            cnt+=1


for p in range(h):
    for q in range(w):
        if a[p][q] =="x":
            a[p][q]="o"
            b = [[0]*w for _ in range(h)]
            n=deque()
            n.append((sy,sx))

            chk = 0
            while n:
                i,j = n.pop()
                for di,dj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                    if (0 &lt;= di &lt;= h-1) and (0 &lt;= dj &lt;= w-1) :
                        if a[di][dj]=="o" and b[di][dj] ==0:
                            n.append((di,dj))
                            b[di][dj] = 1
                            chk+=1
   
            if cnt == chk:
                print("YES")
                exit()
            a[p][q]="x"
print("NO")
