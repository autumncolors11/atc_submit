import sys
sys.setrecursionlimit(10**6)

 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]


#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

txa,tya,txb,tyb,t,v=mii()
n=ii()
minans=10**1000

for i in range(n):
    x,y=mii()
    minans=min(minans,pow((txa-x)**2 + (tya-y)**2,0.5)+ pow((txb-x)**2+(tyb-y)**2,0.5))

if minans &lt;=t*v:
    print("YES")
else:
    print("NO")











