n,k=map(int,input().split())
arr = input()

ans = 0
for i in range(n-1):
    if arr[i] == arr[i+1]:
        ans +=1

ans +=k*2

if ans&gt;n-1:
    ans = n-1

print(ans)
