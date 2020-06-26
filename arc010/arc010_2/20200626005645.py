import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log,gcd
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

#Pythonを用いる場合
#numpy 1.18.0, scipy 1.4.1, scikit-learn 0.22, numba 0.47.0, networkx 2.4
 
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

 
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
holiday=[list(map(str,input().split("/"))) for _ in range(n)]

month=[31,29,31,30,31,30,31,31,30,31,30,31]

cnt=0
tmp=0
re=0
ans=0
chkholiday=False
chksatsun=False
for m in range(1,13):
    for d in range(1,month[m-1]+1):
        cnt+=1
        chkholiday,chksatsun=False,False
        if [str(m),str(d)] in holiday:
            chkholiday=True
        
        if cnt%7==1 or cnt%7==0:
            chksatsun=True
        
        if chksatsun==True and chkholiday==True:
            re+=1
            tmp+=1
        
        elif chksatsun==False and chkholiday==True:
            tmp+=1
        
        elif chksatsun==True and chkholiday==False:
            tmp+=1
        
        else:
            if re&gt;0:
                re-=1
                tmp+=1
            
            else:
                if tmp&gt;0:
                    ans=max(ans,tmp)
                    tmp=0

if tmp&gt;0:
    ans=max(ans,tmp)

print(ans)


