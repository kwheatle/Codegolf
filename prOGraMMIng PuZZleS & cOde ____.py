import re
a='_ a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
s='_'
b=i=raw_input()
u=i[i.find(s):].count(s)
i=re.findall('.....?',i[:i.find(s)])
print i
for x, item in enumerate(i):
    t=''
    for y in i[x]:
        t+=str(int(y.isupper()))
        print a[int(int(t,base=2))+1]
    b=b.replace(s,a[int(int(t,base=2))+1],1)
print b

