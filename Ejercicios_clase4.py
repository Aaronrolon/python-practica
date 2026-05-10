"""Ejercitación.
Escribir un programa que muestre en qué etapa de la vida se encuentra según la edad ingresada
Fases:
pre natal (embarazo)
Infancia (0 a 6 años de edad)
Niñez (6 a 12 años de edad)
Adolescencia (12 a 20 años de edad)
Juventud (20 a 25 años de edad)
Adultez (25 a 60 años de edad)
Ancianidad (60 años en adelante)"""

edad = int(input("Ingrese su edad para mortar en que etapa de vida esta: "))

match edad : 
    case _ if edad >= 0:
        print("Prenatal")
    case _ if edad >=0 and edad <= 12:
        print("Niñez")
    case _ if  edad >= 12 and edad <= 20:
        print("Adolescencia")
    case _ if edad >=20 and edad <= 25:
        print("Juventud")
    case _ if edad >= 25 and edad <= 60:
        print("Adultez")
    case _ if edad >= 60:
        print("Ancianidad")

"""1. Escribir un programa que almacene en una CONSTANTE una contraseña, luego solicite al usuario ingresar la
contraseña, si es correcta mostrará el mensaje la contraseña es correcta y terminará el programa, de lo contrario
mostrará el mensaje contraseña incorrecta intente nuevamente, y se solicitara nuevamente la contraseña hasta
que la esta sea la correcta."""
"""Un contador es una variable entera que la utilizamos para
contar cuando ocurre un suceso. """
contador = 0
INTENTOS_MAXIMOS = 3
contraseña = 12345
while contador > INTENTOS_MAXIMOS:
   verificacion =  int(input("Ingrese la contraseña para ingresar: "))
   if contraseña == verificacion:
       print("!Bienvenido usuario")
       break
   
   contador +=1
   print("Utilizastes el maximo de intentos")
   
else:
       print(f"Error, Intentos restantes {INTENTOS_MAXIMOS}")

"""Ejercicio: Escriba un programa que permita el ingreso de
números por teclado, cada número que ingrese debe tener una
posición empezando por el 1, el siguiente el 2.... Cada vez que
se ingrese un número mostrará la posición y el valor del
número ingresado, pero si ingresa el cero 0 el programa debe
terminar.
Ejemplo 1- nro: 325
2- nro: 4
0- Programa terminado"""

acumulador = 0

while True:
    n = float(input("ingrese un numero: "))
    if n == 0 :
        break

    acumulador +=1
    print(f"Su numero ingresado es {n:.2f} - el acumulado es {acumulador}")

"""Ejercitación.
1. Escribir un programa que muestre automáticamente los números del 1 al 10.
2. Escribir un programa que muestre la tabla del 3, sin multiplicar (utilice un acumulador)"""

for i in range(0,11):
    print(i * 3)