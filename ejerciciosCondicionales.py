import random
import statistics as stats
# Ejercicios condicionales

# Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

print('Le damos la bienvenida a nuestra tienda')
print('1. Camisa: $20000')
print('Descuentos')
print('Por la compra de tres o más camisas tendra el 30%')
print('Por compras inferiores tendra un 10%')
precio = 20000
cantidad = int(input('Ingrese la cantidad: '))
if cantidad >= 3:
    subtotal = precio * cantidad
    descuento = subtotal * 0.3
    total = subtotal - descuento
    print(f'La cantidad de productos adquiridos fue {cantidad}')
    print('Se le aplico un descuento del 30% a su compra')
    print(f'El total a pagar es: ${total}')
elif cantidad < 3:
    subtotal = precio * cantidad
    descuento = subtotal * 0.1
    total = subtotal - descuento
    print(f'La cantidad de productos adquiridos fue {cantidad}')
    print('Se le aplico un descuento del 10% a su compra')
    print(f'El total a pagar es: ${total}')


# En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

print('Le damos la bienvenida a nuestra tienda')
print('Como nos gusta concentir a nuestros clientes')
print('hoy tendremos una dinamica con todos ustedes')
print('en la cual tendran descuentos del 15% y el 20%')
print('en el total de sus compras')
print('lo unico que debe hacer, es estar atento al numero')
print('que se escogera al azar')
numero = random.randint(1, 100)
subtotal = float(input('Ingrese el total de su compra: '))
print(f'Su numero es: {numero}')
if numero < 74:
    descuento = subtotal * 0.15
elif numero >= 74:
    descuento = subtotal * 0.2
print(f'Usted tuvo un descuento de ${descuento}')

# Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que consite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al cliente.
print('Bienvenido al departamento de finanzas')
monto = float(input('Ingrese el monto total: '))
if monto < 50000:
    cuota = monto * 0.03
elif monto > 50000:
    cuota = monto * 0.02
print(f'Su cuota a pagar es: ${cuota}')

# Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.
print('Bienvenidos al programa de control de contaminacion')
lunes = int(input('Ingrese el nivel de contaminación: '))
martes = int(input('Ingrese el nivel de contaminación: '))
miercoles = int(input('Ingrese el nivel de contaminación: '))
jueves = int(input('Ingrese el nivel de contaminación: '))
viernes = int(input('Ingrese el nivel de contaminación: '))
dias = [lunes, martes, miercoles, jueves, viernes]
promedio = stats.mean(dias)
print(f'su promedio fue: {promedio}')
ganancia = float(input('Ingrese la ganancia diaria: '))
if promedio > 170:
    subtotal = ganancia * 0.5
    multa = ganancia - subtotal
    print('¡Tiene altos niveles de contaminación!')
    print('Debe suspender su producción por una semana')
    print(f'Usted debera pagar: ${multa}')
else:
    print('Tiene bajos niveles de contaminación')

# Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.
precio = float(input('Ingrese el valor total: '))
devaluacionCarro = precio * 0.3
incrementoCasa = precio * 0.126
mitad = incrementoCasa / 2
if devaluacionCarro < mitad:
    print('Le recomiendo adquirir el automovil')
else:
    print('No es recomendable comprar el automovil')
    print('Le recomiendo mejor adquirir el terreno')

# En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.

print('Bienvenidos')
print('1. Computadora= $11000')
precio = 11000
cantidad = int(input('Ingrese la cantiodad de computadoras: '))
subtotal = precio * cantidad
if cantidad < 5:
    descuento = subtotal * 0.1
elif cantidad >= 5 and cantidad < 10:
    descuento = subtotal * 0.2
else:
    descuento = subtotal * 0.4
total = subtotal - descuento
print(f'Su descuento fue de: ${descuento}')
print(f'El valor total de su compra es: ${total}')

# Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.
print('Bienvenidos')
articulo = float(input('Ingrese el valor del articulo (sin IVA): '))
print('¿La marca del producto es Nosy?')
print('Escribir:')
print('0. no')
print('1. si')
nosy = int(input(''))
descuento = 0
descuentoNosy = 0
if articulo >= 2000:
    descuento = articulo * 0.1
if nosy == 1:
    descuentoNosy = articulo * 0.05
iva = articulo * 0.16
total = articulo - descuento - descuentoNosy + iva
print(f'El valor total es: ${total}')

# Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.000 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses.

piezas = float(input('Ingrese el monto total de su compra: '))
if piezas > 500000:
    inversion = piezas * 0.55
    prestamoBanco = piezas * 0.3
    credito = piezas * 0.15
else:
    inversion = piezas * 0.7
    prestamoBanco = 0
    credito = piezas * 0.3
intereses = credito * 0.2
print(f'La cantidad a invertir fue: ${inversion}')
print(f'El valor del prestamo fue: ${prestamoBanco}')
print(f'El valor del credito fue: ${credito}')
print(f'Los intereses fueron: ${intereses}')

# Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume.
numeroUno = int(input('Ingrese un numero: '))
numeroDos = int(input('Ingrese un numero: '))
if numeroUno == numeroDos:
    total = numeroUno * numeroDos
elif numeroUno > numeroDos:
    total = numeroUno - numeroDos
else:
    total = numeroUno + numeroDos
print(f'El resultado es: {total}')

# Leer tres números diferentes e imprimir el número mayor de los
# tres.
numeroUno = int(input('Ingrese un numero: '))
numeroDos = int(input('Ingrese un numero: '))
numeroTres = int(input('Ingrese un numero: '))
if numeroUno > numeroDos and numeroUno > numeroTres:
    print(f'El numero mayor es: {numeroUno}')
elif numeroDos > numeroUno and numeroDos > numeroTres:
    print(f'El numero mayor es: {numeroDos}')
else:
    print(f'El numero mayor es: {numeroTres}')

