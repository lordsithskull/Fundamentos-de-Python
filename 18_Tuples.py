#Las tuplas son inmutables, no permiten agregar, modificar valores
numbers = (1, 2, 3, 4, 5)
strings = ('Alan','Maria', 'Juan', 'zule', 'Maria')

print(numbers)
print(type(numbers))
print(strings)
print(type(strings))

#numbers.append(10) '''generará un error '''
print(numbers)
#numbers[1] = 'change '''de igual forma 'change' generará un errror''

print(strings)
print(strings.index('zule'))
#.count permite contar el numero de veces de un elemento en la tupla
print(strings.count('Maria')) 

#coversion de tupla a lista 
my_list = list(strings)
my_list[1] = 'Julio'
print(my_list)
my_tuple = tuple(my_list)
print(my_list)