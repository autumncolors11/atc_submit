import math

a,b,x = map(int,input().split())

if (a ==1 and b==1 and x ==1) or (a*a*b == x):
    print(0)    

elif x &lt; a*a*b/2:
    print(90-math.degrees(math.atan(2*x/(a * (b**2)))))
    
else:
    print(90-math.degrees(math.atan(a**3 / (2*(a*a*b-x)))))
