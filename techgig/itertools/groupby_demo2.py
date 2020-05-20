from itertools import groupby
def main():
    s = input().strip()
    s = sorted(s)
    groups = groupby(s)
    result = [(sum(1 for _ in group),label) for label, group in groups]
    output = " ".join("({}, \'{}\')".format(label, count) for label, count in result)
    print(output)
main()
'''
Input
aabbccc
Output
(2, 'a') (2, 'b') (3, 'c')
'''