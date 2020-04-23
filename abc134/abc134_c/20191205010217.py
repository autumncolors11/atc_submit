from collections import deque

num = int(input())

arr = []

for i in range(num):
    arr.append(int(input()))

arr0 = sorted(arr,reverse=True)
arr00 = arr0[0]
arr01 = arr0[1]

for i in range(num):
    if arr[i] != arr00:
        print(arr00)
    else:
