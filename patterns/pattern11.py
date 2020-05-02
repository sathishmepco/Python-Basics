def main():
    n = int(input().strip())
    space = 0
    for i in range(n):
        for j in range(space,n-1,1):
            print(end='  ')
        for j in range(2*i+1,0,-1):
            if j == 2*i+1:
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
      3 2 1
    5 4 3 2 1
  7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
'''