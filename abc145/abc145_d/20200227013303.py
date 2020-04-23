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

x,y=mii()

if (x+y) %3!=0:
    print(0)
    exit()
if max(x,y)/min(x,y)&gt;2:
    print(0)
    exit()

def nCk(n, k, mod=10 ** 9 + 7):
    if n &lt; k:
        return 0
    k = min(k, n - k)
    numer = 1
    for x in range(n - k + 1, n + 1):
        numer = (numer * x) % mod
    denom = 1
    for x in range(1, k + 1):
        denom = (denom * x) % mod
    return numer * pow(denom, mod - 2, mod) % mod

n=(2*y-x)//3
m=(2*x-y)//3

