numero = int(input('Introduce un numero '))
residuo = numero % 2

if residuo == 0:
  print(f'El numero {numero} es par')
elif residuo == 1:
  print(f'El numero {numero} es impar')
  