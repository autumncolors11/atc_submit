a,b=map(str,input().split())

c,d = "".join([a]*int(b)),"".join([b]*int(a))

if c &lt;= d:
    print(c)
else:
    print(d)
