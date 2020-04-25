import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log

#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]


#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

n=ii()
mat = []
for i in range(n):
    a,b=mii()
    mat.append([a,b])
ans=0
for i in range(n):
    for j in range(n):
        if i==j:continue
        dis = (mat[i][0]-mat[j][0])**2 + (mat[i][1]-mat[j][1])**2
        ans=max(dis,ans)
print(ans**0.5)

