def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(i+1):
            if j == 0:
                print(str(i+1),end='')
            else:
                print(' '+str(i+1),end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''