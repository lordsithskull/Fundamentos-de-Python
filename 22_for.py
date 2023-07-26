'''
#range sera el rango range(20) contará del 0 al 20, pero podemos especificar
#desde que rango comenzar  range(1,20)
for element in range(1,20):
  print(element)
'''

my_list = [23, 45, 67, 89, 43]
print('Lista')
for element in my_list:
  print(element)
print('\n')

print('Tupla')
my_tuple = ('Miguel', 'Jaime', 'Daniel', 'Aime', 'Samuel', 'Isabel', 'Edith')
for names in my_tuple:
  print(names)
print('\n')


print('diccionario')
product = {
  'name' : 'Camisa',
  'price' : 100,
  'stock' : 89
}

for ropa in product:
  print(ropa)
print('\n')

for key in product:
  print(key,' => ',product[key])
print('\n')

for key, value in product.items():
  print(key, ' => ', value)
print('\n')
print('diccionarios multiples')
people = [
  {
    'name' : 'nico',
    'age' : 34
  },
  {
    'name' : 'zule',
    'age'  : 45    
  },
  {
    'name' : 'santi',
    'age' : 4
  }
]

for person in people:
  print(person)

for person in people:
  print('name =>', person['name'])
  print('age =>', person['age'])