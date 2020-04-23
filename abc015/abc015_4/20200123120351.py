w=int(input())
n,k=map(int,input().split())

arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

mat=[[[0]*(w+1) for _ in range(k+1)] for _ in range(n+1)]

#W:全体の幅 N：枚数制約 K：重要度 A:スクショの幅 B：スクショの重要度
#全体の幅と枚数を制約として可能な限り重要度の合計を高くする

for num in range(1,n+1):
    for kn in range(1,k+1):
        for wi in range(1,w+1):
            
            mat[num][kn][wi] = max(mat[num][kn][wi],mat[num-1][kn][wi])
    
            if wi &gt;= arr[num-1][0]:
                mat[num][kn][wi] = max(mat[num-1][kn-1][wi-arr[num-1][0]]+arr[num-1][1],mat[num][kn][wi])

print(mat[-1][-1][-1])
