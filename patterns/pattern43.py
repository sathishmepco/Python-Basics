def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(5,0,-1):
            if j == 5:
                print(str(j),end='')
            else:
                print(' '+str(j),end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''