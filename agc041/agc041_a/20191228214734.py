num,a,b = map(int,input().split())

if(b-a) %2 ==0:
    print((b-a)//2)

    #間隔が奇数の時
else:
    #aと右端の差
    p=num-a
    #bと左端の差
    q=b-1
    #aと左端の差
    r=a-1
    #bと右端の差
    s=num-b
    
    #もしbとaの差が3未満のとき
    if b-a &lt;3:
        p = min(b-1,num-a)
        print(p)
    
    else:
        z=r+1+(b-(r+1)-1)//2
        y=s+1+(num-(a+(s+1)))//2
        print(min(y,z))
