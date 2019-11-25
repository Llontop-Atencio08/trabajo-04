#EJERCICIO01
# Conversion de datos con I/O (I=Input/O=Output)
alumno,curso,nota1,nota2,nota3="","",0.0,0.0,0.0
prom_final=0.0

# INPUT
alumno=input ("Ingrese el alumno:")
curso=input ("Ingrese el curso:")
nota1=float(input("Ingrese nota1:")) # input() devuelve un str
nota2=float(input("Ingrese nota2:"))
nota3=float(input("Ingrese nota3:"))

# PROCESSING
prom_final=(nota1+nota2+nota3)/3
# unsupported operand type(s) for /: 'str' and 'int'

# OUTPUT
print("El promedio final del ",alumno," es:",prom_final)


#EJERCICIO02
# Declaracion variables
obrero,empresa,nrodias,costo,horas_extra,asignacion_familar="","",0,0.0,0,0.0
monto=0.0

# INPUT
obrero="MARIA TORRES"
empresa="GANDULES"
nrodias=7
costo=100.5
horas_extra=3
asignacion_familar=20.0

# PROCESSING
monto=(nrodias*costo)+(horas_extra*15)+(asignacion_familar)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Obrero: ",obrero,"   #")
print("# Empresa  : ",empresa,"          #")
print("# Nro de dias  : ",nrodias,"          #")
print("# CostoxDia : ",costo,"         #")
print("# HorasExtra: ",horas_extra,"           #")
print("# Asignacion familiar : ",asignacion_familar,"          #")
print("###########################")
print("# Monto a Pagar: ",monto,"     #")
print("###########################")

#EJERCICIO03
# Convertir la cadena "74662380" en entero
x="74662380"
a=int(x) # int("74662380")
print(a, type(a))

#EJERCICIO04
# Conversion de datos con I/O (I=Input/O=Output)
paciente,peso,talla="",0.0,0.0
total_de_imc=0.0

# INPUT
paciente=input ("Ingrese el paciente:")
peso=float(input("Ingrese peso:"))
talla=float(input("Ingrese talla:"))

# PROCESSING
total_de_imc= peso/(talla*talla)
# unsupported operand type(s) for /: 'str' and 'int'

# OUTPUT
print("El  total de imc del ",paciente," es:",total_de_imc)


#EJERCICIO05
# Declaracion variables
estudiante,universidad,ciclo,nota_curso1,nota_curso2,nota_curso3="","","",0.0,0.0,0.0
promedio_final=0.0

# INPUT
estudiante="JIMMY CUEVA"
universidad="PEDRO RUIZ GALLO"
ciclo="DECIM0"
nota_curso1= 18
nota_curso2=19
nota_curso3=19

# PROCESSING
promedio_final= (nota_curso1+nota_curso2+nota_curso3)/3

# OUTPUT
# OUTPUT
print("###########################")
print("#     FICHA DE TERCIO SUPERIOR     #")
print("###########################")
print("# Estudiante : ",estudiante,"  #")
print("# Universidad: ",universidad,"        #")
print("# Ciclo: ",ciclo,"           #")
print("# Nota curso1: ",nota_curso1,"   #")
print("# Nota curso2: ",nota_curso2,"     #")
print("# Nota curso3:",nota_curso3,"    #")
print("###########################")
print("# Promedio final:  ",promedio_final,"      #")
print("###########################")
