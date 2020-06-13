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
arr0=list(mss())
arr=[]

mat={"b":1,"c":1,"t":3,"j":3,"l":5,"v":5,"p":7,"m":7,"n":9,"g":9,"d":2,"w":2,"f":4,"q":4,"s":6,"x":6,"h":8,"k":8,"z":0,"r":0}
chk=["a","e","i","o","u","y",".",","]

for i in arr0:
    tmp=[]
    for j in list(i):
        j=j.lower()
        
        if j not in chk:
            tmp.append(mat[j])
    
    if len(tmp)&gt;0:
        arr.append("".join(list(map(str,tmp))))

print(*arr)



