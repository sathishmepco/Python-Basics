def main():
    n = int(input().strip())
    names = {}
    min_rat = 100
    for i in range(n):
        name = input().strip()
        ratting = int(input().strip())
        names[name] = ratting
        if min_rat > ratting:
            min_rat = ratting
    output = []
    for key,value in names.items():
        if value is min_rat:
            output.append(key)
    output.sort()
    for x in output:
        print(x)
main()
'''
Input
-----
4
Warner
2
Kohli
1
Rohit
3
Sachin
1

Output
------
Kohli
Sachin
'''