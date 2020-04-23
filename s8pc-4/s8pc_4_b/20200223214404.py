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

#for i in itertools.product([0,1], repeat=n)


n,k=mii()
arr=limii()
ans=10**100
aa=[]
for i in product([0,1], repeat=n):
    if sum(i)==k:

        tmp=0
        chk=0
        for j in range(n):
            if i[j]==1:
                if chk&gt;=arr[j]:
                    tmp+=chk-arr[j]+1
                    chk+=1
                else:
                    chk=arr[j]
            if i[j]==0:
                chk=max(chk,arr[j])
        #print(tmp,i,arr)
        ans=min(tmp,ans)


