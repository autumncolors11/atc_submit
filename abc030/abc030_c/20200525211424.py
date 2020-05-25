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

n,m=mii()
x,y=mii()

arra=limii()
arrb=limii()

cnt=0
i=0
j=0
chk=False
while i&lt;=n-1 and j&lt;=m-1:
    if chk:
        if arrb[j]+y&lt;=arra[i] and i&lt;=n-1 and j&lt;=m-1:
            chk=False
            j+=1
        else:
            i+=1
            
    
    else:
        if arra[i]+x&lt;=arrb[j] and i&lt;=n-1 and j&lt;=m-1:
            cnt+=1
            chk=True
            i+=1
        else:
            j+=1
    #print(i,j,cnt)
print(cnt)

