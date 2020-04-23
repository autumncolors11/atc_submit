n = int(input())

if n &lt; 10:
    print(n)

elif n &lt; 100:
    print(9)
elif n &lt; 1000:
    print(9 + n-100+1)
elif n &lt; 10000:
    print(9+999-100+1)
elif n &lt; 100000:
    print(9+999-100+1 +n-10000+1)
elif n == 100000:
