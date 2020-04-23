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
n=ii()
a,b,c=[],[],[]

for i in range(n):
    x,y,z=mii()
    a.append(x)
    b.append(y)
    c.append(z)

dp=[[0]*n for i in range(3)]
dp[0][0],dp[1][0],dp[2][0]=a[0],b[0],c[0]
for i in range(1,n):
    for j in [0,1,2]:
        if j==0:dp[0][i]=max(dp[1][i-1]+a[i],dp[2][i-1]+a[i])
        elif j==1:dp[1][i]=max(dp[0][i-1]+b[i],dp[2][i-1]+b[i])
        elif j==2:dp[2][i]=max(dp[1][i-1]+c[i],dp[0][i-1]+c[i])

print(max(dp[0][-1],dp[1][-1],dp[2][-1]))

