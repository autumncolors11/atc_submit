import numpy as np

num, k = map(int,input().split())

count = 0.

for i in range(1,num+1):
    if i &lt;= k-1:
        times = np.log2(k/i)
        if times != int(times):
            times = int(times) +1
        else:
            times = int(times)
        count += (1/num) * (1/2)**times
    elif i &gt;= k:
        count += 1/num
print(count)


