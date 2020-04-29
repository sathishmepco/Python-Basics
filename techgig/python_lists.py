def main():
    n = int(input().strip())
    output_list = []
    for i in range(n):
        s = input().strip().split()
        if s[0] is '1':
            output_list.append(s[1])
        else:
            if i < n-1:
                print(output_list)
            else:
                print(output_list,end='')


main()

'''
Input
5
1 32
2
1 arpit
1 54
2
Output
['32']
['32', 'arpit', '54']
'''