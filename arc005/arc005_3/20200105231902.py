from collections import deque

h,w = map(int,input().split())

a = []


for i in range(h):
    m =input()
    a.append(m)


b = [[100000000]*w for _  in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j] == "s":
            sy,sx = i,j
            b[i][j] =0
        elif a[i][j] == "g":
            gy,gx = i,j


n = deque()
n.append((sy,sx))
while n:
    i,j = n.popleft()
    
    cnt = b[i][j]
    for di,dj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
        if (0 &lt;= di &lt;= h-1) and (0 &lt;= dj &lt;= w-1) and b[di][dj] == 100000000:
            if a[di][dj] == "." or a[di][dj]=="g":
                b[di][dj] = cnt
                n.appendleft((di,dj))
            elif a[di][dj] == "#":
                b[di][dj] = cnt +1
                n.append((di,dj))

if b[gy][gx] &lt;= 2:
    print("YES")
else:
    print("NO")

