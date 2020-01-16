#i=list(raw_input().replace('y','1').replace('n','0'))
#t=[i[::2], i[1::2]]
#if len(t[0])>len(t[1]): t[1]+='1'
#print t
#while len(t)
#for n in xrange(len(t[0])):
#    t[n%2][n] = int(t[0][n]==t[1][n])
#    del t[n%2<1][n]
#print t

s='yynynynny'
e = lambda s:'yn'[s.count('n')%2]
print(e(s))
