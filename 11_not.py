print(not True)
print(not False)

print('AND')
print("True AND True => ", not (True and True))
print("True AND False => ", not (True and False))
print("False AND False => ", not (False and False))
print("True AND False => ", not (False and True))

stock = input('Ingresa el numero de "Stock" ')
stock = int(stock)

print(not(stock >= 100 and stock <= 1000))

print('OR')
print("True OR True => ", not(True or True))
print("True OR False => ", not(True or False))
print("False OR False => ", not(False or False))
print("True OR False => ", not(False or True))

role = input('Digita el rol => ')
print(not(role == 'admin' or role == 'seller'))