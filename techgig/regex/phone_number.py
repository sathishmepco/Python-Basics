import re
def main():
    no = input().strip()
    if re.match(r'[89]\d{9}$',no):   
        print('YES')
    else:  
        print('NO')  
main()
'''
Input
8889997878
Output
YES
'''