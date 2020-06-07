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
mod=998244353
n=ii()
arr=limii()

if arr[0]!=0:
    print(0)
    exit()

if n==1 and arr[0]==0:
    print(1)
    exit()


chk=True

p=Counter(arr)

if p[0]!=1:
    print(0)
    exit()

tmp=0
for i in range(1,max(list(p))+1):
    if p[i]&gt;0:
        pass
    else:
        print(0)
        exit()

ans=1

#掛け算の場合
# (a*b)%mod と同等
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

#割り算の場合
# (a//b)%mod と同等
def div(a,b):
    return a*pow(b, mod-2, mod)

#累乗の場合
#a**n %p と同等
def p_f(a,n,pp):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %pp
        if bi[i]=="1":
            res=(res*a) %pp
    return res

for i in range(max(p.keys())):
    
    ans=(ans*pow(p[i], p[i+1], mod)) %mod
    
print(ans%mod)
