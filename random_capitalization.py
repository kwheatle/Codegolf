import random
i=list(raw_input())
for x in xrange(len(i)):
    n=random.randint(0,len(i))
    if n==x:i[x]=i[x].upper()
print str(i)
