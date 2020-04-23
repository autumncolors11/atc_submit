import sys
sys.setrecursionlimit(10**6)
from collections import Counter,defaultdict,deque

#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

h,w = mii()
 
a = []
 
for i in range(h):
    m =input()
    a.append(m)
 
b = [[10**10]*w for _  in range(h)]
 
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
        if (0 &lt;= di &lt;= h-1) and (0 &lt;= dj &lt;= w-1) and b[di][dj] == 10**10:
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
