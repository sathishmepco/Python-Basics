def main():
    n = int(input().strip())
    space = 0
    for i in range(n):
        for j in range(space,n-1,1):
            print(end='  ')
        for j in range(1,2*i+2,1):
            if j == 1:
                print(str(j),end='')
            else:
                print(' '+str(j),end='')
        space+=1
        if i < n-1:
            print()
main()
'''
Input
5
Output
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
'''