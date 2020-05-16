from itertools import combinations
def main():
    s,n = input().strip().split()
    n = int(n)
    s = sorted(s)
    for i in range(1,n+1):
        result = list(combinations(s,i))
        for val in result:
            print(''.join(val))
main()

'''
Input
HELP 2
Output
E
H
L
P
EH
EL
EP
HL
HP
LP
'''