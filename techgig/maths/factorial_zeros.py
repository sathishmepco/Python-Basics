#This program will find out how many zeros in the end of the factorial
def main():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        output = 0
        while n >= 5:
            output += int(n/5)
            n = n/5
        print(output)
main()
'''
Input
3
10
100
1000
Output
2
24
249
'''