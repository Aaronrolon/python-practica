#Cadenas(STRING).

#longitud: lend()
texto = "Universidad"
print(texto,"tiene",len(texto),"caracteres." )

"""Obtener un caracter de la cadena
● Acceder por nro de índice
● Un índice inexistente,
devuelve error
● Último índice (len()-1)
● Las cadenas son Inmutables"""

texto = "UNPAZ"
print(texto)
print(texto[0],texto[1],texto[2],texto[3],texto[4])

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])

print(texto[-1],texto[-2],texto[-3],texto[-4],texto[-5])

#Es posible fragmentar una cadena de distintas formas utilizando los índices.

#[:] Total
texto = "Universidad, Nacional de Jose c. Paz"
texto_nuevo = texto[:]
print(texto_nuevo)
#[Desde:]
texto_nuevo = texto[7:]
print(texto_nuevo)
#[:Hasta]
texto_nuevo = texto[:19]
print(texto_nuevo)
#[Desde:Hasta]
texto_nuevo = texto[7::2]
print(texto_nuevo)

"""Ejercitación.
Escribir un programa permita ingresar el total de prendas de una compra y muestre las
opciones de pago al cliente
Si comprá 1 unidad, puede pagar en efectivo
Si comprá 5 unidad, puede pagar con débito automático
Si comprá 20 unidades, puede pagar en 3 cuotas sin interés.
Si comprá 50 unidades, puede pagar en 6 cuotas sin interés.
Si comprá cualquier otra cantidad de prendas puede pagar con mercado pago
Si paga con tarjeta de crédito calcular y mostrar las cuotas a pagar según corresponda,
cada prenda vale $200, devuelva valores enteros(int)
Ejemplo: gasto total: 50
 “ud puede pagar en 6 cuotas de $ 1666”"""

prendas = int(input("Ingrese la cantidad de prendas que compro: "))
gastos = prendas * 200

match prendas :
    case 1:
        print("Puede abonar en efectivo")
    case 5:
        print("Puede abonar con debito")
    case 20:
        print(f"Puede abonar con tarjeta de credito en 3 cuotas de {int(gastos / 3)}")
    case 50:
        print(f"Puede abonar con tarjeta de credito en 6 cuotas de {int(gastos / 6)}")
    case _:
        print("Puede abonar con Mercado Pago")