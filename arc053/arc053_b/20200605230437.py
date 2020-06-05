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

s=Counter(list(ss()))

arr=list(s.values())
cnteven=0
leneven=0
cntodd=0
lenodd=[]

for i in arr:
    if i%2==0:
        cnteven+=1
        leneven+=i
    else:
        cntodd+=1
        lenodd.append(i)


#print(cntodd,cnteven,leneven,lenodd)

if cntodd==0:
    print(leneven)
    exit()
p=min(lenodd)
cnt=sum(lenodd)-p*len(lenodd)+leneven
ans=cnt//len(lenodd) + p
if ans%2==0:
    ans-=1
#print(p,cnt,len(lenodd))
print(ans)
    
