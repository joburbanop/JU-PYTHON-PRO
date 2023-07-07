#--------------------METODOLOGIAS AGILES-----------------------
#Una metodología ágil es una forma de trabajar en proyectos de una manera flexible y colaborativa. se trabaja por etapas y se hace una retroalimentacion 
# a lo largo de este curso trabajaremos en base a una metologia algil llamada scrumm entonces Scrum es una metodología de trabajo en equipo que 
#se utiliza en muchos proyectos, especialmente en el desarrollo de software y juegos. 

#------------------ INTERPRETES-------------------------
#¿cómo los ordenadores entienden lo que les decimos con nuestro código? 
#los ordenadores solo pueden entender un tipo de lenguaje muy básico llamado código máquina este codigo maquina. 
#este codigo Utiliza el alfabeto binario, que consta de los dos únicos símbolos 0 y 1, denominados bits. 
#Para que un ordenador entienda y ejecute un programa, el código debe traducirse primero a código máquina, que es una representación binaria de las instrucciones. 
#El intérprete es como un traductor especial que toma el código que escribimos en un lenguaje de programación fácil de entender, como Python,
# y lo traduce al código máquina que los ordenadores pueden entender.

#----------------IDE (Entorno de Desarrollo Integrado)------------------------
#Un IDE es un programa que nos proporciona una interfaz amigable donde podemos escribir y editar nuestro código de una manera más fácil.}
#exiaten muchos ides

#----------------CODIGO DE CLASE----------------------

import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Introduce la longitud de la contraseña: "))

password = ""

for _ in range(length):
    password += random.choice(characters)
print("Contraseña generada:", password)

#-------------------RETO DE CLASE------------------------------
#PRIMER RETO 
#verifica si una frase es un palíndromo e imprimir un mensaje indicando el resultado.

#SEGUNDO RETO (serie de Fibonacci)
#)El reto consiste en escribir un programa en Python que genere los primeros N números de la serie de Fibonacci y los imprima en pantalla.
#La serie de Fibonacci comienza con los números 0 y 1, y cada número siguiente se obtiene sumando los dos números anteriores.
#Por ejemplo, los primeros 10 números de la serie son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

#------------------------RETO PARA LA CASA----------------------
#El reto consiste en escribir un programa en Python que encuentre el número de Fibonacci más cercano a un número objetivo dado por el usuario.
#EJEMPLO DE ENTRADA Y SALIDA
#entrada-> Ingrese el número objetivo: 10
#salida -> El número de Fibonacci más cercano a 10 es 8

