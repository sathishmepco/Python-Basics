import json

#convert string to json object
json_str =  '{ "name":"Sathish", "age":30, "city":"Chennai"}'
json_obj = json.loads(json_str)

print(json_obj['city'])
print(json_obj['name'])

#convert dict to json
dict = {
  "name": "Sathish",
  "age": 30,
  "city": "Chennai"
}
json_str = json.dumps(dict)
print(json_str)
