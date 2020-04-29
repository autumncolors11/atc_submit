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

sa=list(ss())
sb=list(ss())
sc=list(ss())
cnta,cntb,cntc=-1,-1,-1
lensa=len(sa)
lensb=len(sb)
lensc=len(sc)
temp="a"

while lensa!=-1 and lensb!=-1 and lensc!=-1:
    if temp=="a":
        cnta+=1
        lensa-=1
    elif temp=="b":
        cntb+=1
        lensb-=1
    else:
        cntc+=1
        lensc-=1

    if lensa==-1:
        print("A")
        exit()
    elif lensb==-1:
        print("B")
        exit()
    elif lensc==-1:
        print("C")
        exit()
    #print(lensa,lensb,lensc)
    if temp=="a":
        temp=sa[cnta]
    elif temp=="b":
        temp=sb[cntb]
    else:
        temp=sc[cntc]
    

        


