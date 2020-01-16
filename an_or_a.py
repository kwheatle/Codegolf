w = 'Zero One Two Three Four Five Six Seven Eight Nine'.lower().split()
v = 'a e i o u'.split()
n = input()
s = str(n)
if len(str(n)) == 2 and int(s[0]) == 1:
    if w[int(s[1])][0] in v:
        print('"an"')
    else:
        print('"a"')
else:
    if w[int(s[0])][0] in v:
        print('"an"')
    else:
        print('"a"')
