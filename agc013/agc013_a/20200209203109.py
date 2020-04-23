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
def mss(): return sys.stdin.readline().rstrip()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

n=ii()
arr=limii()
cnt=0
if n==1:
    print(1)
    exit()

if arr[0]&lt;arr[1]:
    temp=0
elif arr[0]==arr[1]:
    temp=1
else:
    temp=2
    
for i in range(n-1):
    if temp==0:
        if arr[i]&lt;= arr[i+1]:
            pass
        else:
            cnt+=1
            temp=1
    elif temp==1:
        if arr[i]&lt;arr[i+1]:
            temp=0
        elif arr[i]==arr[i+1]:
            pass
        else:
            temp=2
    else:
        if arr[i]&gt;=arr[i+1]:
            pass
        else:
            cnt+=1
            temp=1
print(cnt+1)
    
    
    
    
