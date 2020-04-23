n = int(input())

def fact(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

if n == 1:
    print(1)
    exit()

arr = [0 for _ in range(1001)]

for i in range(1,n+1):

    for j in range(len(fact(i))):
        arr[fact(i)[j][0]] += fact(i)[j][1]

ans = 1
for i in range(2,1001):
    if arr[i] &gt; 0:
        ans *= arr[i] +1
    if ans &gt; 1000000007:
        ans % 1000000007

print(ans % 1000000007)
