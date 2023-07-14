name = "Miguel"
last_name = "Sánchez Escalera"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

#se pueden usar diferentes comillas es decir declar con '' o "" dependiendo la oracion
quote = "I'm Miguel"
print(quote)

quote1 = 'She said "Hello"'
print(quote1)

template = "Hola mi nombre es " + name + " y mis apellidos son " + last_name
print(template)

template = "hola, mi nombre es {} y mis apellidos son {}".format(
  name, last_name)
print('v2', template)

template = f"hola, mi nombre es {name} y mis apellidos son {last_name}"
print('v3', template)
