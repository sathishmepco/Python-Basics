def main():
    number = int(input()) 
    s = list(map(int,input().strip().split()))[:number] 
    print('List is ',s)
    print('Tuple is ',tuple(s))
    print(hash(tuple(s)))
main()