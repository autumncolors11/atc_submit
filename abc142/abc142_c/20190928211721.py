num = int(input())

arr = list(map(int,input().split()))
arr1 = []
for i in range(len(arr)):
    arr1.append((arr[i],i+1))

arr1.sort(key=lambda x: x[0])

arr2 = [i[1] for i in arr1]

print(*arr2)
