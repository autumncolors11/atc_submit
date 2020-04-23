
a = int(input())

arr = []

for i in range(1,int(a**0.5)+1):
    b = a / i
    
    if a == int(b)*i:
        arr.append([int(i),int(b)])

arrb = [sum(arr[i]) for i in range(len(arr))]
print(min(arrb)-2)
