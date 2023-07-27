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

score_computer = 0
score_user = 0
#tuple

options = ('piedra', 'papel', 'tijeras')

while (True):
  print('\n', '*' * 10)
  user_option = input('Piedra, papel o tijeras => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)
  if not user_option in options:
    print('esa opcion no es valida')

  print('User option => ', user_option)
  print('Computer option => ', computer_option)

  if user_option == computer_option:
    print('Empate')
  #caso piedra
  elif user_option == 'piedra':
    if computer_option == 'tijeras':
      print('La piedra VENCE a las tijeras')
      score_user += 1
    elif computer_option == 'papel':
      print('El papel VENCE a la piedra')
      score_computer += 1
  #caso papel
  elif user_option == 'papel':
    if computer_option == 'tijeras':
      print('Las tijeras VENCEN al papel')
      score_computer += 1
    elif computer_option == 'piedra':
      print('El papel VENCE a la piedra')
      score_user += 1
  #caso tijeras
  elif user_option == 'tijeras':
    if computer_option == 'piedra':
      print('La piedra VENCE a las tijeras')
      score_computer += 1
    elif computer_option == 'papel':
      print('Las tijeras VENCEN al papel')
      score_user += 1
  print('Marcador : \n Usuario => ', score_user, '\n CPU => ', score_computer)

  if score_computer == 2:
    print('\nEL CPU ganó ', score_computer, ' a ', score_user)
    break
  if score_user == 2:
    print('\nEL Usuario ganó ', score_user, ' a ', score_computer)
    break
