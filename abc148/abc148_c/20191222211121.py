a,b = map(int,input().split())
 
import fractions
 
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
 
