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

x,y,a,b,c=mii()

p=deque(list(reversed(sorted(limii(),reverse=True)[:x])))
q=deque(list(reversed(sorted(limii(),reverse=True)[:y])))
r=deque(sorted(limii(),reverse=True))
pp=p.popleft()
qq=q.popleft()
rr=r.popleft()
for i in range(c):
    if pp&gt;qq:
        if qq&lt;rr:
            q.append(rr)
            if i!=c-1:
                rr=r.popleft()
            qq=q.popleft()
    else:
        if pp&lt;rr:
            p.append(rr)
            if i!=c-1:
                rr=r.popleft()
            pp=p.popleft()
p.append(pp)
q.append(qq)
print(sum(list(p))+sum(list(q)))
        
        
