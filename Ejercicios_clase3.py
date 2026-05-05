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
texto_nuevo = texto[7:2]
print(texto_nuevo)