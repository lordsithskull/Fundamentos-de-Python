print('AND')
print("True AND True => ", True and True)
print("True AND False => ", True and False)
print("False AND False => ", False and False)
print("True AND False => ", False and True)

print("10 > 5 y  5< 10 ", 10 > 5 and 5 < 10)
print("10 > 5 y  5 > 10 ", 10 > 5 and 5 > 10)

stock = input('Ingresa el numero de "Stock" ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

print('OR')
print("True OR True => ", True or True)
print("True OR False => ", True or False)
print("False OR False => ", False or False)
print("True OR False => ", False or True)

role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')