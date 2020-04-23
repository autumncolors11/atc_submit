s = input()

arr = list(s)

count = 0

for i in range(len(arr)):
    if i % 2 == 0:
        if arr[i] == "R" or arr[i] == "U" or arr[i] == "D":
            count +=1
    if i % 2 == 1:
        if arr[i] == "L" or arr[i] == "U" or arr[i] == "D":
            count +=1        

if count == len(arr):
    print("Yes")
else:
    print("No")
