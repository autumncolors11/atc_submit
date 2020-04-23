n,m = map(int,input().split())

#赤フラグ 玉の個数
arr = [1 for _ in range(n)]
arr1 = [False for _ in range(n)]
arr1[0]=True
ch1 = True

for i in range(m):
    x,y = map(int,input().split())
    x = x-1
    y = y-1
    if ch1 == True and x == 0:
        ch1 = None
        arr[y] +=1
        arr1[y] = True
        arr[x] -=1
        if arr[x] == 0:
            arr1[x] = False
        continue
    
    arr[y] +=1
    arr[x] -=1
    if ch1 == None and arr1[x] == True:
        
        arr1[y] = True
        
    if ch1 == None and arr[x] == 0:
        arr1[x] = False

cnt=0
for i in range(n):
    if arr1[i] == True:
        cnt +=1   
print(cnt)


    
