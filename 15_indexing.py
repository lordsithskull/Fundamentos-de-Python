#indexado de los caracteres en el string
text = 'Ella sabe Python'
print(text[0])
print(text[5])
#print(text[99]) genera error ya que no exite la posicion
size = len(text)
#obtener valor del último caracter
print("size => ", size)
print(text[size - 1])
print(text[-1])

#slicing
print(text[0:5])
print(text[10:16])
print(text[:5])

print(text[5:-1])
print(text[5:])
print(text[:])

print(text[10:16:1])
print(text[10:16:2])
print(text[::2])
