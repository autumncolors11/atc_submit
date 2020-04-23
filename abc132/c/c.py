num = int(input())

arr0 = list(map(int,input().split()))

arr = sorted(arr0)

a0 = arr[num//2]
a1 = arr[num//2 -1]

if a0 == a1:
    print(0)

else:
    print(a0-a1)
