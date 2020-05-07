def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(n-i-1):
            print(end='  ')
        for j in range(i+1):
            if j == 0:
                print(CHARS[j],end='')
            else:
                print(' '+CHARS[j],end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
        A
      A B
    A B C
  A B C D
A B C D E
'''