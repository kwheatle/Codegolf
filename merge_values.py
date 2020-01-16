while 1:
	f = input()
	s = input()
	fn0 = (f <> 0)
	sn0 = (s <> 0)
	if fn0 and sn0 and f == s:
		print(f)
		continue
	if fn0 and sn0 and f <> s:
		print('0')
		continue
	if fn0 != sn0:
		if fn0:
			print(f)
		if sn0:
			print(s)
		continue
	if fn0 == sn0 and fn0 == False:
		print(f)

