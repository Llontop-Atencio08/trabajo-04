#Calcular el sueldo de un empleado
#Nro de dias trabajados x costo de dia
#Se les sumas las horas extras, cada hora extra vale 50 soles
#Mostrar la boleta de pago

#Declaracion de variables
empleado,nrodias,costo,horas_extra,monto="",0,0.0,0,0.0

#INPUT
empleado=input("Ingrese el nombre del empleado:")
nrodias=int(input("Ingrese nro de dias:"))
costo=float(input("Ingrese costo por dia:"))
horas_extra=int(input("Ingrese nro de horas extras:"))

#PROCESSING
monto=(nrodias*costo)+(horas_extra*50)

#OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Empleado: ",empleado,"   #")
print("# NroDias   : ",nrodias,"          #")
print("# CostoxDia : ",costo,"         #")
print("# HorasExtra: ",horas_extra,"           #")
print("###########################")
print("# Monto a Pagar: ",monto,"     #")
print("###########################")

#Calcular el ingreso total de pedido Natura
#Consultora
#Nro de pedidos
#Costo de venta del producto
#Nro de clientes en el ciclo


#Declaracion de variables
consultora,nro_de_pedidos,costo_de_venta,nro_de_clientes="",0,0.0,0

#INPUT
consultora=input("Ingrese el nombre de consultora:")
nro_de_pedidos=int(input("Ingrese nro de pedidos:"))
costo_de_venta=float(input("Ingrese el costo de venta:"))
nro_de_clientes=int(input("Ingrese el nro de:"))

#PROCESSING
ingreso_total=(nro_de_pedidos*costo_de_venta)

#OUTPUT
print("###########################")
print("#     INGRESO TOTAL       #")
print("###########################")
print("# Consultora: ",consultora,"   #")
print("# NroDePedidos : ",nro_de_pedidos,"          #")
print("# CostoDeVenta : ",costo_de_venta,"         #")
print("# NroDeClientes: ",nro_de_clientes,"           #")
print("###########################")
print("# Ingreso Total: ",ingreso_total,"     #")
print("###########################")


#CALCULAR EL INGRESO TOTAL DE VENTA DE LECHE FRESCA
#Ganadero
#Nro de litros de leche fresca
#Costo x litro de leche fresca
#Numero de dias de entrega de leche fresca

#Declaracion de variables
ganadero,nro_de_litros,costo_x_litro,nro_de_dias,monto="",0.0,0.0,0,0.0

#Input
ganadero=input("Ingrese nombre de ganadero:")
nro_de_litros=float(input("Ingrese nro de litros:"))
costo_x_litro=float(input("Ingrese costo x litro:"))
nro_de_dias=int(input("Ingrese nro de dias:"))

#Processing
monto=(nro_de_litros*costo_x_litro)*nro_de_dias

#Output
print("###########################")
print("#     INGRESO TOTAL       #")
print("###########################")
print("# Ganadero: ",ganadero,"   #")
print("# Nro de Litros   : ",nro_de_litros,"          #")
print("# Costo x Litro : ",costo_x_litro,"         #")
print("# Nro de Dias: ",nro_de_dias,"          #")
print("###########################")
print("# Monto: ",monto,"     #")
print("###########################")



#Calcular el promedio de alumno
#nombre de alumno
#codigo
#nota1
#nota2
#nota3

#Declaracion De Variables
nombre_de_alumno,codigo,nota1,nota2,nota3="","",0.0,0.0,0.0

#Input
nombre_alumno=input("Ingrese nombre del alumno:")
codigo=input("Ingrese codigo:")
nota1=float(input("Ingrese nota1:"))
nota2=float(input("Ingrese nota2:"))
nota3=float(input("Ingrese nota3:"))

#Processing
promedio=(nota1+nota2+nota3)/3

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
print("##########################")


#Calcular la edad promedio de alumnos de 5to año de secundaria
#Nombre de colegio
#Dieciseis Anios
#Diecisiete Anios
#Dieciocho Anios

#Declaracion De Variables
nombre_de_colegio,dieciseis_anios,diecisiete_anios,dieciocho_anios="",0,0,0


#Input
nombre_colegio=input("Ingrese nombre de colegio:")
dieciseis_anios=int(input("Ingrese dieciseis anios:"))
diecisiete_anios=int(input("Ingrese  diecisiete anios:"))
dieciocho_anios=int(input("Ingrese dieciocho anios"))


#Processing
promedio=(dieciseis_anios+diecisiete_anios+dieciocho_anios)/3

#Output
print("###################################")
print("# PROMEDIO DE EDAD EN LOS ALUMNOS #")
print("###################################")
print("# Nombre de colegio: ",nombre_colegio,"  #")
print("# Dieciseis Anios: ",diecisiete_anios,"  #")
print("# Diecisiete Anios: ",diecisiete_anios,"   #")
print("# Dieciocho Anios: ",dieciocho_anios,"   #")
print("###################################")
print("# Promedio: ",promedio,"    #")
print("###################################")


#Ingreso Anual En Venta De Ropa
#Nombre de Tienda
#Enero
#Febrero
#Marzo
#Abril
#Mayo
#Junio
#Julio
#Agosto
#Setiembre
#Octubre
#Noviembre
#Diciembre

