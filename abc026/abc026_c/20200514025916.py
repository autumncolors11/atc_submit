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

n=ii()
arr=[[] for _ in range(n)]

for i in range(1,n):
    a=ii()
    a-=1
    arr[a].append(i)

def dfs(p):
    minmoney=10**10
    maxmoney=0
    money=1
    if len(arr[p])&gt;0:
        for i in arr[p]:
            minmoney=min(minmoney,dfs(i)[2])
            maxmoney=max(maxmoney,dfs(i)[2])
        totalmoney=minmoney+maxmoney+1
        return [minmoney,maxmoney,totalmoney]
    else:
        return [1,1,1]
        
print(dfs(0)[2])
    

    



