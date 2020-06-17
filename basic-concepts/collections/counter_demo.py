from collections import Counter
def main():
    c = Counter()
    words =  ['red', 'blue', 'red', 'green', 'blue', 'blue']
    for word in words:
        c[word] += 1
    print(c)
    print('Most Common :: ')
    print(c.most_common(1))
		
main()