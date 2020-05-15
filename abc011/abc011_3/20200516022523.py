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

arr=sorted([ii() for _ in range(3)])

if n in arr:
    print("NO")
    exit()

if n&gt;3:
    if arr[0]+1==arr[1] and arr[1]+1==arr[2]:
        print("NO")
        exit()

i=0
while n&gt;0:
    if n-3 in arr:
        
        if n-2 in arr:

            if n-1 in arr:
                pass
            else:
                n-=1
                i+=1
        else:
            n-=2
            i+=1

    else:
        n-=3
        i+=1


if i&lt;=100:
    print("YES")
else:
    print("NO")

