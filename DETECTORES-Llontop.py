#Detector a alumno aprobado
# #Declaracion De Variables
nombre_de_alumno,codigo,nota1,nota2,nota3="","",0.0,0.0,0.0

#Input
nombre_alumno=input("Ingrese nombre del alumno:")
codigo=input("Ingrese codigo:")
nota1=float(input("Ingrese nota1:"))
nota2=float(input("Ingrese nota2:"))
nota3=float(input("Ingrese nota3:"))

#Processing
promedio=(nota1+nota2+nota3)/3

#Detector
#Sera aprobado cuando el promedio del alumno > 10.5
alumno_aprobado=(promedio > 10.5)

#Output
print("##########################")
print("#   PROMEDIO DE ALUMNO   #")
print("##########################")
print("# Nombre de alumno: ",nombre_alumno,"  #")
print("# Codigo: ",codigo," #")
print("# Nota1: ",nota1,"   #")
print("# Nota2: ",nota2,"   #")
print("# Nota3: ",nota3,"   #")
print("##########################")
print("# Promedio: ",promedio,"    #")
print("# Alumno aprobado: ",alumno_aprobado," #")
print("##########################")


#Detector a adolescentes para ingreso a discoteca
#Declaracion de variables
nombre_discoteca,nombre_de_adolescente,anio_actual,anio_de_nacimiento,edad="","",0,0,0

#Input
nombre_discoteca=input("Ingrese el nombre de discoteca:")
nombre_de_adolescente=input("Ingrese el nombre de adolescente:")
anio_actual=int(input("Ingrese anio actual:"))
anio_de_nacimiento=int(input("Ingrese anio de nacimiento:"))

#Processing
edad=anio_actual-anio_de_nacimiento

#Detector
#Ingresara a discoteca cuando el adolescente > 18
edad_aprobada=(promedio> 18)

#Output
print("###################")
print("#   ADOLESCENTES  #")
print("###################")
print("# Nombre de discoteca: ",nombre_discoteca,"  #")
print("# Nombre de adolescente: ",nombre_de_adolescente," #")
print("# Anio Actual: ",anio_actual,"   #")
print("# Anio de Nacimiento: ",anio_de_nacimiento,"   #")
print("##########################")
print("# Promedio: ",promedio,"    #")
print("# Edad Aprobada: ",edad_aprobada," #")
print("##########################")


#Detector maxima visita en lugar turistico de Lambayeque
#Declaracion de Variables
nombre_de_departamento,nro_de_visitas_museo_tumbas_reales,nro_de_visitas_bosque_de_pomac,nro_de_visitas_museo_bruning="",0,0,0

#Input
nombre_de_departamento=input("Ingrese nombre de departamento:")
nro_de_visitas_museo_tumbas_reales=int(input("Ingrese nro de visitas museo tumbas reales:"))
nro_de_visitas_bosque_de_pomac=int(input("Ingrese nro de visitas bosque de pomac:"))
nro_de_visitas_museo_bruning=int(input("Ingrese nro de visitas museo bruning:"))

#Processing
promedio=(nro_de_visitas_museo_tumbas_reales+nro_de_visitas_bosque_de_pomac+nro_de_visitas_museo_bruning)/3

#Detector
#Dia que haya alcanzado el mayor numero de turistas
cantidad_maxima=(promedio > 50)

#Output
print("#########################################################")
print("# PROMEDIO DE VISITAS A LUGARES TURISTICOS DE LAMBAYEQUE#")
print("#########################################################")
print("# Nombre de departamento: ",nombre_de_departamento,"  #")
print("# Nro de visitas Museo Tumbas Reales: ",nro_de_visitas_museo_tumbas_reales,"  #")
print("# Nro de visitas Bosque de Pomac: ",nro_de_visitas_bosque_de_pomac,"   #")
print("# Nro de visitas Museo Bruning: ",nro_de_visitas_museo_bruning,"   #")
print("#########################################################")
print("# Promedio: ",promedio,"    #")
print("# Cantidad Maxima: ",cantidad_maxima," #")
print("#########################################################")


