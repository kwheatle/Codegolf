a='abcdefghijklmnopqrstuvwxyz'
for c in range(51):
    i=25-abs(25-c)
    print a[:i]+a[i].upper()+a[i+1:]
