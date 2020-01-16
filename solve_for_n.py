import re

def f(s):
    return "" if not s else f(s[2:]) + s[:2]
while 1:
    i = raw_input()
    t = 0
    a = []
    o = []
    m = 1
    re.split('[+-=]', i)
    for l in i:
        if l == ' ': continue
        a+=l
    n = (a.index('N')-1)
    for l in a:
        if l == '+':
            l = '-'
        elif l == '-':
            l = '+'
        if l == '=':
            continue
        if t == n:
            m = l
            del a[n]
            n = -1
            continue
        if l == 'N':
            continue
        t+=1
        o+=l

    O = (f(str(o).replace('[', '').replace(']','').replace(',', '').replace("'", '').replace(' ', '')))
    print("N = " + str(round(eval(O) / int(m))))
