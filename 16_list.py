numbers = [1, 2, 3]
print(type(numbers))

task = [1, True, 'Hola']
print(type(task))
print(task[1])
text = 'Hola'
#text[0] = 'W' Esta linea de codigo no se podra ejecutar
#Python no permite reemplazar la 'H' en 'hola' por la 'w'
task[0] = 'watch platzi courses'
print(task)

print(numbers[:3])
print(numbers[2:3])
print(numbers[1:3])
