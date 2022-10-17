mensaje='hola mundo'
texto=input('escribe un texto: ')
if texto=='hola':
    print(mensaje[:])
elif texto=='como estas':
    print(mensaje[:4])
elif texto=='saludos':
    print(mensaje[5:])
else:
    print('error')