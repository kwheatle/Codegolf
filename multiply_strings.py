f = raw_input()
s = raw_input()
i = [f, s]
o=''
c=0
for x in min(i, key=len):
    o += unichr(max(ord(x), ord(max(i, key=len)[c])))
    c+=1
print(o)
