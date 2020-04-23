tap,consent = map(int,input().split())

count = 1
n = 1
while count &lt; consent:
    count = n * tap - (n-1)
    n += 1

