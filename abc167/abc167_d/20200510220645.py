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
n,k=mii()
arr=limii()

visited=[0]*n

i=0

town=[0]

while visited[i]==0:
    visited[i]=1
    if i==0:
        visited[i]=1
    
    i=arr[i]-1

    town.append(i)

#town=[0, 5, 1, 4, 2, 1]
b=town.index(town[-1])
#at=[1, 4, 2]
at=deepcopy(town[b:-1])
#print(at,b)

if k&lt;=b:
    print(town[k]+1)
    exit()

else:
    k-=b
    #print(k)
    a=k%len(at)
    #print(a)
    #print(at)
    print(at[a]+1)




