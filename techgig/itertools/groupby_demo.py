from itertools import groupby
def main():
    s = input().strip()
    groups = groupby(s)
    result = [(sum(1 for _ in group),label) for label, group in groups]
    output = " ".join("({}, {})".format(label, count) for label, count in result)
    print(output)
main()
'''
from itertools import zip_longest
def main():
    s = input().strip()
    counts = []
    count = 1
    for a,b in zip_longest(s,s[1:], fillvalue = None):
        if a == b:
            count += 1
        else:
            counts.append((count,a))
            count = 1
    for i in range(len(counts)):
        v = counts[i]
        v = str(v).replace("\'","")
        if i == len(counts)-1:
            print(v)
        else:
            print(v,end=' ')
'''
main()

'''
Input
244001
Output
(1, 2) (2, 4) (2, 0) (1, 1)
'''