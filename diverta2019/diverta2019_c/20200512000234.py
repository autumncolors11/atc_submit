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
backa=0
frontb=0
backafrontb=0
ans=0
for i in range(n):
    s=list(ss())
    for j in range(len(s)-1):
        if s[j]+s[j+1]=="AB":
            ans+=1
    if s[0]=="B" and s[-1]=="A":
        backafrontb+=1
    elif s[0]=="B":
        frontb+=1
    elif s[-1]=="A":
        backa+=1
#print(backa,frontb,backafrontb,ans)

if backafrontb&gt;0:
    ans+=backafrontb-1

    if backa&gt;0:
        ans+=1 
        backa-=1
    if frontb&gt;0:
        ans+=1
        frontb-=1
    ans+=min(backa,frontb)
else:
    ans+=min(backa,frontb)


print(ans)


