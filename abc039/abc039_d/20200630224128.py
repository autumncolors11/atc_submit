import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log,gcd
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

#Pythonを用いる場合
#numpy 1.18.0, scipy 1.4.1, scikit-learn 0.22, numba 0.47.0, networkx 2.4
 
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

 
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

h,w=mii()

mat=[list(ss()) for _ in range(h)]

chk=[[0]*w for _ in range(h)]

arr=[["."]*w for _ in range(h)]

if h==1 and w==1:
    print("possible")
    print(mat[0][0])
    exit()
elif h==1 and w==2:
    if mat[0][0]==mat[0][1]:
        print("possible")
        print("".join(mat[0]))
        exit()
    else:
        print("impossible")
        exit()
elif h==2 and w==1:
    if mat[1]==mat[0]:
        print("possible")
        for i in range(h):
            print("".join(mat[i]))
        exit()
    else:
        print("impossible")
        exit()
elif w==1:
    for i in range(h):
        if i==0:
            if mat[i][0]==mat[i+1][0]=="#":
                arr[i][0]="#"
                chk[i][0]=1
                chk[i+1][0]=1
        elif i==w-1:
            if mat[i][0]==mat[i-1][0]=="#":
                arr[i][0]="#"
                chk[i][0]=1
                chk[i-1][0]=1
        else:
            if mat[i-1][0]==mat[i][0]==mat[i+1][0] and mat[i-1][0]=="#":
                arr[i][0]="#"
                chk[i][0],chk[i-1][0],chk[i+1][0]=1,1,1
elif h==1:
    for i in range(w):
        if i==0:
            if mat[0][i]==mat[0][i+1]=="#":
                arr[0][i]="#"
                chk[0][i]=1
                chk[0][i+1]=1
        elif i==w-1:
            if mat[0][i]==mat[0][i-1]=="#":
                arr[0][i]="#"
                chk[0][i]=1
                chk[0][i-1]=1
        else:
            if mat[0][i]==mat[0][i-1]==mat[0][i+1] and mat[0][i]=="#":
                arr[0][i]="#"
                chk[0][i],chk[0][i-1],chk[0][i+1]=1,1,1      

else:

    for i in range(h):
        for j in range(w):
            if [i,j]==[0,0]:
                if mat[0][0]=="#" and mat[0][1]=="#" and mat[1][0]=="#" and mat[1][1]=="#":
                    arr[0][0]="#"
                    chk[0][0]=1
                    chk[0][1]=1
                    chk[1][0]=1
                    chk[1][1]=1
            elif [i,j]==[h-1,w-1]:
                if mat[h-1][w-1]=="#" and mat[h-2][w-1]=="#" and mat[h-1][w-2]=="#" and mat[h-2][w-2]=="#":
                    arr[i][j]="#"
                    chk[h-1][w-1]=1
                    chk[h-1][w-2]=1
                    chk[h-2][w-1]=1
                    chk[h-2][w-2]=1
            elif [i,j]==[0,w-1]:
                if mat[0][w-1]=="#" and mat[1][w-1]=="#" and mat[0][w-2]=="#" and mat[1][w-2]=="#":
                    arr[i][j]="#"
                    chk[0][w-1]=1
                    chk[0][w-2]=1
                    chk[1][w-1]=1
                    chk[1][w-2]=1
            elif [i,j]==[h-1,0]:
                if mat[h-1][0]=="#" and mat[h-2][0]=="#" and mat[h-1][1]=="#" and mat[h-2][1]=="#":
                    arr[i][j]="#"
                    chk[h-1][0]=1
                    chk[h-1][1]=1
                    chk[h-2][0]=1
                    chk[h-2][1]=1

            elif j==0:
                if mat[i][j]=="#" and mat[i-1][j]=="#" and mat[i+1][j]=="#" and mat[i][j+1]=="#" and mat[i+1][j+1]=="#" and mat[i-1][j+1]=="#":
                    chk[i][j],chk[i-1][j],chk[i+1][j],chk[i-1][j+1],chk[i][j+1],chk[i+1][j+1]=1,1,1,1,1,1
                    arr[i][j]="#"

            elif j==w-1:
                if mat[i][j]=="#" and mat[i-1][j]=="#" and mat[i+1][j]=="#" and mat[i][j-1]=="#" and mat[i+1][j-1]=="#" and mat[i-1][j-1]=="#":
                    chk[i][j],chk[i-1][j],chk[i+1][j],chk[i-1][j-1],chk[i][j-1],chk[i+1][j-1]=1,1,1,1,1,1
                    arr[i][j]="#"
            elif i==0:
                if mat[i][j]=="#" and mat[i][j-1]=="#" and mat[i][j+1]=="#" and mat[i+1][j]=="#" and mat[i+1][j-1]=="#" and mat[i+1][j+1]=="#":
                    chk[i][j-1],chk[i][j],chk[i][j+1],chk[i+1][j-1],chk[i+1][j],chk[i+1][j+1]=1,1,1,1,1,1
                    arr[i][j]="#"
            elif i==h-1:
                if mat[i][j]=="#" and mat[i][j-1]=="#" and mat[i][j+1]=="#" and mat[i-1][j]=="#" and mat[i-1][j-1]=="#" and mat[i-1][j+1]=="#":
                    chk[i][j-1],chk[i][j],chk[i][j+1],chk[i-1][j-1],chk[i-1][j],chk[i-1][j+1]=1,1,1,1,1,1
                    arr[i][j]="#"

            else:
                if mat[i][j]=="#" and mat[i][j-1]=="#" and mat[i][j+1]=="#" and mat[i-1][j]=="#" and mat[i-1][j-1]=="#" and mat[i-1][j+1]=="#":
                    if mat[i+1][j]=="#" and mat[i+1][j-1]=="#" and mat[i+1][j+1]=="#":
                        chk[i][j-1],chk[i][j],chk[i][j+1],chk[i-1][j-1],chk[i-1][j],chk[i-1][j+1],chk[i+1][j-1],chk[i+1][j],chk[i+1][j+1]=1,1,1,1,1,1,1,1,1
                        arr[i][j]="#"
cnt=0
for i in range(h):
    for j in range(w):
        if mat[i][j]=="#":
            cnt+=1
ans=0

for i in range(h):
    ans+=sum(chk[i])

if cnt==ans:
    print("possible")
    for i in range(h):
        print("".join(arr[i]))
else:
    print("impossible")

                

