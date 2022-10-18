mensaje=input("ingrese un mensajito:")
contador=0
for letras in mensaje:
    if letras=='a':
        contador+=1
print('en este mensaje tienes ', contador, 'A')
