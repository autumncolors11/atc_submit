num = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
for i in range(num):
    if b[i] &gt;= a[i]:
        cp=a[i]
        count += a[i]
        a[i]=0
        b[i] -=cp
        if b[i] &gt;= a[i+1]:
            cp = a[i+1]
            count += cp
            a[i+1] = 0
        else:
            a[i+1] -=b[i]
            count += b[i]
    else:
        a[i] -=b[i]
        count += b[i]
print(count)
