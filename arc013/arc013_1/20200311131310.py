import sys
sys.setrecursionlimit(10**6)

 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

n,m,l=mii()
p,q,r=mii()


a0,b0,c0 = n//p,m//q,l//r
a1,b1,c1 = n//q,m//p,l//r
a2,b2,c2 = n//r,m//p,l//q
a3,b3,c3 = n//p,m//r,l//q
a4,b4,c4 = n//r,m//q,l//p
a5,b5,c5 = n//q,m//r,l//p


aa0 = a0*b0*c0
aa1 = a1*b1*c1
aa2=a2*b2*c2
aa3=a3*b3*c3
aa4=a4*b4*c4
aa5=a5*b5*c5

print(max(aa0,aa1,aa2,aa3,aa4,aa5))

