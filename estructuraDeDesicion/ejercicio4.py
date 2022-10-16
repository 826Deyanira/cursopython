##si es entre 13 y 15==regular
##si es entre 15 y 17==bueno
##si es entre 17 y 20==excelente
nota1=float(input("ingrese su primera nota:"))
nota2=float(input("ingrese su segunda nota:"))
nota3=float(input("ingrese su tercera nota:"))
nota4=float(input("ingrese su cuarta nota:"))
PROMEDIO=nota1+nota2+nota3+nota4
FINAL=PROMEDIO/4
print(FINAL)
if FINAL<13:
    print('ERES BURRITO')
if FINAL>=13 and FINAL<=15:
    print('ERES REGULAR')
if FINAL>15 and FINAL<=17:
    print('ERES BUENO')
if FINAL>17 and FINAL<=20:
    print('ERES EXCELENTE')
