#primer python
"""
#ejercicio 1:
print("hola mundo.")

#ejercicio 2
computador= 'hola mundo.'
print(computador)

#ejercicio 3
name=input("¿Cual es tu nombre ")
print (" Hola " + name + " es un placer! ")

#ejercicio 4
print (((3+2)/(2*5))**2)

#ejercicio 5
ht=float (input("escribe tus horas trabajadas "))
ch=float(input("escribe el costo por hora "))
valor= (ht*ch)
print (valor)

#ejercicio 6
N=int(input("escribe un entero positivo "))
print (N*(N+1)/2)

#ejercicio 7 
peso=float(input("introduzca su peso en KG aqui: "))
estatura=float(input("introduzca su estatura en metros aqui: "))
imc=round(peso/estatura**2,2)
print("tu indice de masa corporal es ", imc)

#ejercicio 8
n= int(input("introduzca un numero entero: "))
m= int(input("introduzca otro numero entero: "))
d= n/m
c= n//m
r= n%m
print("el resultado de la division es: ",d,", el residuo es :",r,",su cociente es:",c)

#ejercicio 9
inversion=float(input("cantidad a invertir: "))
ia=float(input("el interes anual es: "))
años=float(input("el numero de años invertido es: "))
formula= inversion*(ia/100+1)**años
print("el capital obtenido: ", formula)

#ejercicio 10
pp=int(input("cuantos payasos quieres pedir: "))
pm=int(input("cuantas muñecas quieres pedir: "))
formula= (pp*112)+(pm*75)
print("el peso total del paquete es", formula,"g")
"""