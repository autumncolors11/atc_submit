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

s=list(ss())
t=ii()
ans=[0,0]
cnt=0
for i in range(len(s)):
    if s[i]=="?":
        cnt+=1
    elif s[i]=="L":
        ans[0]-=1
    elif s[i]=="R":
        ans[0]+=1
    elif s[i]=="U":
        ans[1]+=1
    elif s[i]=="D":
        ans[1]-=1

if t==1:
    print(abs(ans[0])+abs(ans[1])+cnt)
else:
    if abs(ans[0])+abs(ans[1])&gt;=cnt:
        print(abs(ans[0])+abs(ans[1])-cnt)
    else:
        if (abs(ans[0])+abs(ans[1]))%2 != cnt%2:
            print(1)
        else:
            print(0)
