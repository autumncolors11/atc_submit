a,b,k = map(int,input().split())
 
if a  &lt;= k:
    k = k-a
    a = 0
    b = b-k
    if b &lt; 0:
        b=0
else:
    a = a-k
    

print(str(a)+" "+str(b))
