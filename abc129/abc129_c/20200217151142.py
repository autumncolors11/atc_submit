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

INF=-float("inf")

n,m=mii()

arr=lin(m)

dp=[0]*(n+1)

for i in arr:
    dp[i]=INF

if n==1:
    print(1)
    exit()

if dp[1]!=INF:
    dp[1]=1

if dp[1]==INF and dp[2]!=INF:
    dp[2]=1

elif dp[1]==INF and dp[2]==INF:
    print(0)
    exit()
elif dp[1]!=INF and dp[2]!=INF:
    dp[2]+=dp[1]
    

for i in range(2,n+1):
    if dp[i]!=INF:
        if dp[i-1]!=INF and dp[i-2]==INF:
            dp[i]+=dp[i-1]
        elif dp[i-1]==INF and dp[i-2]!=INF:
            dp[i]+=dp[i-2]
        elif dp[i-1]!=INF and dp[i-2]!=INF:
            dp[i]+=dp[i-1]+dp[i-2]
        else:
            dp[i]=0
#print(dp)
print(dp[-1]%mod)

