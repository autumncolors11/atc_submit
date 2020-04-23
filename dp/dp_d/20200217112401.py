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

n,w=mii()
wei,val=[0],[0]

for i in range(n):
    x,y=mii()
    wei.append(x)
    val.append(y)

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        if j&gt;=wei[i]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-wei[i]]+val[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])


