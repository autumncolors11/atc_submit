import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log,sin,cos

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

n,l =mii()

mat=[ss() for _ in range(l)]
gg=ss()

if n==1:
    print(1)
    exit()

for i in range(n*2):
    if gg[i]=="o":
        goal=i
        break
#print(goal)

for i in range(l)[::-1]:
    if 0&lt;goal&lt;2*(n-1):
        if mat[i][goal+1]=="-":
            goal+=2
        elif mat[i][goal-1]=="-":
            goal-=2
    
    elif goal==0:
        if mat[i][goal+1]=="-":
            goal+=2
    else:
        if mat[i][goal-1]=="-":
            goal-=2
print(goal//2 +1)



