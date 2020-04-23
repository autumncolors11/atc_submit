num = int(input())
arr = list(map(int,input().split()))

arr_inv = [1/i for i in arr]

print(1/sum(arr_inv))
