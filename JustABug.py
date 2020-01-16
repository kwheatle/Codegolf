#s=' '
#for n in range(17):
#    x=abs(8-n)
#    print'1'+s*x+'2'+s*x+'3'+s*x+'4'+s*x+'5'+s*x+'6'+s*x+'7'+s*x+'8'+s*x+'9'+s*x+'0'
for n in range(17):print(' '*abs(8-n)).join('1234567890')
