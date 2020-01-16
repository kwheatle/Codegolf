from random import *
i=input()
s=shuffle
c=list('bcdfghjklmnpqrstvwxyz')
v=list('aeiou'*4+'e')
s(c)
s(v)
r=int(random()*round(i/2,len(`i`)-1)-1)
o=map(''.join,zip(c,v))
o[r]+='yh'[r%2]*(i%2)
print''.join(o)[:i].title()
