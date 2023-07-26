'''
while True
  print('Ciclo infinito')
'''

'''
counter normal
counter = 0 
while counter < 10:
  counter += 1
  print(counter)
'''

'''
#Rompiendo el while con  break
counter = 0
while counter < 20:
  counter += 1
  if counter == 15:
    break  
  print(counter)  
'''

''' '''
counter = 0

#continue salta a la siguiente iteracion hasta que se cumpla la funcion
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)