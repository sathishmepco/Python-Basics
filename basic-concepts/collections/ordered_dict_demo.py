from collections import OrderedDict
def main():
	d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
	new_dict = OrderedDict(sorted(d.items(),key=lambda t:t[0]))
	print('Dictionary sorted by key')
	print(new_dict)
	new_dict = OrderedDict(sorted(d.items(),key=lambda t:t[1]))
	print('Dictionary sorted by value')
	print(new_dict)
	new_dict = OrderedDict(sorted(d.items(),key=lambda t:len(t[0])))
	print('Dictionary sorted by length of the key')
	print(new_dict)
main()
'''
Dictionary sorted by key
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
Dictionary sorted by value
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
Dictionary sorted by length of the key
OrderedDict([('pear', 1), ('apple', 4), ('banana', 3), ('orange', 2)])
'''