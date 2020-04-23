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

#https://atcoder.jp/contests/arc031/tasks/arc031_2
mat=[]
for i in range(10):
    arr=list(ss())
    mat.append(arr)

ground=0
for i in range(10):
    for j in range(10):
        if mat[i][j]=="o":
            ground+=1

ans=0

for i in range(10):
    for j in range(10):
        if mat[i][j]=="x":
            cnt=0
            task = deque([])
            seen = [[0]*10 for _ in range(10)]
            if i&gt;0 and mat[i-1][j]=="o":
                task.appendleft([i-1,j])
                cnt+=1
                seen[i-1][j]=1
            if i&lt;9 and mat[i+1][j]=="o":
                task.appendleft([i+1,j])
                cnt+=1
                seen[i+1][j]=1
            if j&gt;0 and mat[i][j-1]=="o":
                task.appendleft([i,j-1])
                cnt+=1
                seen[i][j-1]=1
            if j&lt;9 and mat[i][j+1]=="o":
                task.appendleft([i,j+1])
                cnt+=1
                seen[i][j+1]=1
            if cnt==0:
                continue

            while len(list(task))!=0:
                place = task.popleft()
                for dire in [[place[0]-1,place[1]],[place[0]+1,place[1]],[place[0],place[1]-1],[place[0],place[1]+1]]:
                    if 0&lt;=dire[0]&lt;=9 and 0&lt;=dire[1]&lt;=9:
                        if seen[dire[0]][dire[1]]!=1 and mat[dire[0]][dire[1]]=="o":
                            seen[dire[0]][dire[1]]+=1
                            task.appendleft([dire[0],dire[1]])
                            cnt+=1
            ans=max(ans,cnt)

if ans==ground:
    print("YES")
else:
    print("NO")

