#n,じゃんけん回数  k，ちょうど出せないk回前までの手
n,k = map(int,input().split())
#r,s,p：グー，ちょき，パーで勝ったときの点数
r,s,p = map(int,input().split())
#相手の手
arr = list(input())
point = 0
for x,y in enumerate(arr):
    if x+k &lt; n:
        if arr[x+k] == arr[x]:
            arr[x+k]=None

for i in arr:
    if i == "r":
        point+=p
    elif i =="s":
        point+=r
    elif i =="p":
        point+=s

print(point)
