def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(i):
            print(end='  ')
        for j in range(0,n-i,1):
            if j == 0:
                print(str(j+1),end='')
            else:
                print(' '+str(j+1),end='')
        if i < n-1:
            print()
main()

'''
Input
5
Output
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
'''