import fractions
from functools import reduce


def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

n,x = map(int,input().split())

arr = list(map(int,input().split()))

arr1 = [(i-x if i-x&gt;=0 else x-i) for i in arr]

print(gcd(*arr1))
