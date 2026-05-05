#Primeros pasos en python
#1. Escribir un programa que muestre por pantalla “Hola mundo”
print("Hola mundo")
"""2. Escribir un programa, que muestre los números del 1 al 5. Para los que sepan programar,
NO deben utilizar estructuras NO vistas en la clase 2.
Resultado final: 12345
"""
print("1,2,3,4,5")
"""3. Crear un programa que muestre una letra en cada renglón, se repite 3 veces, por ejemplo:
Resultado final:
a
a
a
"""
print("a")
print("a")
print("a") 
""""4. Crear un programa que muestre un triángulo formado por una letra, como se muestra a
continuación:
O
OO
OOO
OOOO
"""
print("O")
print("OO")
print("OOO")
print("OOOO")

#5. Escribir un programa que muestre por pantalla nombre y apellido
print("nombre> juan")
print("apellido> perez")

"""6. Escribir un programa que agregue dos comentarios al ejercicio anterior, donde diga nombre:
tu nombre y abajo otro comentario tu apellido
"""
nombre = "aaron"
#nombre del usuario
apellido = "rolon"
#apellido del usuario

"""7. Agregar un comentario que cuente qué operación realiza este programa"""
numero1 = 15 
numero2 = 20
print((numero1 + numero2)/2)
#suma de 2 variables decimales.

#Variables, constantes
"""8. Escribir un programa que asigne un mismo valor entero a 3 variables en una sola línea y
muestre por pantalla el contenido de cada una."""

valor = valor_2 = valor_3 = (1)
print(valor)
print(valor_2)
print(valor_3)

"""9. Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre
por pantalla el contenido de la variable"""

saludo = "Hola mundo"
print(saludo)

"""10. Escribir 4 programas que contengan una variable inválida cada uno.(distintas)
● Trate de ejecutar y analice el error, vea con atención los mensajes de error que le
devuelve el intérprete"""

"""2num = 2 
print("error de numero en la variable")
for = 5
print("error de palabra reservada")
salu do = "hola"
print("error de espacio en variable")
pesos$ = "valor pesos"
    print("error de signo en variable")"""

"""Escribir un programa que contenga 8 variables, 2 de cada tipo de datos visto en clase. luego
imprima indicando a qué tipo pertenece y su contenido. Por ejemplo:"""

# 2 variables int
edad = 20
anio = 2025

# 2 variables float
altura = 1.75
peso = 70.5

# 2 variables str
nombre = "Aaron"
ciudad = "Buenos Aires"

# 2 variables bool
es_mayor = True
tiene_auto = False


# Mostrar tipo y contenido
print("edad:", edad, "tipo:", type(edad))
print("anio:", anio, "tipo:", type(anio))

print("altura:", altura, "tipo:", type(altura))
print("peso:", peso, "tipo:", type(peso))

print("nombre:", nombre, "tipo:", type(nombre))
print("ciudad:", ciudad, "tipo:", type(ciudad))

print("es_mayor:", es_mayor, "tipo:", type(es_mayor))
print("tiene_auto:", tiene_auto, "tipo:", type(tiene_auto))

"""12. Escriba un programa que contenga 3 constantes, elija 3 elementos de la tabla periódica y
asigne a cada una de las constantes el peso atómico de cada elemento. muestre por pantalla
el elemento y el peso atómico correspondiente. """

titanio = 47.867
hierro = 55.845
cromo = 51.996
print(f"Titanio (Ti), peso atomico:{titanio}")
print(f"Hierro (Fe), peso atomico:{hierro}")
print(f"Cromo (Cr), peso atomico:{cromo}")

"""13. Escribir un programa que almacene en distintas variables, dos valores enteros , dos reales ,
dos string y muestre el tipo de dato con la instrucción type() de todas las variables."""

num1 = 2
num2 = 5
palabra1 = "hello"
palabra2 = "mundo"
num1_real = 3.14
num2_real = 0.0
print("numero entero 1",num1 , "Tipo", type(num1))
print("numero entero 2",num2, "Tipo", type(num2))
print("numero reales 1",num1_real, "Tipo", type(num1_real))
print("numero reales 2",num2_real, "Tipo", type(num2_real))
print("primera palabra",palabra1, "Tipo", type(palabra1))
print("segunda palabra",palabra2, "Tipo", type(palabra2))

"""14. Escribir un programa que muestre por pantalla el resultado de la suma de dos variables
numéricas"""

