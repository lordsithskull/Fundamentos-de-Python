#CRUD Create, Read, Update & delete
numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 10
print(numbers)
#append permite insertar un dato al final del arreglo/lista
numbers.append(700)
print(numbers)
#.insert permite inserta el valor en una posición expecífica
numbers.insert(0,'hola')
print(numbers)

numbers.insert(3, ' change')
print(numbers)
#Se pueden unir dos listas
task =['todo 1','todo 2', 'todo 3']
new_list = numbers + task
print(new_list)
#con index podemos saber donde se encuentra un elemento y cambiarlo
print(new_list.index('todo 2'))
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)
#pop nos permite eliminar el ultimo elemento o la posicion indicada
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)
#.sort ordena el array, cuando hay diferentes tipos de dato sort no podrá hacer el ordenamiento
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)