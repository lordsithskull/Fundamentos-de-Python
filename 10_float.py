x = 3.3
y = 1.1 + 2.2
print(x)
print(y)

print(x == y)

#Redondeo con strings
y_str = format(y, ".2g")
print('str => ', y_str)
x_str = format(x, ".2g")
print('str => ', x_str)

print(y_str == x_str)
print(y_str == str(x))  # misma comparacion sin pasar por variable x_str

print('* ' * 10)  #]imprime 10 simbolos *
print(x, y)

#uso de margen de tolerancia
tolerance = 0.00001
print(abs(x - y) < tolerance)