#Detectar el anio en que hubo mas gastos en el hogar
#Declaracion de Variables
gastos_anio2005,gastos_anio2006,gastos_anio2007,total=0.0,0.0,0.0,0.0

#Input
gastos_anio2005=float(input("Ingrese gastos anio2005:"))
gastos_anio2006=float(input("Ingrese gastos anio2006:"))
gastos_anio2007=float(input("Ingrese gastos anio2007:"))

#Processing
total=(gastos_anio2005+gastos_anio2006+gastos_anio2007)

#Detector
#Anio en el que hubo mas gastos en el hogar > 72000
hogar_compulsivo=(total > 72000)

#Output
print("##################################")
print("# PROMEDIO DE GASTOS EN UN HOGAR #")
print("##################################")
print("# Gastos anio2005: ",gastos_anio2005,"  #")
print("# Gastos anio2006: ",gastos_anio2006,"  #")
print("# Gastos anio2007: ",gastos_anio2007,"  #")
print("##################################")
print("# Total: S/. ",total,"    #")
print("# Hogar Compulsivo: ",hogar_compulsivo,"  #")
print("##################################")


#Detectar consumo de bebidas alcoholicas
#Declaracion De Variables
consumidor,nro_cervezas,nro_champagne,nro_vodka,total="",0,0,0,0

#Input
consumidor=input("Ingrese nombre consumidor")
nro_cervezas=int(input("Ingrese nro cervezas:"))
nro_champagne=int(input("Ingrese nro champagne:"))
nro_vodka=int(input("Ingrese nro vodka:"))

#Processing
total=(nro_cervezas+nro_champagne+nro_vodka)

#Detector
#Sera alcoholico cuando consuma > 100 botellas
alcoholico=(total > 100)

#Output
print("##################################")
print("# CONSUMO DE BEBIDAS ALCOHOLICAS #")
print("##################################")
print("# Consumidor : ",consumidor,"  #")
print("# Nro cervezas: ",nro_cervezas,"        #")
print("# Nro champagne: ",nro_champagne,"       #")
print("# Nro vodka: S/. ",nro_vodka," #")
print("##################################")
print("# Total: ",total,"      #")
print("# Alcoholico: ",alcoholico,  "#")
print("###########################")

#Detectar el sueldo minimo de un empleado
#Declaracion de variables
empleado,nrodias,costo,horas_extra,total="",0,0.0,0,0.0

#INPUT
empleado=input("Ingrese el nombre del empleado:")
nrodias=int(input("Ingrese nro de dias:"))
costo=float(input("Ingrese costo por dia:"))
horas_extra=int(input("Ingrese nro de horas extras:"))

#PROCESSING
total=(nrodias*costo)+(horas_extra*50)

#DETECTOR
#Sera empleado con el sueldo minimo > 930
empleado_sueldo_minimo =(total > 930)

#OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Empleado : ",empleado,"   #")
print("# NroDias   : ",nrodias,"          #")
print("# CostoxDia : ",costo,"         #")
print("# HorasExtra: ",horas_extra,"           #")
print("###########################")
print("# Total : ",total,"     #")
print("# Empleado Sueldo Minimo : ", empleado_sueldo_minimo,"  #")
print("###########################")

#Detectar si hay mas de 100 ninios en el nido "rosario"
#Declaracion De Variables
nombre_de_ninio,nro_ninios_de_tres_anios,nro_ninios_de_cuatro_anios,nro_ninios_de_cinco_anios="",0,0,0

#Input
nombre_de_ninio=input("Ingrese nombre de ninio:")
nro_ninios_de_tres_anios=int(input("Ingrese el nro ninios de tres anios:"))
nro_ninios_de_cuatro_anios=int(input("Ingrese el nro ninios de cuatro anios:"))
nro_ninios_de_cinco_anios=int(input("Ingrese el nro ninios de cinco anios:"))

#Processing
total_de_alumnos=(nro_ninios_de_tres_anios+nro_ninios_de_cuatro_anios+nro_ninios_de_cinco_anios)

#Detectar
#Sera un exceso de ninios > 100
exceso_de_ninios=(total > 100)

