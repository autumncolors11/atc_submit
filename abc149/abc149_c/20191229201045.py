x = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
a = False
while a ==False:
    a = is_prime(x)
    if a == False:
        x+=1

print(x)
