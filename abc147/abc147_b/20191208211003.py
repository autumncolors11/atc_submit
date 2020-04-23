arr = list(input())

la = len(arr)

if la %2 ==0:
    a1 = arr[:la//2]
    a2 = arr[la//2:]
    a2.reverse()


    cnt = 0
    for i in range(la//2):
        if a1[i]  != a2[i]:
            cnt +=1

else:
    a1 = arr[:la//2]
    a2 = arr[la//2:]
    a2.reverse()
    cnt = 0
    for i in range(la//2):
        if a1[i]  != a2[i]:
            cnt +=1

