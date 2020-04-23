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
arr= limii()

bs = [0,399,799,1199,1599,1999,2399,2799,3199,4801]
bc = [0,1,2,3,4,5,6,7,8]
ans = [0,0,0,0,0,0,0,0,0]

for i in range(n):
    score = arr[i]
    chk=True
    ank=0
    while chk:
        if bs[ank]&lt;score&lt;=bs[ank+1]:
            chk=False
        ank+=1
    ans[ank-1]+=1

for i in range(8):
    if ans[i]&gt;0:
        ans[i]=1
if sum(ans[:-1])!=0:
    print(str(sum(ans[:-1]))+" "+str(sum(ans)))
else:
    print(str(1)+" "+str(sum(ans)))




