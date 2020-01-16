i = raw_input()
o = ''
for x in i:
    if x == i[-1]:
        o += x
        for y in range(0, len(i)-1):
            o += ')'
    else:
        o += x + '('
print(o)
    
