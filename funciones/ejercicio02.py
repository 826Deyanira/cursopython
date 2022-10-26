numero='10'
int(numero)
setence=input('ingrese los datos: ')
def countsvocals(texto):
    vocales=['a','e','i','o','u']
    contadorvocales=0
    for letras in texto:
        if letras in vocales:
            contadorvocales+=1
    return contadorvocales
print('la cantidad de vocales es: ',countsvocals(setence))


## crear una funcion con 
##def countvocales(setence, vocales):
##return contador