from collections import Counter
def main():
    c = Counter()
    words =  ['red', 'blue', 'red', 'green', 'blue', 'blue']
    for word in words:
        c[word] += 1
    print(c)
    print('Most Common :: ')
    print(c.most_common(1))
	
    c = Counter('malayalam')
    print('From String :: malayalam')
    print(c.most_common())
    print('a occured :: ',c['a'])
    print('z occured :: ',c['z'])
	
    print('Counter to List (reverse)')
    l = list(c.elements())
    print('List is :: ',l)
	
    print('Subtract of two Counters :: ')
    c1 = Counter(a=4, b=2, c=0, d=-2)
    c2 = Counter(a=1, b=2, c=3, d=4)
    c1.subtract(c2)
    print(c1)
		
main()

'''
Counter({'blue': 3, 'red': 2, 'green': 1})
Most Common ::
[('blue', 3)]
From String :: malayalam
[('a', 4), ('m', 2), ('l', 2), ('y', 1)]
a occured ::  4
z occured ::  0
Counter to List (reverse)
List is ::  ['m', 'm', 'a', 'a', 'a', 'a', 'l', 'l', 'y']
Subtract of two Counters ::
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
'''