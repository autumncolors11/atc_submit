from itertools import product
s = input()
ans = "0"
#opで+の候補生成
for op in product(["-", "+"], repeat=len(s)-1):
    
    op = list(op)
    op.append("")
    #op=('', '+')の場合，1+""+2+"+"+5になる
    if eval(''.join( a + b for a, b in zip(s, op))) ==7:
        print(''.join( a + b for a, b in zip(s, op))+"=7")
        exit()
