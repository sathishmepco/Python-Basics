def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    space = 0
    for i in range(n):
        for j in range(space,n-1,1):
            print(end='  ')
        for j in range(2*i+1):
            if j == 0:
                print(CHARS[j],end='')
            else:
                print(' '+CHARS[j],end='')
        space+=1
        if i < n-1:
            print()
main()
'''
Input
5
Output
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
'''