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
arr0=limii()

arr=Counter(arr0)

ai=list(arr.items())
ai.sort()
if n%2==0:
    cnt=0
    for p,i in enumerate(range(1,n,2)):

        if ai[p][0]==i and ai[p][1]==2:
            cnt+=1
    if cnt==n//2:
        print((2**(n//2))%mod)
    else:
        print(0)
else:
    cnt=0
    for p,i in enumerate(range(0,n,2)):
        if p==0:
            if ai[p][0]==i and ai[p][1]==1:
                cnt+=1
        else:        
            if ai[p][0]==i and ai[p][1]==2:
                cnt+=1
    if (n+1)//2==cnt:
        print((2**(cnt-1))%mod)
    else:
