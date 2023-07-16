'''
print("Hola, esto es Python")
print("Hola soy Miguel y tengo 35 años")
print("12+52 =",12+52)
print("10-5 =",10-5)
print("3*29 = ", 3*29)
print("15/3 = ", 15/3)

#Esto es un comentario
'''

user_option = input('Piedra, papel o tijeras => ')
computer_option = 'papel'

if user_option == computer_option:
  print('Empate')
#caso piedra
elif user_option == 'piedra':
  if computer_option == 'tijeras':
    print('La piedra vence a la tijeras')
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