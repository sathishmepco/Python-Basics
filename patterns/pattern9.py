def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    space = 0
    for i in range(n):
        for j in range(space,n-1,1):
            print(end='  ')
        for j in range(2*i,-1,-1):
            if j == 2*i:
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
      C B A
    E D C B A
  G F E D C B A
I H G F E D C B A
'''