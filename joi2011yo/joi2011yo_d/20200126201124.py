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
def ii(): return int(sys.stdin.readline().rstrip()) 
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

n = ii()
a = limii()
#0以上20以下でDP
dp = [0]*21
dp[a[0]] = 1
for i in range(1, n-1):
    ex = [0]*21
    
    for j in range(21):
        if 0&lt;= j+a[i] &lt;=20:
            ex[j+a[i]] += dp[j]
        if 0&lt;= j-a[i] &lt;=20:
            ex[j-a[i]] +=dp[j]
    dp = ex
print(dp[a[-1]])
