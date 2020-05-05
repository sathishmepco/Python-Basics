str = 'Hello Facebook'
print( str )
print('Character at 0 index ::',str[0] )
print('Character at 10 index ::',str[10] )
print('Last character ::',str[-1])
print('Second Last character ::',str[-2])
print('Characters from index 2 to 5 ::', str[2:5] )
print('Characters from index 2 to end of the string ::', str[2:] )
print('Characters from beginning to positino to 5 ::',str[:5])
print('Characters from the second last to end of the stirng ::',str[-2:])
print('Length of the string is ::',len(str))
print("""
Displaying 
multiple
lines
""")
print('Py''thon')
print("5 times displaying name :: ",5*'Sathish ')
print('This will join '
		'two lines together')
print('Concatenate two strings ::',str+' Developer')		
str = '      hello     '
print('String trim (strip) function :',str.strip())
str = '      hello'
print('String left trim trim (lstrip) function :',str.lstrip())
str = 'hello     '
print('String right trim (rstrip) function :',str.rstrip())
str = str.upper()
print('Upper case conversion :',str)
result = str.isupper()
print('Is all chars are upper case :',result)
str = str.lower()
print('Lower case conversion :',str)
result = str.islower()
print('Is all chars are lower case :',result)
str = str.replace('l','L')
print('Replace l with L :',str)
str = 'Hello World'
print('Splitting Hello World :',str.split())
str = 'Python#is#awesome'
print('Spliting Python#is#awesome :',str.split('#'))



'''
Hello Facebook
Character at 0 index :: H
Character at 10 index :: b
Last character :: k
Second Last character :: o
Characters from index 2 to 5 :: llo
Characters from index 2 to end of the string :: llo Facebook
Characters from beginning to positino to 5 :: Hello
Characters from the second last to end of the stirng :: ok
Length of the string is :: 14

Displaying
multiple
lines

Python
5 times displaying name ::  Sathish Sathish Sathish Sathish Sathish
This will join two lines together
Concatenate two strings :: Hello Facebook Developer
String trim (strip) function : hello
String left trim trim (lstrip) function : hello
String right trim (rstrip) function : hello
Upper case conversion : HELLO
Is all chars are upper case : True
Lower case conversion : hello
Is all chars are lower case : True
Replace l with L : heLLo
Splitting Hello World : ['Hello', 'World']
Spliting Python#is#awesome : ['Python', 'is', 'awesome']
'''