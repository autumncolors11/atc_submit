
import itertools

n, m = list(map(int, input().split()))
kokkai = [[_] for _ in range(n)]
for i in range(m):
    x, y = list(map(int, input().split()))
    kokkai[x - 1].append(y - 1)
    kokkai[y - 1].append(x - 1)
ans = 1
#print(kokkai)
for i in range(2, n + 1):
    patan = list(itertools.combinations(range(n), i))
    #print(patan)
    for k in patan:
        hantei = 1
        k = list(k)
        for l in k:
            for x in k:
                
                if x in kokkai[l]:
                   # print(l,x,kokkai[l])
                    continue
                else:
                    hantei = 0
                    break
        if hantei:
            ans = len(k)
print(ans)

