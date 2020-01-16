def f(i,n):
    l=list(i.replace('^','**'))
    [l.insert(c,'*')for c in range(1,len(l))if l[c-1]in"0123456789"and l[c]=='x']
    print eval(''.join(l).replace('x',`n`))
    
f("3x^3-5x^2+2x-10", 5)
