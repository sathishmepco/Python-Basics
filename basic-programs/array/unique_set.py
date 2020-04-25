#Find unique elements
def main():
    s1 = input().strip()
    array1 = s1.split()
    uniqueset = set(array1)
    print(uniqueset)

main()

'''
Input
1 2 3 2 3 1 4 5 3 4 5
Output
{'1', '2', '5', '3', '4'}
'''