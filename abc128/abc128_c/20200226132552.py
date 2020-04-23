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
s=[]
k=[]
for i in range(m):
    temp=limii()
    k0=temp[0]
    s0=temp[1:]
    s.append(s0)
    k.append(k0)

p=limii()
ans=0
#bit全探索
#print(p)
for i in product([0,1], repeat=n):
    #点灯している電球の数
    temp=0

    #全ての電球で探索
    for j in range(m):
        #対象の電球のonになっている個数
        cnt=0
        for x in s[j]:
            
            if i[x-1]==1:
                cnt+=1
            
        if cnt%2==p[j]:
            temp+=1
        #print(i,j,cnt)
    if temp==m:
        ans+=1
print(ans)

