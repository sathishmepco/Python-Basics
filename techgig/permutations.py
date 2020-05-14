from itertools import permutations 
def main():
    s,n = input().strip().split()
    n = int(n)
    p = permutations(s,n)
    l = sorted(list(p))
    for val in l:
        print(''.join(val))
main()
'''
Input
HELP 3
Output
EHL
EHP
ELH
ELP
EPH
EPL
HEL
HEP
HLE
HLP
HPE
HPL
LEH
LEP
LHE
LHP
LPE
LPH
PEH
PEL
PHE
PHL
PLE
PLH
'''