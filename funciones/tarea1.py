## Crear una función de operadores aritmeticos matemático
## operadorMatemátivo(numeroUno, numeroDos, operacion)
## operadorMatematico(4,5, 'entre')
## por consola la suma de 4/5
operacionUsuario=input("ingrese la operacion:")
def operadorMatematico(num1,num2,operacion):
    if operacion == 'suma':
        resultado= num1+num2
    elif operacion =='resta':
        resultado= num1-num2
    elif operacion =='multiplicacion':
        resultado= num1*num2
    elif operacion =='division':
        resultado= num1/num2
    return resultado
final=operadorMatematico(10,3,operacionUsuario)
print(final)