"""
全体の流れ：
bit全探索を使う

1. 全通りで嘘か正直か仮定する bit全探索リストをつくる
2. 仮定が矛盾するかどうかを1：True 0：Falseで判断する
"""
n = int(input())
arr = []
for i in range(n):
    na = int(input())
    ar0 = []
    for j in range(na):
        x,y = map(int,input().split())
        ar0.append([x-1,y])
    arr.append(ar0)

print(arr)

#1：正直者
#0：嘘つき
#最大数
ans=0
#全探索
for i in range(1<<n):
    #候補作成，for iによって全候補作成
    c_list=[]
    for j in range(n):
        c_list.append((i>>j)%2)

    #作成した候補が矛盾しないかどうか
    check=1
    for j in range(n):
        #1ならばTrue j番目の人が正直であるとする
        if c_list[j]:
            
            #正直であるとしたj番目の人の全ての発言で確認
            for z in arr[j]:
                
                #発言の対象になる人と仮定したものが矛盾しないかどうか確認，矛盾すると0
                if c_list[z[0]]!=z[1]:
                    check=0
                    print(c_list,z)
    if check:
        ans=max(ans,sum(c_list))
print(ans)

