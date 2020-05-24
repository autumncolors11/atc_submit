import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log

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

c=ii()

t1=[]
t2=[]
t3=[]

for i in range(c):
    n,m,l=mii()
    arr=sorted([n,m,l])
    t1.append(arr[0])
    t2.append(arr[1])
    t3.append(arr[2])

print(max(t1)*max(t2)*max(t3))


