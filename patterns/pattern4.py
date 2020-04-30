def main():
    n = int(input().strip())
    for i in range(n,0,-1):
        for j in range(2*(n-i)):
            print(' ',end='')
        for j in range((2*i)-1):
            if j == 0:
                print(end='*')
            else:
                print(' *',end='')
        if i > 1:
            print()
main()

'''
Input
5
Output
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''