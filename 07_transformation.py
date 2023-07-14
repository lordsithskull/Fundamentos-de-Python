#python puede transformar el tipo de dato de forma dinámica
name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Nicolas " + "Molina")
print(10 + 20)
#una expresion como esta genera un error print("Nicolas" + 12)

#para solucionar se pueden usar las expresiones
age = 12
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')
