import os
import platform
import calculator as calc
from employee import person

def function(country="India"):
	print("I am from "+country)

a = 100
b = 101

print(f'Sum of {a} and {b} is -',calc.add(a,b))
print('Is', a,'even -',calc.isEven(a))
print('Is', b,'even -',calc.isEven(b))
print('Person name -',person['name'])
print('Person country -',person['country'])
print('Operating System is -',platform.system())
print('Hello, ' + os.getlogin() + '! How are you?')
function("America")
function()

'''
Sum of 100 and 101 is - 201
Is 100 even - True
Is 101 even - False
Person name - Sathish
Person country - India
Operating System is - Windows
Hello, Seng! How are you?
I am from America
I am from India
'''