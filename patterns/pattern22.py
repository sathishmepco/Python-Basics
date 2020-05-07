def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(i):
            print(end='  ')
        for j in range(i,n,1):
            if j == i:
                print(end='*')
            else:
                print(' *',end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
* * * * *
  * * * *
    * * *
      * *
        *
'''