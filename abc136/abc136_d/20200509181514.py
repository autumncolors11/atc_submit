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
arr=list(ss())
temp=0
centr=0
centl=0
ans=[0]*len(arr)

childeven=0
childodd=0

for i in range(len(arr)):
    if arr[i]=="R":
        if temp==0:
            centr=i
            if i%2==0:
                childeven+=1
            else:
                childodd+=1
        else:
            childeven=0
            childodd=0
            centr=i
            temp=0
            if i%2==0:
                childeven+=1
            else:
                childodd+=1

    else:
        if temp==0:
            temp=1
            centl=i

            if i%2==1:
                ans[centr]+=childeven
                ans[centr+1]+=childodd
            else:
                ans[centr]+=childodd
                ans[centr+1]+=childeven
                
            if (i-centl)%2==0:
                ans[centl]+=1
            else:
                ans[centl-1]+=1

        else:
            if (i-centl)%2==0:
                ans[centl]+=1
            else:
                ans[centl-1]+=1
    #print(ans,childeven,childodd)

print(*ans)