#Output
print("#########################")
print("# CANTIDAD DE ALUMNOS   #")
print("#########################")
print("# Nombre de ninio: ",nombre_de_ninio,"  #")
print("# Nro Ninios de Tres Anios: ",nro_ninios_de_tres_anios,"   #")
print("# Nro Ninios de Cuatro Anios: ",nro_ninios_de_cuatro_anios,"   #")
print("# Nro Ninios de Cinco Anios: ",nro_ninios_de_cinco_anios,"   #")
print("#########################")
print("# Total: ",total," #")
print("# Exceso de Ninios: ",exceso_de_ninios,"  #")
print("#########################")


#Detectar de consultora conpulsiva
consultora,nro_de_pedidos,costo_de_venta,nro_de_clientes="",0,0.0,0

#INPUT
consultora=input("Ingrese el nombre de consultora:")
nro_de_pedidos=int(input("Ingrese nro de pedidos:"))
costo_de_venta=float(input("Ingrese el costo de venta:"))
nro_de_clientes=int(input("Ingrese el nro de:"))

#PROCESSING
ingreso_total=(nro_de_pedidos*costo_de_venta)

#Detector
#Sera consultora compulsivo cuando el total > 350
consultora_compulsivo=(total > 350)

#OUTPUT
print("###########################")
print("#     INGRESO TOTAL       #")
print("###########################")
print("# Consultora: ",consultora,"   #")
print("# NroDePedidos : ",nro_de_pedidos,"          #")
print("# CostoDeVenta : ",costo_de_venta,"         #")
print("# NroDeClientes: ",nro_de_clientes,"           #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# Consultora Compulsivo: ",consultora_compulsivo,  "#")
print("###########################")

#Detector de empleado compulsivo
empleado,nro_dias,costo,horas_extra,monto="",0,0.0,0,0.0

#INPUT
empleado=input("Ingrese el nombre del empleado:")
nro_dias=int(input("Ingrese nro de dias:"))
costo=float(input("Ingrese costo por dia:"))
horas_extra=int(input("Ingrese nro de horas extras:"))

#PROCESSING
monto=(nrodias*costo)+(horas_extra*50)

#DETECTOR
#Sera empleado compulsivo > 7000
empleado_compulsivo=(monto > 7000)

#OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Empleado: ",empleado,"   #")
print("# NroDias   : ",nrodias,"          #")
print("# CostoxDia : ",costo,"         #")
print("# HorasExtra: ",horas_extra,"           #")
print("###########################")
print("# Monto: S/. ",monto,"      #")
print("# Empleado Compulsivo: ",empleado_compulsivo,  "#")
print("###########################")


#Detector de ganancia promedio de un vendedor
#Declaracion de variables
cantidad_jugo_surtido,cantidad_jugo_especial,cantidad_jugo_naranja,cantidad_jugo_platano,costo_por_vaso,monto_total=0,0,0,0,0.0,0.0

#Input
cantidad_jugo_surtido=int(input("Ingrese la cantidad jugo surtido:"))
cantidad_jugo_especial=int(input("Ingrese la cantidad de jugo especial:"))
cantidad_jugo_naranja=int(input("Ingrese la cantidad de jugo naranja:"))
cantidad_jugo_platano=int(input("Ingrese la cantidad de jugo platano:"))
costo_por_vaso=float(input("Ingrese el costo por vaso:"))

#Processing
monto_total=((cantidad_jugo_surtido+cantidad_jugo_especial+cantidad_jugo_naranja+cantidad_jugo_platano)*costo_por_vaso)

#Dara ganancia cuando el monto total > 1500
ganancia=(monto_total > 1500)

#Output
print("######################")
print("# FICHA MONTO TOTAL  #")
print("######################")
print("# Cantidad jugo surtido: ",cantidad_jugo_surtido,"  #")
print("# Cantidad jugo especial ",cantidad_jugo_especial,"  #")
print("# Cantidad jugo naranja: ",cantidad_jugo_naranja,"   #")
print("# Cantidad jugo platano: ",cantidad_jugo_platano,"   #")
print("#########################################################")
print("# Monto total: ",monto_total,"    #")
print("# Ganancia:",ganancia,"       #")
print("#########################################################")


