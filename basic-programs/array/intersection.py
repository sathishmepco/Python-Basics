def main():
    a = int(input('Enter the length of array1 : ').strip())
    s1 = input('Enter the values of array1 : ').strip()
    b = int(input('Enter the length of array2 : ').strip())
    s2 = input('Enter the values of array2 : ').strip()
    array1 = s1.split()
    array2 = s2.split()
    list1 = []
    list2 = []
    for i in range(a):
        value = int(array1[i])
        list1.append(value)
    for i in range(b):
        value = int(array2[i])
        list2.append(value)
    list3 = list(set(list1) & set(list2))
    print('intersection of both arrays : ',list3)
main()

'''
Enter the length of array1 : 3
Enter the values of array1 : 1 2 3
Enter the length of array2 : 3
Enter the values of array2 : 2 3 4
intersection of both arrays :  [2, 3]
'''