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

h,w,k=mii()

arr=[list(ss()) for _ in range(h)]
mat1=[[0]*w for _ in range(h)]
height=[]
cnt1=0
chk1=True
tmp1=1
for i in range(h):
    if "#" in arr[i]:
        if chk1!=True:
            height.append(tmp1)
            tmp1=1
            cnt1+=1
        
        for j in range(w):
            mat1[i][j]=cnt1
        chk1=False
        
    else:
        for j in range(w):
            mat1[i][j]=cnt1
        tmp1+=1
height.append(tmp1)
#print(height)

ans=[[0]*w for _ in range(h)]

start=0
tmp=1
chk=False
for i in height:
    for j in range(w):
        if "#" in [arr[p][j] for p in range(start,start+i)]:
            if chk!=False:
                tmp+=1
            for k in range(start,start+i):
                ans[k][j]=tmp
            chk=True
        else:
            for k in range(start,start+i):
                ans[k][j]=tmp
    tmp+=1
    start+=i
    chk=False
    
for j in range(h):
    print(*ans[j])               




        
