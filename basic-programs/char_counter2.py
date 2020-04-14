def main():
	s = input()
	x = {}
	for character in s:
		x[character] = s.count(character)
	i = 0
	max = 0
	sMax = 0
	maxCh = ''
	sMaxCh = ''
	for k,v in x.items():
		if max < v:
			sMax = max
			max = v
			sMaxCh = maxCh
			maxCh = k
		elif sMax < v:
			sMax = v
			sMaxCh = k
	if sMax is 0:
		print('(\''+maxCh+'\',',str(max)+')',end = "")
	else:
		print('(\''+maxCh+'\',',str(max)+')','(\''+sMaxCh+'\',',str(sMax)+')',end = "")

main()
'''
hello java
('l', 2) ('a', 2)
'''