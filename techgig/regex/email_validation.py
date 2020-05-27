import re
def main():
    email = input().strip()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        print('YES')
    else:
        print("NO")
main()

'''
Input
practice@prac.com
Output
YES
'''