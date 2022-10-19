##los numeros primos
##la division en ellos mismos y 1
##residuo siempre es cero 
# 2/1 == 0
# 2/2 == 0
# 3/1 == 0
# 3/3 == 0
# 5/1 == 0
# 5/5 == 0
##compubinario
##hacer un algoritmo que pida al ususario un numero
##y me diga si ese numero es primo o no
numero=int(input("ingrese un numero:"))
for n in range(2,numero):
    if numero%n == 0:
        print('no es primo')
        break
    elif numero%3 == 0:
        print('no es primo')
        break
    else:
        print('es primo')
        break

##otra forma
## condicion=True
## while condicion==True
## numero=int(input("ingrese un numero:"))
##  if numero%2==0 or numero%3==0:
##     print('no es primo')
##  else:
##        print('es primo') 
##        condicion=False