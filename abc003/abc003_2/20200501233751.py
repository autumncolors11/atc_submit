import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log

def ss(): return sys.stdin.readline().rstrip() #input()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

s=list(ss())
t=list(ss())

lens=len(s)

arr=["a","t","c","o","d","e","r"]
chk=0
for i in range(lens):
    if s[i]==t[i]:
        chk+=1
    elif s[i]=="@" and t[i]=="@":
        chk+=1
    elif s[i]=="@" and t[i] in arr:
        chk+=1
    elif s[i] in arr and t[i]=="@":
        chk+=1

if chk==lens:
    print("You can win")
else:
    print("You will lose")