num1 = 5
num2 = 10
print(f"La suma del numero {num1}, mas el numero {num2} es: {num1 + num2}")

"""15. Escribir un programa que muestre por pantalla el resultado de la siguiente operación
aritmética"""

num = ((3 + 2) / (2-5))**2
print(num)

"""16. Escribir un programa que calcule y muestre por pantalla el 15% de 5400"""
num = 5400

print(f"El 15% de 5400 es: {5400 * 0.15}")

"""17. Escribir un programa que muestre por pantalla, el resultado de 27 dividido 5 y el resto de esa
división (recuerde cómo se calcula el resto , busque el operador de python en la guia de
estudio) , almacene cada valor en una variable distinta."""

divicion = 27 / 5
resto = 27 % 5
print(f"La div de (27/5) es: {divicion}")
print(f"El resto de la div de (27/5) es: {resto}")

"""18. Escribir un programa que calcule el área de un triángulo, sabiendo que :
● La base (b) mide 20.5
● La altura (h) es igual a la base al cuadrado
Investigue cual es la fórmula para calcular el área de un triángulo y utilicela en el programa
luego muestre por pantalla el resultado"""

base = 20.5
altura = 20.5
area = (base * altura) / 2
print(f"la base del triangulo es: {base},la altura es: {20,5} y el area del triangulo es: {area}. ")

#Conversión implícita
"""20. Escribir un programa que muestre por pantalla el resultado de dos sumas de 3 variables, una
de tipo int, una de tipo float y otra de tipo bool que primero tomará el valor True y luego el
valor False. (analice la situación y responda qué sucedió"""

num_int = 25
num_float = 3.14
#primer caso 
valor_boleano = True
suma1 = num_int + num_float + valor_boleano
#segundo caso 
valor_boleano = False
suma2 = num_int + num_float + valor_boleano

print(f"La suma con True: {suma1}.")
print(f"La suma con false: {suma2}.")

#Entradas input()

"""21. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo
por hora. Después debe mostrar por pantalla la paga que le corresponde."""

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo por hora: "))
pago = horas_trabajadas * costo_por_hora
print(f"La paga total es: {pago}")

"""22. Escribir un programa que contenga 4 variables con valores de los distintos tipos de datos
vistos en clase, entero, reales(coma), string(texto) y booleano. luego muestre por pantalla
cada una de las variables en una misma línea."""

num_entero = 10
num_reales = 14.45
string = "aaronrolon"
booleano = True
print(f"num entero {num_entero}, numero reales {num_reales}, cadena de texto {string}, booleano{booleano},")

"""23. Escribir un programa que lea un entero positivo, n , introducido por el usuario y después
muestre en pantalla la suma de todos los enteros desde 1 hasta n . La suma de los n
primeros enteros positivos puede ser calculada de la siguiente forma:"""

n = int(input("Ingrese un numero entero positivo"))
suma = n * (n + 1) / 2
print(f"La suma de los primeros {n} numero es: {suma}")

"""24. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión"""

capital = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interes anual: "))
anual = int(input("Ingrese la cantidad de años: "))

interese = interes / 100 # pasar a decimal
capital_final = capital * (1 + interes) ** anual

print(f"El capital optenido es: {capital_final}")

"""25. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

#ingreso la cantidad de muñecas que encesito
payaso = int(input("Ingres la cantidad de payasos: "))
muñeca = int(input("Ingrese la cantidad de muñecas: "))
#calculo el peso de las muñecas por la cantidad q tengo
peso_total = (payaso * 112) + (muñeca * 75)
print(f"El peso total por todo es: {peso_total} gramos")

"""26. Una panadería vende una baguette a $50 cada una. La baguette que no es el día tiene un
descuento del 60%. Escribir un programa que comience leyendo el número de baguette
vendidas que no son del día. Después el programa debe mostrar el precio habitual de una
baguette , el descuento que se le hace por no ser fresca y el costo final total con descuento."""

precio_normal = 50
cantidad = int(input("Ingrese la cantidad de pan: "))
calidad = input("Que pan desea (fresco / viejo)").lower()

if calidad == "fresco":
    precio_final = precio_normal
    descuento = 0
else:
    descuento = precio_normal * 0.6
    precio_final = precio_normal - descuento

total = cantidad * precio_final

print(f"Percio habitual {precio_normal}")
print(f"Precio con descuento {descuento}")
print(f"Precio total de la compra {total}")
