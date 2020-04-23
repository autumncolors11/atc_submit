def my_index(l, x, default=False):
    if x in l:
        return int(l.index(x))+1
    else:
        return default
 
ans = []
 
num = int(input())
 
for i in range(1,50001):
    ans.append(int(i*1.08))
 
