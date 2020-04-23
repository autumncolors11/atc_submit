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
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #整数1つinput
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii())
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input
def ss(): return sys.stdin.readline().rstrip() #文字列1つinput
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

n,w = mii()
wei=[]
val=[]
for i in range(n):
    ww,vv=map(int,input().split())
    wei.append(ww)
    val.append(vv)
#dp[i][j]:i番目まで選んで、価値がj以上となる最小の重さ
dp=[[10**10]*(sum(val)+1) for i in range(n+1)]
dp[0][0]=0
for i in range(n):
    for j in range(sum(val)+1):
        if j&gt;=val[i]:
            dp[i+1][j]=min(dp[i][j-val[i]]+wei[i],dp[i][j])
        else:
            dp[i+1][j]=dp[i][j]
ans=[]
for i in range(sum(val)+1):
    if dp[n][i]&lt;=w:
        ans.append(i)
print(max(ans))
