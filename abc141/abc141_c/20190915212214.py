num,k,q = map(int,input().split())

arr = [0]*num


for i in range(q):
    a = int(input())
    arr[a-1] +=1

arr = [i-(q-k) for i in arr]

for i in range(len(arr)):
    if arr[i] &gt; 0:
        print("Yes")
    else:
        print("No")
