#This porgram will add the both array elements and removes duplicates
def main():
    a = int(input().strip())
    s1 = input().strip()
    b = int(input().strip())
    s2 = input().strip()
    array1 = s1.split()
    array2 = s2.split()
    count = 0
    array1.extend(array2)
    array1 = list(dict.fromkeys(array1))
    print(array1)

main()

'''
Input
3
1 2 3
3
2 3 4
Output
['1', '2', '3', '4']
'''