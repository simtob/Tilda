
s = input()
while s is not None:
	parts = s.split()
	a = int(parts[0])
	b = int(parts[1])
	print(abs(a-b))
	try:
		s = input()
	except:
		break