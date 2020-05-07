def main():
    n = int(input().strip())
    arr = []
    flag = -1
    for i in range(n):
        v = int(input().strip())
        arr.append(v)
    for i in range(n):
        if arr.count(arr[i]) >= 2:
            flag = arr[i]
            break
    
    print(flag,end='')
        
main()

'''
Input
7
10
5
3
4
3
5
6
Output
5
'''