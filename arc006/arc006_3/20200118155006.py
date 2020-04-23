n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
    
#print(arr)

ans = [[100000000000]]

for i in range(n):
    chk = True
    p=0
    while chk:
        if min(ans[p]) &gt;= arr[i]:
           ans[p].append(arr[i])
           chk=False
          
        else:
            if p == len(ans)-1:
                ans.append([100000000000])
           
            p+=1

