d,g = map(int,input().split())
    
arr = []
    
for i in range(d):
    arr.append(list(map(int,input().split())))
    
from itertools import product
from math import ceil
    
ans = 1e09
#各問題を選択するしないを01表記
for c in product([0,1],repeat=d):
    #print(c)
    #スコア
    score = 0
    #解く問題数
    num = 0
    
    ind = 0
    #まず01表記を全て
    for i in range(d):
        #もし01表記で1の場合，完答した場合の点数，問題数を加算
        if c[i] == 1:
            score += arr[i][0]*100*(i+1) + arr[i][1]
            num += arr[i][0]
        #0だった場合，
        else:
            ind = max(i,ind)
    #目標よりも点数が大きかった場合，小さい方を答えにする
    if g - score &lt;= 0:
        ans = min(ans,num)
        #print(0,ans,num,score,ind)
    #もし目標が，点数とind番目の問題を完答してない場合との和より小さい時
    elif g - score &lt;= (arr[ind][0]-1)*100*(ind+1):
        num += ceil((g-score)/(100*(ind+1)))
        ans = min(ans,num)
        #print(1,ans,num,score,ind)
    else:
        pass
#print(2,num,score,ind)
print(ans)
