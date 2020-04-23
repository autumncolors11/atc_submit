num = int(input())

alice = 0
bob = 0
cards = list(map(int,input().split()))
for i in range(1,num+1):
    
    if i % 2 == 1:
        alice += max(cards)
        cards.remove(max(cards))
    else:
        bob += max(cards)
        cards.remove(max(cards))

ans = alice - bob
print(ans)
