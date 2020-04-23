n = int(input())

s0,t0 = map(str,input().split())
s = list(s0)
t = list(t0)
ans = []

for i in range(n):
    ans.append(s[i])
    ans.append(t[i])
    
print("".join(ans))
