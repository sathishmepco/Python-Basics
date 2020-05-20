def main():
    n = int(input().strip())
    ids = list(input().strip().split())
    count = int(input().strip())
    output = 0
    for i in range(count):
        id, price = input().strip().split()
        price = int(price)
        if id in ids:
            output += price
            ids.remove(id)
    print(str(output))
main()
'''
Input
7
1 5 3 4 2 3 7
5
1 10
2 20
2 20
4 60
4 70
Output
90
'''