def checkKey(dict, key):
	#if key in dict.keys():		#valid
	#if dict.has_key(key):		#invalid (has_key() is removed in python3)
	if key in dict:				#valid
		print('Key (',key,') is available')
		print('Value is - ',dict[key])
	else:
		print('Key (',key,') is not available')

num_dic = {}
num_dic[1] = 'One'
num_dic[2] = 'Two'
print( num_dic[1] )
print( num_dic[2] )
#print( num_dic[0] )	#key error

checkKey(num_dic,1)		# key is available
checkKey(num_dic,100)	# key is not available

month_dict = {1:'Jan', 2:'Feb', 3:'Mar'}
for key, value in month_dict.items():
	print( key, value)
print(month_dict.items())
print(month_dict.keys())
print(month_dict.values())

month_dict.pop(2)
print('Removing the key 2 :',month_dict)

month_dict.clear()
print('Clearing the dictionary,',month_dict)

'''
One
Two
Key ( 1 ) is available
Value is -  One
Key ( 100 ) is not available
1 Jan
2 Feb
3 Mar
dict_items([(1, 'Jan'), (2, 'Feb'), (3, 'Mar')])
dict_keys([1, 2, 3])
dict_values(['Jan', 'Feb', 'Mar'])
Removing the key 2 : {1: 'Jan', 3: 'Mar'}
Clearing the dictionary, {}
'''