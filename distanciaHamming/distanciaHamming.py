palabraValida='hola'
evaluar='gola'
distanciaHamming=0
if len(palabraValida) == len(evaluar):
    for letras in range(0,len(palabraValida)):
        if palabraValida[letras]!=evaluar[letras]:
            distanciaHamming+=1
print('distancia hamming', distanciaHamming)