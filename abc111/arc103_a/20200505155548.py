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
#https://atcoder.jp/contests/abc111/tasks/arc103_a
n=ii()
arr=limii()
arra=[]
arrb=[]

for i in range(n):
    if i%2==0:
        arra.append(arr[i])
    else:
        arrb.append(arr[i])
    
r=list(Counter(arra).most_common(2))
s=list(Counter(arrb).most_common(2))

if len(r)==1 and len(s)==1:
    if r[0][0]==s[0][0]:
        print(len(arra))
        exit()
    else:
        print(0)
        exit()

if r[0][0]==s[0][0]:
    if r[0][1]==s[0][1]:
        print(len(arra)-max(r[0][1],s[0][1]) + len(arra)-max(r[1][1],s[1][1]))
        exit()
    else:
        print(len(arra)-max(r[0][1],s[0][1]) + len(arra)-max(r[1][1],s[1][1]))
        exit()
else:
    print(len(arra)-r[0][1]+len(arra)-s[0][1])
    exit()

#print(n-(c+d))

