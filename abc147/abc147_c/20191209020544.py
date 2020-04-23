n = int(input())
arr = []
for i in range(n):
    na = int(input())
    ar0 = []
    for j in range(na):
        x,y = map(int,input().split())
        ar0.append([x-1,y])
    arr.append(ar0)


#1：正直者
#0：嘘つき
#最大数
ans=0
#全探索
for i in range(1&lt;&lt;n):
    #全候補
    c_list=[]
    for j in range(n):
        c_list.append((i&gt;&gt;j)%2)

    check=1
    for j in range(n):
        #1ならばTrue
        if c_list[j]:
            
            for z in arr[j]:
                
                if c_list[z[0]]!=z[1]:
                    check=0
    if check:
        ans=max(ans,sum(c_list))
print(ans)
