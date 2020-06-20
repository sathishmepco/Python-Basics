from collections import namedtuple
def main():
	Person = namedtuple('Person','name age gender')
	print('Type of Person is ::',type(Person))
	sat = Person(name='Sathish',age=33,gender='male')
	jessy = Person(name='Jessy',age=30,gender='female')
	print('Representation is :',sat)
	print('Field by name :',jessy.name)
	for p in [sat,jessy]:
		print(p)
		
	try:
		namedtuple('Person','name class age')
	except ValueError as err:
		print(err)
		
	try:
		namedtuple('Person','name age age')
	except ValueError as err:
		print(err)
		
	Address = namedtuple('Address',['street','city','state'])
	s1 = Address('anna nagar','Chennai','Tamil Nadu')
	s2 = Address('kkr nagar','Madurai','Tamil Nadu')
	print(s1[0])
	print(s1.city)
	print(getattr(s1,'state'))
	print(s2._fields)
	print(s2)
	print(s2._replace(street = 'KKR NAGAR')) 

main()
'''
Type of Person is :: <class 'type'>
Representation is : Person(name='Sathish', age=33, gender='male')
Field by name : Jessy
Person(name='Sathish', age=33, gender='male')
Person(name='Jessy', age=30, gender='female')
Type names and field names cannot be a keyword: 'class'
Encountered duplicate field name: 'age'
anna nagar
Chennai
Tamil Nadu
('street', 'city', 'state')
Address(street='kkr nagar', city='Madurai', state='Tamil Nadu')
Address(street='KKR NAGAR', city='Madurai', state='Tamil Nadu')
'''