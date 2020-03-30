import os
import platform
import calculator as calc
from employee import person

a = 100
b = 101

print(f'Sum of {a} and {b} is -',calc.add(a,b))
print('Is', a,'even -',calc.isEven(a))
print('Is', b,'even -',calc.isEven(b))
print('Person name -',person['name'])
print('Person country -',person['country'])
print('Operating System is -',platform.system())
print('Hello, ' + os.getlogin() + '! How are you?')