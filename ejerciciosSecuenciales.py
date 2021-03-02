# Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.
print('Inversionista uno')
personaUno = float(input('Ingresar su inversion: '))
print('Inversionista dos')
personaDos = float(input('Ingresar su inversion: '))
print('Inversionista tres')
personaTres = float(input('Ingresar su inversion: '))
capital = personaUno + personaDos + personaTres
porcentajeUno = (personaUno / capital) * 100
porcentajeDos = (personaDos / capital) * 100
porcentajeTres = (personaTres / capital) * 100
print(f'La inversion de la primera persona fue de un {porcentajeUno}% ')
print(f'La inversion de la segunda persona fue {porcentajeDos}% ')
print(f'Le inversion de la tercera persona fue {porcentajeTres}% ')
print(f'La inversion total fue: ${capital:,}')

# Una empresa paga a sus empleados además del sueldo base una
# bonificación especial de $80.000 por cada hijo. Realice un programa
# en Java que determine el monto de la bonificación y el monto total a
# pagar al trabajador.
sueldoBase = float(input('Ingrese sueldo base: '))
numHijos = int(input('Ingrese la cantidad de hijos que tiene: '))
bono = 80000
bonoTotal = bono * numHijos
sueldo = sueldoBase + bonoTotal
print(f'Su bonificacion fue de: ${bonoTotal:,}')
print(f'Su sueldo fue de: ${sueldo:,}')

# Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.
saldoInicial = float(input('Ingrese saldo inial: '))
intereses = saldoInicial * 0.015
saldoFinal = saldoInicial + intereses
print(f'Su saldo es: ${saldoFinal}')
# Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
# cliente debe dar una cuota inicial del 35%y el resto lo paga en 12
# cuotas. Determine el valor a pagar por cuota inicial y el monto de
# cada cuota.
terreno = 80000
hectareas = int(input('Ingrese la cantidad de hectareas adquiridas: '))
precio = terreno * hectareas
cInicial = precio * 0.35
cuotas = (precio - cInicial) / 12
print(f'Su cuota inicial sera ${cInicial:,}')
print(f'El resto de sus cuotas seran ${cuotas:,}')
# Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# programa en Java que determine el monto de cada descuento y el
# monto total a pagar al trabajador
sueldoBase = float(input('Ingresar sueldo base: '))
descuentoLey = sueldoBase * 0.01
seSocial = sueldoBase * 0.04
seForzoso = sueldoBase * 0.005
cAhorro = sueldoBase * 0.05
suTotal = sueldoBase - descuentoLey - seSocial - seForzoso - cAhorro
print(f'Descuento por ley de politicas publicas ${descuentoLey:,}')
print(f'Descuento por seguro social ${seSocial:,}')
print(f'Dscuento por seguro Forzoso ${seForzoso:,}')
print(f'Descuento por caja de ahorro ${cAhorro:,}')
print(f'Sueldo total ${suTotal:,}')
# El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.
palabras = int(input('Ingrese la cantidad de palabras: '))
centimetro = int(input('Ingrese el tamaño: '))
color = int(input('Ingrese la cantidad de colores: '))
tPalabra = palabras * 20000
tCentimetro = centimetro * 15000
tColor = color * 25000
total = tPalabra + tCentimetro + tColor
print(f'Total a pagar ${total:,}')
# Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un programa en Java que determine el monto
# del bono a pagar a un trabajador que tiene varios años en la empresa.
antiguedad = int(input('Ingrese el tiempo que lleva en la empresa: '))
bono = (antiguedad - 1) * 120000
total = bono + 100000
print(f'Su bono es de ${total:,}')
# Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.
numHoras = int(input('Ingrese la cantidad de horas trabajadas: '))
hora = numHoras * 20000
cajaAhorro = hora * 0.05
sueldo = hora - cajaAhorro
print(f'Descuento por caja de ahorro ${cajaAhorro:,}')
print(f'Total a pagar ${sueldo:,}')
# Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.
mInicial = float(input('Ingrese saldo de la tarjeta: '))
mFinal = float(input('Ingrese el saldo final: '))
consumo = mInicial - mFinal
recargo = consumo * 0.2
monto = consumo + recargo
print(f'El total a pagar es: ${monto}')
# En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un programa en Java que determine el monto a pagar
# por un revelado completo sabiendo que adiconalmente le cobran el
# IVA (16%).
cantidad = float(input('Ingrese la cantidad de fotos: '))
precio = 1500
foto = precio * cantidad
iva = foto * 0.16
total = foto + iva
print(f'Precio sin Iva ${foto:,}')
print('Aplicantole el iva del 16%')
print(f'El total a pagar es ${total:,}')
# Ejercicio 11
presupuesto = float(input('Ingrese el presupuesto anual: '))
ginecologia = presupuesto * 0.4
traumatologia = presupuesto * 0.3
pediatria = presupuesto * 0.3
print(f'El presupuesto para Ginecologia es ${ginecologia:,}')
print(f'El presupuesto para Traumatologia es ${traumatologia:,}')
print(f'El presupuesto para Pediatria es ${pediatria:,}')
# Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# programa en Java que teniendo como dato de entrada el total de
# películas alquiladas, y el número de días de alquiler, determine el
# monto a pagar.
precio = 1500
nPeliculas = int(input('Ingrese la cantidad de peliculas: '))
nDias = int(input('Ingrese el numero de dias: '))
alquiler = precio * nDias * nPeliculas
promocion = alquiler - (precio * nDias)
print(f'El total a pagar es ${promocion:,}')
# Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un programa en Java que determine el
# monto a pagar por una familia que desee realizar dicho Tour
# sabiendo que también cobran el 12% de IVA.
precio = 25000
nPersonas = int(input('Ingrese el numero de personas: '))
nDias = int(input('Ingrese el numero de dias: '))
tour = precio * nPersonas * nDias
iva = tour * 0.12
total = tour + iva
print(f'El total a pagas es ${total:,}')
# Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un programa en Java que determine
# el valor total a pagar por la habitación si la estadía fue de varios
# días.
dias = int(input('Ingrese numero de dias: '))
habitacion = (dias - 1) * 200000
total = habitacion + 100000
print(f'El total a pagar es ${total:,}')
# El banco del Pueblo da microcréditos a empresarios para ser
# cancelados en un lapso de 2 años (24 meses). Al monto del
# préstamo se le cobra un interés del 24%. El empresario debe pagar
# la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
# cuotas ordinarias. Realice un algoritmo que teniendo como dato de
# entrada el monto del préstamo, determine el monto total a pagar por
# el préstamo, el monto de las cuotas especiales y el monto de las
# cuotas ordinarias.
mInicial = float(input('Ingrese el monto de su prestamos: '))
intereses = (mInicial * 0.24) + mInicial
mitad = intereses / 2
pCuotas = mitad / 4
uCuotas = mitad / 20
print(f'El monto de las cuatro primeras cuotas es ${pCuotas:,}')
print(f'Sus cuotas ordinarias seran de ${uCuotas:,}')
print(f'El monto total es ${intereses:,}')
