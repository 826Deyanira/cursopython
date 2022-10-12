## for es una estructura de ciclo
## que nos permite ingresar elementos y variables
## for numero in range(1,11):
   ##print(numero)
## while tambien es una estructura de ciclo
## int es un metodo de python que transforma un dato 
## tipo texto a un dato de tipo nuumerico real o entero
## input es un metodo de python que pide un dato por consola  al usuario

condicion=True
while condicion==True:
    numero=int(input('ingrese el numero ganador: '))
    if numero==10:
        print('ganaste el premio')
        condicion=False
    else:
        print('sientate chato ese no es numero')
