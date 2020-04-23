arr = list(input())
ans = 0
ct= 0
cs= 0
for i in range(len(arr)):
    if arr[i] == "S":
        cs +=1
        
    
    else:
        
        if cs >0:
            ans +=1
            cs -=1
           

print(len(arr)-2*ans)
