import heapq as hq

num ,m =map(int,input().split())

arr = [-i for i in list(map(int,input().split()))]
hq.heapify(arr)

for i in range(m):
    hq.heappush(arr, -1*(-1*hq.heappop(arr)//2))

    
print(-1*sum(arr))
       
