n = int(input())
arr = list(map(int, input().split()))

#arr：最小公倍数の対象とする配列
MOD = 10**9 + 7
def lcm(arr):
    primes = {}
    for val in arr:
        p = 2
        while p * p &lt;= val:
            if val % p == 0:
                cnt = 0
                while val % p == 0:
                    cnt += 1
                    val //= p
                if p not in primes:
                    primes[p] = cnt
                else:
                    primes[p] = max(cnt, primes[p])
            p += 1
     
        if val != 1:
            if val not in primes:
                primes[val] = 1
    lcma = 1
    for p in primes:
        lcma = lcma * pow(p, primes[p], MOD) 
    return lcma

b = lcm(arr)

ans=0
for i in range(n):
    ans+= b*pow(arr[i],MOD-2,MOD)

