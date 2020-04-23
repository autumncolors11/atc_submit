n = int(input())
s = input()

arr = []
arr.append(s[0])
for i in range(n-1):
    if s[i+1] != s[i]:
        arr.append(s[i+1])


c = len(arr)
print(c)
