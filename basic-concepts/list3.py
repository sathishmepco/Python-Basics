def sortByLength(e):
  return len(e)
def sortByYear(e):
  return e['year']  

list = [23,32,52,12,11,10,90,34]
print('The list elements are :',list)
list.sort()
print('After sorting :',list)
list.sort(reverse=True)
print('Reversing the list :',list)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW','Volvo']
print('String list :',cars)
cars.sort()
print('Sorting the string list :',cars)
cars.sort(key=sortByLength)
print('Sort the string by length :',cars)

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
print('Cars dictionary :',cars)
cars.sort(key=sortByYear)
print('Sort the cars by year :',cars)