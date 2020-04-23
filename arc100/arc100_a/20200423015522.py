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
arr=limii()
for i in range(n):
    arr[i]-=i+1

arr.sort()

def med(x):
    h = int(n/2)
    if n%2==0:
        return (arr[h-1]+arr[h])//2
    else:
        return arr[int((n-1)/2)]

ans=10**100
if n%2 ==0:
    ans1=0
    ans2=0
    m=med(arr)
    for i in range(n):
        ans1+=abs(arr[i]-m)
        ans2+=abs(arr[i]-(m+1))
    ans=min(ans1,ans2)
else:
    m=med(arr)
    ans1=0
    for i in range(n):
        ans1+=abs(arr[i]-m)
    ans=ans1
print(ans)



