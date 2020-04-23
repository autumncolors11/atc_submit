asize,bwater,cwater = map(int,input().split())

if bwater + cwater &gt;= asize:
    cnokori = cwater - (asize - bwater)
    print(cnokori)

else:
