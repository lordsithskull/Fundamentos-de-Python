text = 'Ella sabe programar en Python'
'''
# in dentro del arreglo permite la busqueda dentro de un string
print('Javascript' in text)
print('Python' in text)
if 'Python' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')
  '''
#Con size podemos saber el tamaño del string
size = len('text')
print(size)

print(text)
print(text.upper())
print(text.lower())
print('Cuantas "a" hay en el texto ', text.count('a'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text_2 ='este es un título'
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("398".isdigit())
print(text.islower())