num = int(input())
p = list(map(int,input().split()))

dp = [0]*(sum(p)+1)
dp[0]=1

for i in p:
    temp=dp[:]
    for x,y in enumerate(dp):
        
        if y and x+i &lt;=sum(p)+1:
            temp[x+i]=1
    dp[i]=1
    dp=temp  

print(dp.count(1))
