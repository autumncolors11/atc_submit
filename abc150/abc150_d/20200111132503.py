n,m =map(int,input().split())

a =  sorted([int(x)//2 for x in input().split()],reverse=True)

import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

import math

lcm1 = 1
for i in a:
    lcm1 = lcm(lcm1, i)
    if((lcm1//i)%2==0):
        print(0)
        exit()

print(math.ceil((m//lcm1)/2))
