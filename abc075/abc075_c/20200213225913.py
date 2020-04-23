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
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？


"""
グラフ入力例
n,m=mii()
g = [[] for _ in range(n)]
seen = [0]*n
for i in range(m):
    x,y=mii()
    g[x-1].append(y-1)
    g[y-1].append(x-1)
    
"""
#g:グラフ v:スタート地点
def dfs(g, v):
	seen[v] += 1
    #スタート地点
	#print('v :', v)
	
	for nv in g[v]:
		if seen[nv]: continue
        #次の場所
		#print('v nv :', v, nv, 'Recursion')
		dfs(g, nv)

n,m=mii()
arr = []
for i in range(m):
    x,y=mii()
    arr.append([x,y])

ans = 0
for i in range(m):
	g = [[] for _ in range(n)]
	for j, m in enumerate(arr):
		if i != j:
			a, b = m
			g[a-1].append(b-1)
			g[b-1].append(a-1)
		
	seen = [0]*n
	dfs(g, 1)
	#print(i, j, seen)
	
	if sum(seen) != n: ans += 1

print(ans)
