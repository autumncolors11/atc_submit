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
def mss(): return sys.stdin.readline().rstrip()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

n=ii()
arr=limii()
    
I = arr.count(3)
J = arr.count(2)
K = arr.count(1)
    
dp = [[[0 for _ in range(I+J+K+1)] for __ in range(I+J+1)]
        for ___ in range(I+1)]
    
for i in range(I+1):
    for j in range(I+J+1-i):
        for k in range(I+J+K+1-i-j):
            if i + j + k == 0:
                continue
            tmp = 0
            if k &gt; 0:
                tmp += (k/n)*dp[i][j][k-1]
            if j &gt; 0:
                tmp += (j/n)*dp[i][j-1][k+1]
            if i &gt; 0:
                tmp += (i/n)*dp[i-1][j+1][k]
            dp[i][j][k] += (n/(i+j+k))*(1 + tmp)
    
print(dp[I][J][K])
