# Conversion de datos con I/O (I=Input/O=Output)
ninio,examen1,examen2,examen3="",0,0,0
promedio=0.0

# INPUT
ninio=input("Ingrese nombre ninio:")
examen1=int(input("Ingrese examen 1:")) # input() devuelve un str
examen2=int(input("Ingrese examen 2:"))
examen3=int(input("Ingrese exmanen 3:"))

# PROCESSING
promedio=(examen1+examen2+examen3)/3
# unsupported operand type(s) for /: 'str' and 'int'

# OUTPUT
print("El promedio del ",ninio," es:",promedio)


#Conversion de datos con I/O (I=Input/O=Output)
cliente,producto1,producto2,producto3="",0.0,0.0,0.0
total=0.0

#Input
cliente=input("Ingrese nombre cliente:")
producto1=float(input("Ingrese producto1:")) #input() devuelve un str
producto2=float(input("Ingrese producto2:"))
producto3=float(input("Ingrese producto3:"))

#Processing
total=(producto1+producto2+producto3)
#unsupported operand type (s) for /: 'str' anda 'float'

#Output
print("El total de ",cliente," es:",total)


#Conversion de datos con I/O (I=Input/O=Output)
vendedor,semana1,semana2,semana3,semana4="",0.0,0.0,0.0,0.0
total=0.0

#Input
vendedor=input("Ingrese nombre vendedor:")
semana1=float(input("Ingrese semana1:")) #input() devuelve un int
semana2=float(input("Ingrese semana2:"))
semana3=float(input("Ingrese semana3:"))

#Processing
total=(semana1+semana2+semana3+semana4)
#unsupported operand type (s) for/: 'str' and 'int'

#Output
print("El total de ",vendedor," es:",total)


#Conversion de datos con I/O (I=Input/O=Output)
colegio,seis_anios,siete_anios,ocho_anios="",0,0,0
promedio=0

#Input
colegio=input("Ingrese colegio:")
seis_anios=int(input("Ingrese seis anios:"))
siete_anios=int(input("Ingrese siete anios:"))
ocho_anios=int(input("Ingrese ocho anios:"))

#Processing
promedio=(seis_anios+siete_anios+ocho_anios)/3
#unsupported operand type (s) for/: 'str' and 'int'

#Output
print("El promedio de ",colegio," es:",promedio)


# Convertir la cadena "1875" en un entero
x="1875"
a=int(x)
print(a, type(a))

