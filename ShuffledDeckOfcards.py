#from itertools import*
#print ''.join(map(str,list(product('acbd','123456789abde'))))
l=lambda x,y:map(unichr,[int('1F0'+a+b,16)for a in x for b in y])
print l('ABCD','123456789ABDE')
