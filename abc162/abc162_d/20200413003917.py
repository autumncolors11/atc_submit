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
s=list(ss())
rarr = []
garr=[]
barr=[]

for i in range(n):
    if s[i]=="R":
        rarr.append(i)
    elif s[i]=="G":
        garr.append(i)
    else:
        barr.append(i)

#組み合わせ全通り
ans=len(rarr)*len(barr)*len(garr)

#[0, 2, 5, 11, 12, 16, 17, 18, 23, 27, 31] 11
#[4, 7, 8, 13, 20, 21, 25, 29, 35] 9
#[1, 3, 6, 9, 10, 14, 15, 19, 22, 24, 26, 28, 30, 32, 33, 34, 36, 37, 38] 19
if len(rarr)&gt;len(garr):
    rarr,garr=garr,rarr
if len(barr)&gt;len(garr):
    barr,garr=garr,barr

garr=Counter(garr)

for r in rarr:
    for b in barr:
        #GRB
        if r-b &gt;0 and garr[r + r-b]:
            ans-=1
        #GBR
        elif b-r &gt;0 and garr[b + b-r]:
            ans-=1
        #RGB BGR
        if r-b &gt;0 and (r-b)%2==0 and garr[b+((r-b)//2)]:
            ans-=1

        elif b-r &gt;0 and (b-r)%2==0 and garr[r+((b-r)//2)]:
            ans-=1
        #RBG
        if r-b&gt;0 and garr[b-(r-b)]:
            ans-=1
        elif b-r&gt;0 and garr[r-(b-r)]:
            ans-=1

print(ans)
