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

#ejercicio 11

inversion= float(input("introduce la inversion inicial: "))
intereses= 0.04
balance1= inversion * (1+intereses)
print("balance tras el primer año: " + str(round(balance1, 2)))
balance2= balance1 * (1+intereses)
print("balance tras el segundfo año: " + str(round(balance2,2)))
balance3= balance2* (1+intereses)
print("balance tras el tercer año: " + str(round(balance3,2)))

#ejercicio 12

pan= int(input("introduce el numero de panes vendidos que no son frescos: "))
precio= 3000
descuento= 0.4
costo= pan * precio * (1-descuento)
print("el costo de un pan fresco es: " + str(precio) + "$")
print("el descuento sobre un pan no fresco es: " + str(descuento*100) + "%")
print("el costo final a pagar es: " + str(round(costo,2)) + "$")

#segundo python

#ejercicio 1

print("introduce un numero entero: ")
N=int(input())
S=((N*(N+1)/2))
if S > 20:print(S, "es un gran numero! ")
else: print("la suma de todos los enteros desde 1 hasta",N, "es",S,"asi que NO es un gran numero")

#ejercicio 2

print("escriba un numero entero: ")
N = int(input())
print("escriba otro numero entero")
M = int(input())
C = (N / M)
R = (N * M)
print("el cociente es", C)
print("el residuo es", R)
if C < 1: print("el divisor es mayor al dividendo")
if C > 1: print("el divisor es menor que el dividendo")
if C == 1: print("el divisor y el dividendo son iguales")

#ejercicio 3

print("ingrese la cantidad que desea invertir ")
c=float(input())
print("ingrese el interes anual ")
i=float(input())
print("ingrese el numero de años: ")
a=float(input())
cap=(c*(i/100)**a)
if cap<100000: print("la inversion de", c, "tiene baja rentabilidad")
if cap>100000 and cap<1000000: print("la inversion de ", c , "tiene una rentabilidad moderada")
if cap>1000000: ("la inversion de ", c, "es una buena inversion")

#ejercicio 4
print("numero de payasos vendidos")
p=int(input())
print("numero de muñecas vendidas")
m=int(input())
s="si"
pg=p*112
kg=s*75
pesototal=pg+kg
if pesototal>3000000:
  print("desea enviarlo? ")
  h=input()
  if h==s: print("contenedor enviado")
  else: print("contenedor no enviado")
else: print("el peso total del pedido",pesototal)

#tercer python

#ejercicio 1

def suma (a,b):
  print(a+b)
  return a+b
print("escribe un numero")
a=int(input())
print("escribe otro numero ")
b=int(input())
suma(a,b)

#ejercicio 2

def resta (a,b):
  print(a-b)
  return a-b
print("escribe un numero")
a=int(input())
print("escribe otro numero ")
b=int(input())
resta (a,b)

#ejercicio 3

def multiplicacion (a,b):
  print(a*b)
  return a*b
print("escribe un numero")
a=int(input())
print("escribe otro numero ")
b=int(input())
multiplicacion (a,b)

#ejercicio 4

def division (a,b):
  print(a/b)
  return a/b
print("escribe un numero")
a=int(input())
print("escribe otro numero ")
b=int(input())
division (a,b)

#ejercicio 5

def suma(a,b):
  return a+b

def resta(a,b):
  return a-b

def multiplicacion(a,b):
  return a*b

def division(a,b):
  print(a/b)
  if a ==0:
     return a/b
  else:
     return("no es posible dividir por cero")

print("calculadora simple")
print("operaciones simples")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

opcion = input("seleccione una operacion (1/2/3/4): ")
num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))

if opcion =="1":
  print("el resultado es: ", suma(num1, num2))
elif opcion=="2":
  print("el resultado es: ", resta(num1, num2))
elif opcion=="3":
  print("el resultado es: ", multiplicacion(num1, num2))
elif opcion=="4":
  print("el resultado es: ", division(num1, num2))
else:
  print("opcion invalida. Por favor ingrese una operacion valida.")
  
#ejercicio 6
def intereses(inv):
  d= inv
  if (d>0 and d<1000000):
   return 2
  elif(d>=1000000 and d<2000000):
   return 5
  else:
   return 7
   
def calBalance(int, inv):
  n=int
  d=inv
  return round((d*(1+(n/100))),2 )

def ctaAhorro():
  #inversion, interes, b1,b2,b3 =0.0
  inversion=float(input("ingrese el valor de la inversion: "))
  interes=intereses(inversion)
  b1=calBalance(interes, inversion)
  b2=calBalance(interes,b1)
  b3=calBalance(interes, b2)
  print("balance año 1: " + str(b1) + "balance año 2: " + str(b2) + "balance año 3: " + str(b3))
  
ctaAhorro()

#cuarto python

#ejercicio 1
def areatriangulo(b,a):
  return(b*a)/2

def areacuadrado(bc,ac):
  return bc*ac

def areacirculo(r):
  return(3.14169*(r**2))

def areafig():

 area=0.0
 figura=""
 figura = input("escriba la figura a la que se le desea calcular el area: ") 
 figura.lower()

 if (figura.lower()=="triangulo"):
   base=0.0
   altura=0.0
   base= float(input("ingrese la base: "))
   altura=float(input("ingrese la altura: "))
   area=areatriangulo(base,altura)
   print("el area del triangulo es: ", area)

  elif (figura.lower()=="cuadrado"):        
  base=0.0
  area=0.0
  base=float(input("ingrese la base: "))
  area=float(input("ingrese el area: "))
  print("el area del cuadrado es: ", area)

else (figura.lower()=="circulo"):
pi=3.14169
area=0.0
area=float

#ejercicio 3

def maximo(a,b):
  if a>b:
    return a
  else:
    return b

def minimo(a,b):
 if a<b:
  return a
 else: 
  return b

#programa principal (mala practica)
a=int(input("un numero: "))
b=int(input("otro numero: "))
print(maximo(a-3, minimo(a+2, b-5)))
"""   
#ejercicio 4

preciosiniva=2000000
marca= "NOSY"
iva= 0.20
if preciosiniva>= 2000000:
  descuentoporcentaje=0.10
  if marca == "NOSY":
    descuentoporcentaje+=0.05
  else:descuentoporcentaje=0

descuento=preciosiniva*descuentoporcentaje
preciocondescuento=preciosiniva-descuento
precioconiva=preciocondescuento*(1+iva)

print("el precio a pagar con iva incluido es: ", precioconiva)







