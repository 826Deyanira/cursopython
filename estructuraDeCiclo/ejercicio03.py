eval=True
while eval==True:
    numero=int(input("ingrese que numero de tabla deseas:"))
    if numero==0:
        print('error')
        break
    else:
        for numeros in range(1,11):
            print(numeros, '*' ,numero, '=' ,numeros*numero)
         