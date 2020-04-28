def main():
    n = int(input().strip())
    names = {}
    for i in range(n):
        s = input().strip().split()
        a = int(s[1])
        b = int(s[2])
        c = int(s[3])
        avg = (a+b+c)/3
        names[s[0]] = avg
    name = input().strip()
    print('{0:.2f}'.format(names[name]))

main()
'''
Test Case Input
3
Warner 150 100 120
Kohli 10 30 20
Rohit 60 80 40
Kohli
Test Case Output
20.00
'''