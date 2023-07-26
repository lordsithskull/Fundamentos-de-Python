person = {
  'name' : 'Miguel',
  'last_name' : 'Sánchez',
  'langs' : ['python', 'Javascrit'],
  'age' :  99
}

print ('\n', person, '\n')

person['name'] = 'Mike'
person['age'] -= 64
person['langs'].append('CSharp')
print ('\n', person, '\n')

#formas de eliminar informacion del diccionario
del person['last_name']
person.pop('age')

print ('\n Items')
print (person.items(), '\n')

print ('\n Keys')
print (person.keys(), '\n')

print ('\n Values')
print (person.values(), '\n')