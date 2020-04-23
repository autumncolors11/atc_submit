num = int(input())
figx =0
figy =0

count = 0
for i in range(num):
    time,x,y = map(int,input().split())
    distance = x + y - figx - figy
    if distance &lt;= time and (time % 2 == distance %2):
        count += 1
    
    x=figx
    y=figy
        
if count == num:
    print("Yes")
else:
    print("No")
