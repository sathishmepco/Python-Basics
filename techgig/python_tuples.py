def main():
    n = int(input().strip())
    s = input().strip().split()
    k = int(input().strip())
    num_tuple = ()
    for i in range(n):
        v = int(s[i].strip())
        num_tuple = num_tuple+(v,)
    counter = 0
    for v in num_tuple:
        if v is k:
            counter+=1;
    print(counter,end='')

main()


'''
Input
4
1 3 3 5
3
Output
2
'''