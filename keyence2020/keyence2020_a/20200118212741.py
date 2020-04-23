h=int(input())
w=int(input())
n=int(input())

ans = 0
cnt=0
a = max(h,w)
while ans &lt; n:
    ans += a
    cnt+=1
    
print(cnt)

