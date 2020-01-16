i = raw_input()
U = ['Uppercase']
L = ['Lowercase']
C = [L,U]
for l in i:
    t = l.isupper()
    C[1*t].append(l*t + l*(t<1))
b = max(U, L, key=len)
print '%s %s' % ((len(b)-1)/float(len(i)), b[0])

