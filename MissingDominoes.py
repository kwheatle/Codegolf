n='0123456'
l=lambda s,t=[a+b for a in n for b in n if a<=b]:[m for m in t if m not in s]
print l('00 10 11 20 21 22 30 31 32 33 40 41 42 43 44 50 51 52 53 54 55 60 61 62 63 64 65 66'.split())
