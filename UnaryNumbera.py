i=input().split('0')
b=lambda x:x.count('1')if x else 0
print i
i=map(b,i)
print i
