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
def mss(): return sys.stdin.readline().rstrip()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

n,m = mii()

arr=[[] for i in range(n)]
deg=[0 for i in range(n)]
dp = [0]*(n+1)


for i in range(m):
    x,y = mii()
    arr[x-1].append(y-1)
    deg[y-1]+=1

# V: 頂点数
# G[v] = [w, ...]:
#    有向グラフ上の頂点vから到達できる頂点w
# deg[v]:
#    頂点vに到達できる頂点の数

ans = list(i for i in range(n) if deg[i]==0)
deq = deque(ans)
used = [0]*m

while deq:
    v = deq.popleft()
    for t in arr[v]:
        deg[t] -= 1
        if deg[t]==0:
            deq.append(t)
            ans.append(t)
#print(ans)
# ans: トポロジカル順序に並べた頂点

#ans：遷移前
for i in ans:
    ari = arr[i]
    #j：遷移後の座標を出す
    for j in range(len(ari)):
        dp[ari[j]] = max(dp[i]+1,dp[ari[j]])
    
print(max(dp))




