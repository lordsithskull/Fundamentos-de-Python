'''
En este desafío, se te proporcionará una lista de letras llamada letters. Tu reto es realizar las siguientes operaciones en orden:

Agregar la letra G al final de la lista.
Reemplazar la letra en la posición 0 con la letra Z.
Eliminar la letra C de la lista.
Imprimir la lista resultante al revés.
Ejemplo:

Input: ["A", "B", "C", "D", "E", "F"]
Output: ["G", "F", "E", "D", "B", "Z"]
'''

letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

print(letters)
letters.append('G')
print(letters)
print(letters.index('A'))
letters[0] = 'Z'
print(letters)
letters.reverse()
print(letters)