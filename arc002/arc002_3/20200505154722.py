import sys
sys.setrecursionlimit(10**6)

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
arr=list(ss())
ans=10**100
#["A","B","X","Y"]
for p in ["A","B","X","Y"]:
    for q in ["A","B","X","Y"]:
        for r in ["A","B","X","Y"]:
            for s in ["A","B","X","Y"]:
                if p+q==r+s:
                    continue
                chk=0
                mat=[0]*n

                for i in range(n-1):
                    if arr[i]+arr[i+1]==p+q and mat[i]==0 and mat[i+1]==0:
                        mat[i]=1
                        mat[i+1]=1
                        chk+=1
                    elif arr[i]+arr[i+1]==r+s and mat[i]==0 and mat[i+1]==0:
                        mat[i]=1
                        mat[i+1]=1
                        chk+=1
                    #print(mat)
                ans=min(ans,n-chk)
print(ans)
