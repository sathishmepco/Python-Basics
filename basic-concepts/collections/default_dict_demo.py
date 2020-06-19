from collections import defaultdict
def main():
	print('DefaultDictionary')
	s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
	d = defaultdict(list)
	for k, v in s:
		d[k].append(v)
	print(d.items())
	
	d = {}
	for k, v in s:
		d.setdefault(k, []).append(v)
	print(d)
	
	s = 'mississippi'
	d = defaultdict(int)
	for k in s:
		d[k] += 1
	print(d)
	maxV = 0
	for k,v in d.items():
		if v > maxV:
			maxV = v
			maxC = k
	print(maxC,maxV)
main()
'''
DefaultDictionary
dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
i 4
'''