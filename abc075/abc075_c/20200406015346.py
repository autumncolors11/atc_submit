import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input
def ss(): return sys.stdin.readline().rstrip() #input()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

n,m=mii()

def dfs(mat,v):
    seen[v]+=1
    for pv in mat[v]:
        if seen[pv]:
            continue
        dfs(mat,pv)

ans=0
arr=[]
for i in range(m):
    x,y=mii()
    arr.append([x-1,y-1])

for i in range(m):
    seen=[0]*n
    mat=[[] for _ in range(n)]
    for j,k in enumerate(arr):
        if i!=j:
            a,b=k
            mat[a].append(b)
            mat[b].append(a)
    dfs(mat,1)
    if sum(seen)!=n:
        ans+=1

print(ans)
