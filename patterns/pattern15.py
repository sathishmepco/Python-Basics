def main():
    n = int(input().strip())
    space = 0
    k = 0
    for i in range(n):
        for j in range(space,n-1,1):
            print(end='  ')
        for j in range(0,k+1,1):
            if j == 0:
                print('*',end='')
            else:
                print(' *',end='')
        space+=1
        k+=2
        if i < n-1:
            print()
main()
'''
Input
5
Output
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''