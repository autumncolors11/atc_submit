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

n,m=mii()

arr=sorted(limii())

mat=[]
for i in range(m):
    b,c=mii()
    mat.append([b,c])

mat.sort(key=lambda x: x[1],reverse=True)
maxboundary=mat[0][1]
ans=0
i=0
temp=0
while maxboundary&gt;arr[temp] and temp&lt;n and i&lt;m:
    ans+=mat[i][1]
    
    temp+=1
    if temp==n:
        break
    mat[i][0]-=1
    if mat[i][0]==0:
        i+=1
        if i&lt;m:
            maxboundary=mat[i][1]
    #print(ans,temp,i,mat,maxboundary)

print(ans+sum(arr[temp:]))
