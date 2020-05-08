import sys
sys.setrecursionlimit(10**6)

from collections import Counter,defaultdict,deque

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
s=Counter(list(ss()))
arr=Counter(list(ss()))

chk=True
ans=0
while chk:
    cnt=0
    for i,j in arr.items():
        if s[i]&gt;0:
            s[i]-=j
            if s[i]&lt;0:
                s[i]=0
        if s[i]==0:
            cnt+=1
    if cnt==len(list(arr.keys())):
        chk=False
    ans+=1

if sum(list(s.values()))==0:
    print(ans)
else:
    print(-1)
