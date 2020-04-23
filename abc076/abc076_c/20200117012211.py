s=list(input())
t=list(input())

s.reverse()
t.reverse()

snum=len(s)
tnum=len(t)
chk=False
for i in range(snum-tnum+1):
    #print(s[i:i+tnum])
    cnt=0
    for j in range(i,i+tnum):
        #print(s[j],t[j-i])
        if s[j]==t[j-i]:
            cnt+=1
        elif s[j] =="?":
            cnt+=1
        
    if cnt==tnum and chk==False:
        s[i:i+tnum]=t
        chk=True
    else:
        if s[i]=="?":
            s[i]="a"

for i in range(snum):
    if s[i]=="?":
        s[i]="a"

if chk==True:
    print("".join(reversed(s)))
else:
    print("UNRESTORABLE")
