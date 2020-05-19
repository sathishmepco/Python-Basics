from itertools import combinations_with_replacement
def main():
    s,n = input().strip().split()
    n = int(n)
    s = sorted(s)
    result = list(combinations_with_replacement(s,n))
    for v in result:
        print("".join(v))
main()
'''
Input
HELP 2
Output
EE
EH
EL
EP
HH
HL
HP
LL
LP
PP
'''