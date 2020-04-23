n,k,s=map(int,input().split())

arr = []

for i in range(k):
    arr.append(str(s))

for j in range(n-k):
    if s+1 &gt;= 10*9 +1:
        arr.append(str(s-1))
    else:
        arr.append(str(s+1))
#print(arr)
print(" ".join(arr))
