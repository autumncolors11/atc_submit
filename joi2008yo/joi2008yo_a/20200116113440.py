n0 = int(input())

n=1000-n0

ans =0

if n &gt;=500:
    ans+=1
    n-=500


if n//100 &gt;=1:
    ans+=(n//100)
    n-=100*(n//100)


if n//50 &gt;=1:
    ans+=(n//50)
    n-=50*(n//50)
    

if n//10 &gt;=1:
    ans+=(n//10)
    n-=10*(n//10)
if n//5 &gt;=1:
    ans+=(n//5)
    n-=5*(n//5)  

ans+=(n)
n-=1*(n)
    

print(ans)

