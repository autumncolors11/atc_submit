N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
 
from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)
 
a = 1
for i in range(N):
    a = lcm(a, A[i])
 
ans = 0
for i in range(N):
    ans += a * pow(A[i], mod-2, mod)
 
print(ans % mod)
