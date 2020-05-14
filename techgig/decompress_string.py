def main():
    s = input().strip()
    arr = sorted(s)
    s = "".join(arr)
    distinct = list(set(arr))
    distinct = sorted(distinct)
    d = {}
    output = ''
    for i in range(len(distinct)):
        d[distinct[i]] = s.count(distinct[i])
    for k, v in d.items():
        output += '('+str(v)+', \''+k+'\')'+" "
    print(output.strip(),end='')

main()

'''
Input
aaabbcccd
Output
(3, 'a') (2, 'b') (3, 'c') (1, 'd')
'''