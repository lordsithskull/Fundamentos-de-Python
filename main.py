'''
print("Hola, esto es Python")
print("Hola soy Miguel y tengo 35 años")
print("12+52 =",12+52)
print("10-5 =",10-5)
print("3*29 = ", 3*29)
print("15/3 = ", 15/3)

#Esto es un comentario
'''
#import random funcion para usar valores aleatorios
import random
#tuple 
options = ('piedra', 'papel', 'tijeras')


user_option = input('Piedra, papel o tijeras => ')
user_option = user_option.lower()
computer_option = random.choice(options)

if not user_option in options:
  print('esa opcion no es valida')

print ('User option => ', user_option)
print('Computer option => ', computer_option)

if user_option == computer_option:
  print('Empate')
#caso piedra
elif user_option == 'piedra':
  if computer_option == 'tijeras':
    print('La piedra VENCE a las tijeras')
  elif computer_option == 'papel':
    print('El papel VENCE a la piedra')
#caso papel
elif user_option == 'papel':
  if computer_option == 'tijeras':
    print('Las tijeras VENCEN al papel')
  elif computer_option == 'piedra':
    print('El papel VENCE a la piedra')

elif user_option == 'tijeras':
  if computer_option == 'piedra':
    print('La piedra VENCE a las tijeras')
  elif computer_option == 'papel':
    print('Las tijeras VENCEN al papel')