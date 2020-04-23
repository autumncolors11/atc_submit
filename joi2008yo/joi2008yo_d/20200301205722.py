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
#https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
m=ii()
x,y=mii()
dif=[]

for i in range(m-1):
    x0,y0=mii()
    dif.append([x0-x,y0-y])
dif = list(map(list, set(map(tuple, dif))))
n=ii()
narr=[]
for i in range(n):
    p,q=mii()
    narr.append((p,q))
narr=tuple(narr)
if n==1:
    print(narr[0][0]-x,narr[0][1]-y)
    exit()

for i in range(n):
    mat=deepcopy(dif)
    for j in range(m-1):
        mat[j][0]+=narr[i][0]
        mat[j][1]+=narr[i][1]
    mat=list(map(tuple,mat))
    
    #print(mat,narr)
    if len(set(mat)&amp;set(narr))==m-1:
        print(narr[i][0]-x,narr[i][1]-y)
        exit()


