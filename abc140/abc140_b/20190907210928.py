num = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

count = 0

for i in range(num):
    count += b[a[i]-1]
    
    if i &gt; 0 and a[i-1] + 1 == a[i]:
        count += c[a[i]-2]

