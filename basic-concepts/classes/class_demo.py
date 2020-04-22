class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def sayHello(self):
		print("Hello my name is " + self.name)  

	def myfunc(abc):
		print("Hello my name is " + abc.name)
		
print(Person)
p1 = Person("John", 36)
p1.age = 40
print(p1.name)
print(p1.age)
p1.sayHello()
p1.myfunc()
#del p1  #whiche deletes the object

'''
<class '__main__.Person'>
John
40
Hello my name is John
Hello my name is John
'''