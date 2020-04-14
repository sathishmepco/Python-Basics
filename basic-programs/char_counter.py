from collections import Counter 
import collections

def main():
	str = input()
	x = {}
	for character in str:
		x[character] = str.count(character);
	print(x)
	for k,v in x.items():
		print(k,v)
	print(tuple(([x for x in x.keys()][i], [x for x in x.values()][i]) for i in range(len(x)))) 
	for i in range(len(x)):
		if i is len(x)-1 :
			print(('\''+[x for x in x.keys()][i]+'\'', [x for x in x.values()][i]),end="")
		else:
			print(('\''+[x for x in x.keys()][i]+'\'', [x for x in x.values()][i]),end=" ")
	abc = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
	print()
	print(abc)
	d = {'one':1,'three':3,'five':5,'two':2,'four':4}
	a = sorted(d.items(), key=lambda c: c[1])    
	a.reverse()
	for i in range(len(a)):
		print(a[i])	
    
main()
'''
asdasddds
('d', 4) ('s', 3)
sathish
{'s': 2, 'a': 1, 't': 1, 'h': 2, 'i': 1}
s 2
a 1
t 1
h 2
i 1
(('s', 2), ('a', 1), ('t', 1), ('h', 2), ('i', 1))
('s', 2) ('a', 1) ('t', 1) ('h', 2) ('i', 1)

{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

sorted_dict = collections.OrderedDict(sorted_x)

'''