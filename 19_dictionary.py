my_dict = { }
print(type (my_dict))

my_dict = {
  'avion': "Máquina voladora",
  'name' : "Miguel",
  'last_name' : 'Sánchez Escalera',
  'age' : 35
}

print(my_dict)
print(len(my_dict))

print(my_dict['name'])
print(my_dict['last_name'])
#get permite buscar un valor del dict, pero si no se encuentra no genera error en el programa
print(my_dict.get('unvalor'))

#otro tipo de validacion es con 'in', esta devuelve un valor booleano
print('avion' in my_dict)
print('oto' in my_dict)