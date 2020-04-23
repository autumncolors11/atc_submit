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

n = ii()
arr = limii()
dp = [0]*n
chk=True
cnt=1
while chk:
    if cnt==1:
        dp[cnt] = abs(arr[cnt]-arr[cnt-1])
    else:
        dp[cnt] = min(abs(arr[cnt]-arr[cnt-1])+dp[cnt-1],abs(arr[cnt]-arr[cnt-2])+dp[cnt-2])

    if cnt==n-1:
        chk=False
    cnt+=1
