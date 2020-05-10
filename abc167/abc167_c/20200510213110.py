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

n,m,x=mii()
chk=False
ansmoney=10**100
c=[]
arr=[]

for i in range(n):
    mat=limii()
    c.append(mat[0])
    arr.append(mat[1:])

for i in product([0,1],repeat=n):
    total=0
    chkarr=[0]*m
    for j in range(n):
        if i[j]==1:
            total+=c[j]
            for k in range(m):
                chkarr[k]+=arr[j][k]
            
    
    cnt=0
    for p in range(m):
        if chkarr[p]&gt;=x:
            cnt+=1
    if cnt==m:
        chk=True
        ansmoney=min(ansmoney,total)
if chk:
    print(ansmoney)
else:
    print(-1)
