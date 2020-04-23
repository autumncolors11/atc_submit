import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
mod = 10 ** 9 + 7
 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input
def ss(): return sys.stdin.readline().rstrip() #input()
def mss(): return sys.stdin.readline().rstrip()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

s=ss()
t=ss()
def lcs(str1, str2):
    '''文字列str1, str2の最長共通部分列(Lowest Common Subsequence, LCS)を求める
    計算量O(len(str1)*len(str2))  
    '''
    dp = [[0]*(len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
 
    '''復元を実行
    最長の長さを求めるなら return dp[len(str1)][len(str2)] をするとよい
    '''
    res = ''
    i, j = len(str1), len(str2)
    while i &gt; 0 and j &gt; 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            res = str1[i-1] + res
            i -= 1
            j -= 1
    return res
