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
mat=limii()

a=max(mat)


# 初期化（ABC035Cオセロだと最初はすべて黒と仮定される）
arr = [0] * (a+3)

# いもす法の加算処理
for jj in range(n):
    l, r = mat[jj],mat[jj]+2  # 区間[l, r]の入力を受け取る
    arr[l] += 1
    if r+1 != a+3:
        arr[r+1] -= 1
#print(arr)
# いもす法の累積和（構築処理）
cum = [0] * (a+3)
for i in range( a+3):
    cum[i] += cum[i-1] + arr[i]
#print(cum)
# 答えを出力
ans = max(cum[1:])
print(ans)
