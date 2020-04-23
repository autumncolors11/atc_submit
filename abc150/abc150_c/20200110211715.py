n=int(input())

import itertools
ans =[]
for i in itertools.permutations(range(1,n+1)):
    ans.append(list(i))
    

p = list(map(int,input().split()))
q = list(map(int,input().split()))

x = ans.index(p)+1
y = ans.index(q)+1

if x -y &gt;=0:
    print(x-y)
elif x-y &lt; 0:
    print(y-x)
    
