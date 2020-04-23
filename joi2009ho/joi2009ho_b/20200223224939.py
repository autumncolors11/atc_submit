import sys
sys.setrecursionlimit(10**6)

from bisect import bisect_left,bisect_right

#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]


#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

#for i in itertools.product([0,1], repeat=n)

d=ii()
n=ii()
m=ii()
arrd=[0]+lin(n-1)+[d]
arrk=lin(m)
arrd.sort()

ans=0
for i in arrk:
    a = bisect_left(arrd,i)
    if a&gt;0:
        ans+=min(abs(i-arrd[a-1]),abs(i-arrd[a]))

print(ans)

