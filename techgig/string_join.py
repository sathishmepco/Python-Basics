def main():
    liss=[] 
    concat=input() 
    while(True): 
        try: 
            character=input() 
        except: 
            break 
        liss.append(character) 
    print(concat.join(liss), end="")
main()

'''
Input
-
sathish
prem
vinoth
Output
sathish-prem-vinoth
'''