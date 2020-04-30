def main():
    n = int(input().strip())
    for i in range(n,0,-1):
        for j in range(2*(n-i)):
            print(' ',end='')
        for j in range((2*i)-1):
            if j == 0:
                print(i,end='')
            else:
                print(' '+(str(i)),end='')
        if i > 1:
            print()
main()

'''
Input
5
Output
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
'''