##pedir las  4 notas y evaluar si el promedio es mayor a 13
##mostrar el mensaje de aprobado o caso contrario de desaprobado
nota1=int(input("ingrese su primera nota:"))
nota2=int(input("ingrese su segunda nota:"))
nota3=int(input("ingrese su tercera nota:"))
nota4=int(input("ingrese su cuarta nota:"))
PROMEDIO=nota1+nota2+nota3+nota4
FINAL=PROMEDIO/4
if FINAL>13:
    print('ESTAS APROBADO')
else:
    print('ESTAS desaprobado')