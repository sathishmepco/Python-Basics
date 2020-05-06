def main():
    n = int(input().strip())
    m1 = m2 = m3 = m4 = m5 = 0
    for i in range(n):
        s = input().strip().split()
        m1 += int(s[1])
        m2 += int(s[2])
        m3 += int(s[3])
        m4 += int(s[4])
        m5 += int(s[5])
    print('{0:.2f}'.format(m1/n),end=' ')
    print('{0:.2f}'.format(m2/n),end=' ')
    print('{0:.2f}'.format(m3/n),end=' ')
    print('{0:.2f}'.format(m4/n),end=' ')
    print('{0:.2f}'.format(m5/n),end='')
main()

'''
Input
2
arpit 100 75 40 56 53
anushka 100 100 76 100 100
Output
100.00 87.50 58.00 78.00 76.50
'''