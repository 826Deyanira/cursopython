## Crear una función de operadores aritmeticos matemático
## operadorMatemátivo(numeroUno, numeroDos, operacion)
## operadorMatematico(4,5, 'entre')
## por consola la suma de 4/5
accionUsuario=input("ingrese la accion:")
def mensaje(nombre,apellido,accion):
    if accion == 'saludo':
        mensaje='hola ' ,nombre,apellido,'como estas'
    elif accion=='despedida':
        mensaje='adios ',nombre,apellido
    return mensaje
respuesta=mensaje('jose','alvarez',accionUsuario)
print(respuesta)