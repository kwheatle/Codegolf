i=input
n=0
for x in range(i(),i()+1):n+=`bin(x)`.count('1')
print n
