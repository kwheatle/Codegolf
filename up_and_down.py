from itertools import*
a=input()
#print [eval(x)<1 for x in map(''.join,combinations(['+'+x for x in map(str,input())],2)) if eval(x)<1]
print any(-n in a for n in a)
