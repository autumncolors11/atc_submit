a=list(input())

if a==list("a"):
    print(-1)

elif a[-1] !="a":
    a[-1] = chr(ord(a[-1])-1)
    print("".join(a))
else:
    b=a[:-1]
    print("".join(b))

    

