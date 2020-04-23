n = int(input())

arr=[]

for i in range(n):
    x,l = map(int,input().split())
    arr.append([x,l,x-l,x+l])
arr.sort(key=lambda x: x[3])

#print(arr)

ans = 0
start=-100000
fin=-1000

start = arr[0][2]
fin=arr[0][3]

for a,b,c,d in arr[1:]:
    if c &lt; fin:
        ans+=1
        pass
    elif c &gt;= fin:
        start=c
        fin = d

print(n-ans)
