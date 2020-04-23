n=int(input())
S = input()
 
ans = 0
for i in range(1000):
    a, b, c = map(str, list(str(i).zfill(3)))
    mode = 'a'
    for j in S:
        if mode == 'a' and j == a:
            mode = 'b'
        elif mode == 'b' and j == b:
            mode = 'c'
        elif mode == 'c' and j == c:
            ans += 1
            break
