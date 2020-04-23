n = int(input())

import itertools

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))


ptr = list(itertools.permutations(arr, n))


dis = 0

for i in range(len(ptr)):
    for j in range(n-1):
        dis +=((ptr[i][j][1]-ptr[i][j+1][1]) **2 + (ptr[i][j][0]-ptr[i][j+1][0])**2)**0.5
        
print(dis/len(ptr))


    
