def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(n-i):
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
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''