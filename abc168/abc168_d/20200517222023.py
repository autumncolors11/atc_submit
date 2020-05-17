import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log,sin,cos
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
n,m=mii()

mat=[[] for i in range(n)]

#前の場所がどこだったか
ans=[-1]*n

for i in range(m):
    a,b=mii()
    mat[a-1].append([a-1,b-1])
    mat[b-1].append([b-1,a-1])


q=deque(mat[0])
#print(q,ans[1])
while len(q)&gt;0:

    node = q.popleft()
    #print(node[1],111,type(node[1]),mat[node[1]])
    if node is not None:
        if ans[node[1]]==-1:
            ans[node[1]]=node[0]
            for i in mat[node[1]]:
                q.append([node[1],i[1]])

print("Yes")
for i in range(1,n):
    print(ans[i]+1)



