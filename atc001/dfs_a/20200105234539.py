from collections import deque

h,w = map(int,input().split())

a = []
for i in range(h):
    m =input()
    a.append(m)

for i in range(h):
    for j in range(w):
        if a[i][j] == "s":
            sy,sx = i,j
            break

b = [[0]*w for _ in range(h)]

n = deque()
n.append((sy,sx))
while n:
    i,j = n.pop()
    
    for di,dj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
        if (0 &lt;= di &lt;= h-1) and (0 &lt;= dj &lt;= w-1) :
            if a[di][dj]=="g":
                print("Yes")
                exit()
            elif a[di][dj]=="." and b[di][dj] ==0:
                n.append((di,dj))
                b[di][dj] = 1



print("No")


    
