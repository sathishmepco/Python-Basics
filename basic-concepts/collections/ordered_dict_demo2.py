from collections import OrderedDict
def main():
	issues = {
		1: {'title': 'Title 1','level': 'low'},
		2: {'title': 'Title 2','level': 'medium'},
		3: {'title': 'Title 3','level': 'high'},
		4: {'title': 'Title 4','level': 'low'},
		5: {'title': 'Title 5','level': 'medium'},
		6: {'title': 'Title 6','level': 'high'}
	}
	priorities = {
    'low': 1,
    'medium': 2,
    'high': 3
	}
	
	x = OrderedDict(sorted(issues.items(), key = lambda item: priorities[item[1]['level']]))
	for key, value in x.items():
		print(f"{key}, {value}")
main()

'''
1, {'title': 'Title 1', 'level': 'low'}
4, {'title': 'Title 4', 'level': 'low'}
2, {'title': 'Title 2', 'level': 'medium'}
5, {'title': 'Title 5', 'level': 'medium'}
3, {'title': 'Title 3', 'level': 'high'}
6, {'title': 'Title 6', 'level': 'high'}
'''