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

arr=limss()
n=ii()
mat=[]
for j in range(n):
    a=list(ss())
    b=int("".join(a))
    for i in range(len(a)):
        a[i]=str(arr.index(a[i]))

    mat.append([int("".join(a)),b])

mat.sort(key=lambda x: x[0])
#print(" ")
for i in range(n):
    print(mat[i][1])





