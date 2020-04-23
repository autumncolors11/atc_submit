n = int(input())

s = input()

if n %2 ==1:
    print("No")

else:
    if s[0:int(n/2)] == s[int(n/2):n]:
        print("Yes")
        
    else:
        print("No")
