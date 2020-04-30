def main():
    n = int(input().strip())
    d = 2*n -1
    k = 0
    for i in range(n):
        for j in range(k):
            print('  ',end='')
        for j in range(d):
            if j == 0:
                print(d,end='')
            else:
                print(' '+str(d),end='')
        d -= 2
        k += 1
        if i < n-1:
            print('')

main()

'''
Input
5
Output
9 9 9 9 9 9 9 9 9
  7 7 7 7 7 7 7
    5 5 5 5 5
      3 3 3
        1
'''