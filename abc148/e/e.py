n = int(input())

chk = False
chk1 = True
bis = 5
ans = 0
if (n % 2 ==1) or (n<10):
    print(0)

else:
    #while chk == False:
    #    if list(str(n))[-1] == "0":
    #        chk = True
    #    else:
    #        n -=2
            
    while n > bis:
        
        ans += n // (bis*2)
        bis = bis *5

        
        
    print(ans)