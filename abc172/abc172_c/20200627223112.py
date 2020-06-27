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

n,m,k=mii()
arra=[0]+limii()
arrb=[0]+limii()

cuma=np.cumsum(arra)
cumb=np.cumsum(arrb)
ans=0
cnt=0
tmp=0
placea=0
for i in cuma:
    if i&lt;=k:
        tmp=i
        placea+=1
        ans+=1
        cnt+=1
    else:
        continue
#print(cnt,tmp,ans,placea)
sumb=0
for i in arrb:
    #print(cnt,sumb+i,cuma[placea-1],cuma[placea-1],k,i)
    #print(i)
    if tmp+sumb+i&lt;=k:
        tmp+=i
        sumb+=i
        cnt+=1
        #print(1111111)
    else:

        while sumb+i+cuma[placea-1]&gt;k:
            placea-=1
            cnt-=1
            
            if placea&lt;1:
                break
        if sumb+i&lt;=k:
            tmp+=i
            sumb+=i
            cnt+=1
        #print(1111)
    ans=max(ans,cnt)
    if placea&lt;1:
        break
print(ans-2)

 



