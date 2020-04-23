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

m=0
a=0
r=0
c=0
h=0

for i in range(n):
    s=ss()
    if s[0]=="M":m+=1
    elif s[0]=="A":a+=1
    elif s[0]=="R":r+=1
    elif s[0]=="C":c+=1
    elif s[0]=="H":h+=1
mat=[m,a,r,c,h]
#print(mat)
arr=list(combinations([0,1,2,3,4],3))
ans=0
for i in arr:
    if mat[i[0]]&gt;0 and mat[i[1]]&gt;0 and mat[i[2]]&gt;0:
        ans+=mat[i[0]]*mat[i[1]]*mat[i[2]]
print(ans)










