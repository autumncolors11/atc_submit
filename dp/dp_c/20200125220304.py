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
arr = llint(n)
dp = [[0]*3 for _ in range(n)]
dp[0][0],dp[0][1],dp[0][2]=arr[0][0],arr[0][1],arr[0][2]
for i in range(1,n):
    for abc in [0,1,2]:
        if abc==0:
            dp[i][0] = max(arr[i][0]+dp[i-1][1],arr[i][0]+dp[i-1][2])
        elif abc==1:
            dp[i][1] = max(arr[i][1]+dp[i-1][0],arr[i][1]+dp[i-1][2])
        else:
            dp[i][2] = max(arr[i][2]+dp[i-1][1],arr[i][2]+dp[i-1][0])

print(max(dp[-1][0],dp[-1][1],dp[-1][2]))
