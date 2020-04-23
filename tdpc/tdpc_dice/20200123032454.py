n,d=map(int,input().split())
 
 
# nに出る目を入れる → 第1引数に2,3,5で素因数分解 第2引数に2,3,5の倍数のどれでもない場合を入れる
def fact(n,d):
    chk=True
    arr = [0]*3
    for i,j in enumerate([2,3,5]):
        cnt=0
        while d%j==0:
            d=d//j
            cnt+=1
        arr[i]=cnt
    if d!=1:
        chk=False

    return arr,chk

arr,chk = fact(n,d)
if chk==False:
    print(0)
    exit()
ans=0
 
# 5 3 2 の順
mat =[[[[0]*(arr[2]+1) for _ in range(arr[1]+1)] for _ in range(arr[0]+1)] for _ in range(n+1)]
mat[0][0][0][0]=1
for i in range(n):
    for e2 in range(arr[0]+1):
        for e3 in range(arr[1]+1):
            for e5 in range(arr[2]+1):
                mat[i+1][e2][e3][e5]+=mat[i][e2][e3][e5]/6
                mat[i+1][min(arr[0],e2+1)][e3][e5]+=mat[i][e2][e3][e5]/6
                mat[i+1][e2][min(arr[1],e3+1)][e5]+=mat[i][e2][e3][e5]/6
                mat[i+1][e2][e3][min(arr[2],e5+1)]+=mat[i][e2][e3][e5]/6       
                mat[i+1][min(arr[0],e2+2)][e3][e5]+=mat[i][e2][e3][e5]/6
                mat[i+1][min(arr[0],e2+1)][min(arr[1],e3+1)][e5]+=mat[i][e2][e3][e5]/6
 
 