#Declaracion De Vraiables
nombre_de_tienda,enero,febrero,marzo,abril,mayo,junio,julio,agosto,setiembre,octubre,noviembre,diciembre="",0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0

#Input
nombre_de_tienda=input("Ingrese nombre de tienda:")
enero=float(input("Ingrese enero:"))
febrero=float(input("Ingrese febrero:"))
marzo=float(input("Ingrese marzo:"))
abril=float(input("Ingrese abril:"))
mayo=float(input("Ingrese mayo:"))
junio=float(input("Ingrese junio:"))
julio=float(input("Ingrese julio:"))
agosto=float(input("Ingrese agosto:"))
setiembre=float(input("Ingrese setiembre:"))
octubre=float(input("Ingrese octubre:"))
noviembre=float(input("Ingrese noviembre:"))
diciembre=float(input("Ingrese diciembre:"))

#Processing
promedio=(enero+febrero+marzo+abril+mayo+junio+julio+agosto+setiembre+octubre+noviembre+diciembre)/12

#Output
print("##################")
print("# PROMEDIO ANUAL #")
print("##################")
print("# Mes Enero: ",enero,"  #")
print("# Mes Febrero: ",febrero,"  #")
print("# Mes Marzo: ",marzo,"   #")
print("# Mes Abril: ",abril,"  #")
print("# Mes Mayo: ",mayo,"  #")
print("# Mes Junio: ",junio,"   #")
print("# Mes Julio: ",julio,"  #")
print("# Mes Agosto: ",agosto,"  #")
print("# Mes Setiembre: ",setiembre,"   #")
print("# Mes Octubre: ",octubre,"  #")
print("# Mes Noviembre: ",noviembre,"  #")
print("# Mes Diciemnbre: ",diciembre,"   #")
print("####################")
print("# Promedio: ",promedio,"    #")
print("####################")

#Calcular Total de Bebidas y Cigarros
#Caja de cerveza
#Cigarros
#Paquete de agua

#Declaracion De Variables
caja_de_cervezas,cigarros,paquetes_de_agua=0,0,0

#Input
caja_de_cervezas=int(input("Ingrese cajas de cervezas:"))
cigarros=int(input("Ingrese cigarros:"))
paquetes_de_agua=int(input("Ingrese paquetes de agua:"))

#Processing
total=caja_de_cervezas+cigarros+paquetes_de_agua

#Output
print("###############################")
print("# TOTAL DE BEBIDAS Y CIGARROS #")
print("###############################")
print("# Caja de Cervezas: ",caja_de_cervezas,"  #")
print("# Cigarros: ",cigarros,"  #")
print("# Paquetes de Agua: ",paquetes_de_agua,"   #")
print("###############################")
print("# TOTAL #")
print("###############################")


#Calcular el promedio de visitas a lugares turisticos
#Departamento de Lambayeque
#Nro de visitas Museo Tumbas Reales
#Nro de visitas Bosque de Pomac
#Nro de visitas Museo Bruning

#Declaracion de Variables
nombre_de_departamento,nro_de_visitas_museo_tumbas_reales,nro_de_visitas_bosque_de_pomac,nro_de_visitas_museo_bruning="",0,0,0

#Input
nombre_de_departamento=input("Ingrese nombre de departamento:")
nro_de_visitas_museo_tumbas_reales=int(input("Ingrese nro de visitas museo tumbas reales:"))
nro_de_visitas_bosque_de_pomac=int(input("Ingrese nro de visitas bosque de pomac:"))
nro_de_visitas_museo_bruning=int(input("Ingrese nro de visitas museo bruning:"))

#Processing
promedio=(nro_de_visitas_museo_tumbas_reales+nro_de_visitas_bosque_de_pomac+nro_de_visitas_museo_bruning)/3

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
print("#########################################################")


#Calcular el promedio en 2005 - 2007 en gastos de un hogar
#Anio2005
#Anio2006
#Anio2007

#Declaracion de Variables
gastos_anio2005,gastos_anio2006,gastos_anio2007=0.0,0.0,0.0

#Input
gastos_anio2005=float(input("Ingrese gastos anio2005:"))
gastos_anio2006=float(input("Ingrese gastos anio2006:"))
gastos_anio2007=float(input("Ingrese gastos anio2007:"))

#Processing
promedio=(gastos_anio2005+gastos_anio2006+gastos_anio2007)/3

#Output
print("#################################")
print("# PROMEDIO DE GASTOS EN UN HOGAR#")
print("#################################")
print("# Gastos anio2005: ",gastos_anio2005,"  #")
print("# Gastos anio2006: ",gastos_anio2006,"  #")
print("# Gastos anio2007: ",gastos_anio2007,"  #")
print("#################################")
print("# Promedio: ",promedio,"    #")
print("#################################")


#Calcular el ingreso en venta de jugos
#Cantidad jugo surtido
#Cantidad jugo especial
#Cantidad jugo naranja
#Cantidad ugo platano
#Costo por vaso de jugo
#Mostrar monto total

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
print("#########################################################")
