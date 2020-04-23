a = int(input())

arr = []
for i in range(1,10):
    for j in range(1,10):
        arr.append(i*j)

b = arr.count(a)

if b &gt; 0:
    print("Yes")
else:
    print("No")
