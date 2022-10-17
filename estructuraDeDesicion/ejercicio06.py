##tendremos una variable con el mensaje hola mundo
##pedir al usuario un texto 
##si el texto ingresado es hola
##mostraras el mensaje  completo
##si el texto ingresadpo es como estas
##extraeras del mensaje la palabra hola
##si el texto ingresado es saludos 
##extraeras del mensasje la palabra mundo
##si se ingresa otro texto 
##mostraras por defecto el mensaje de error

mensaje='hola mundo'
texto=input('escribe un texto:')
match texto:
    case 'hola':
        print(mensaje[:])
    case 'como estas':
        print(mensaje[:4])
    case 'saludos':
        print(mensaje[5:])
    case _:
        print('error')