n = input()

for p in range(int(n)):

    s = list(input())
    
    lens=len(s)
    i=0
    ans=0
    while i &lt;= lens-4:
        #print(s[i:i+5])
        if s[i:i+5] == list("kyoto") or s[i:i+5]==list("tokyo"):
            ans+=1
            i+=5
        else:
            i+=1
    
    print(ans)

