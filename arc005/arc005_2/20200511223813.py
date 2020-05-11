import sys
sys.setrecursionlimit(10**6)

from copy import deepcopy

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
x,y,w=mss()
x,y=int(x)-1,int(y)-1

mat =[]
for i in range(10):
    s=list(ss())
    mat.append(s)


#R、L、U、D、RU、RD、LU、LD
direct = [[0,1],[0,-1],[-1,0],[1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
ans=[]

if w=="R":temp=deepcopy(direct[0])
elif w=="L":temp=deepcopy(direct[1])
elif w=="U":temp=deepcopy(direct[2])
elif w=="D":temp=deepcopy(direct[3])
elif w=="RU":temp=deepcopy(direct[4])
elif w=="RD":temp=deepcopy(direct[5])
elif w=="LU":temp=deepcopy(direct[6])
elif w=="LD":temp=deepcopy(direct[7])

for i in range(4):
    #print(ans,y,x,temp)
    ans.append(mat[y][x])



    if 0&lt;=x+temp[1]&lt;=8 and 0&lt;=y+temp[0]&lt;=8:

        x+=temp[1]
        y+=temp[0]
    elif (0&gt;x+temp[1] and 0&lt;=y+temp[0]&lt;=8) or (x+temp[1]&gt;8 and 0&lt;=y+temp[0]&lt;=8):
        temp[1]*=-1
        x+=temp[1]
        y+=temp[0]
    elif (0&lt;=x+temp[1]&lt;=8 and 0&gt;y+temp[0]) or (0&lt;=x+temp[1]&lt;=8 and y+temp[0]&gt;8):
        temp[0]*=-1
        x+=temp[1]
        y+=temp[0]
    else:
        temp[0]*=-1
        temp[1]*=-1
        x+=temp[1]
        y+=temp[0]
    
print("".join(ans))





