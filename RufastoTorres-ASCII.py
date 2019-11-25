#EJERCICIO1
# Calcular el ponderado final del 1er ciclo de un alumno
# Nombre de la universidad
# Donde su ponderado final se calcula de la siguiente manera
# Nota final del primer curso
# Se le suma la nota final del segundo curso
# Se le suma la nota final del tercer curso
# Mostrar la ficha de ponderado

# Declaracion variables
alumno,universidad,nota_final_del_primer_curso,nota_final_del_segundo_curso,nota_final_del_tercer_curso,ponderado="","",0.0,0.0,0.0,0.0

# INPUT
alumno=input("Ingrese el nombre del alumno:")
universidad=input("Ingrese el nombre de la universidad:")
nota_final_del_primer_curso=float(input("Ingrese nota final del primer curso:"))
nota_final_del_segundo_curso=float(input("Ingrese nota final del segundo curso:"))
nota_final_del_tercer_curso=float(input("Ingrese nota final del tercer curso:"))

# PROCESSING
ponderado=(nota_final_del_primer_curso+nota_final_del_segundo_curso+nota_final_del_tercer_curso)/3

# OUTPUT
print("###########################")
print("#     FICHA DE PONDERADO    #")
print("###########################")
print("# Alumno: ",alumno,"   #")
print("# Universidad: ",universidad,"      #")
print("# Nota final del primer curso  : ",nota_final_del_primer_curso,"          #")
print("# Nota final del segundo curso : ",nota_final_del_segundo_curso,"         #")
print("# Nota final del tercer curso: ",nota_final_del_tercer_curso,"           #")
print("###########################")
print("# Ponderado: ",ponderado,"     #")
print("###########################")


#EJERCICIO2
# Calcular el salario de un obrero
# Nombre de la empresa
# Donde su salario se calcula de la siguiente manera
# Nro Dias Trabajados x Costo por Dia
# Se le suma las horas extras, cada hora extra vale 15 soles
# Mostrar la boleta de pago

# Declaracion variables
obrero,empresa,nrodias,costo,horas_extra,monto="","",0,0.0,0,0.0

# INPUT
obrero=input("Ingrese el nombre del obrero:")
empresa=input("Ingrese el nombre de la empresa:")
nrodias=int(input("Ingrese nro de dias:"))
costo=float(input("Ingrese costo por dia:"))
horas_extra=int(input("Ingrese nro de horas extra:"))

# PROCESSING
monto=(nrodias*costo)+(horas_extra*15)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Obrero: ",obrero,"   #")
print("# Empresa: ",empresa,"      #")
print("# NroDias   : ",nrodias,"          #")
print("# CostoxDia : ",costo,"         #")
print("# HorasExtra: ",horas_extra,"           #")
print("###########################")
print("# Monto a Pagar: ",monto,"     #")
print("###########################")


#EJERCICIO3
# Calcular el ingreso anual de una familia
# Donde el ingreso anual se calcula de la siguiente manera
# Ingreso del padre x 12 meses
# Se le suma el ngreso de la madre x 12 meses
# Se le suma el Ingreso del hijo x 12 meses
# Mostrar ficha de ingreso total

# Declaracion variables
familia,ingreso_del_padre,ingreso_de_la_madre,ingreso_del_hijo,ingreso_anual="",0.0,0.0,0.0,0.0

# INPUT
familia=input("Ingrese el nombre de la familia:")
ingreso_del_padre=float(input("Ingrese el ingreso del padre:"))
ingreso_de_la_madre=float(input("Ingrese el ingreso de la madre:"))
ingreso_del_hijo=float(input("Ingrese el ingreso del hijo:"))

# PROCESSING
ingreso_anual=(ingreso_del_padre*12)+(ingreso_de_la_madre*12)+(ingreso_del_hijo*12)

# OUTPUT
print("###########################")
print("#     FICHA DE INGRESO TOTAL     #")
print("###########################")
print("# Familia: ",familia,"   #")
print("# Ingreso del padre: ",ingreso_del_padre,"      #")
print("# Ingreso de la madre  : ",ingreso_de_la_madre,"          #")
print("# Ingreso del hijo : ",ingreso_del_hijo,"         #")
print("###########################")
print("# Ingreso anual: ",ingreso_anual,"     #")
print("###########################")

#EJERCICIO4
# Calcular el IMC con calificacion sobrepeso de un paciente
# Edad del paciente
# Donde su IMC con calificacion sobrepeso se calcula de la siguiente manera
# Peso del paciente
# Sobre la talla x 2
# Mostrar ficha de IMC de sobrepeso

# Declaracion variables
paciente,edad,peso,talla,total_de_imc="",0,0.0,0.0,0.0

# INPUT
paciente=input ("Ingrese el paciente:")
edad=int(input("Ingrese la edad"))
peso=float(input("Ingrese peso"))
talla=float(input("Ingrese talla"))

# PROCESSING
total_de_imc= peso/(talla*2)

# OUTPUT
print("###########################")
print("#   FICHA DE IMC DE SOBREPESO #")
print("###########################")
print("# Paciente : ",paciente,"  #")
print("# Edad: ",edad,"    #")
print("# Peso: ",peso,"     #")
print("# Talla: ",talla,"        #")
print("###########################")
print("# Total del imc : ",total_de_imc,"  #")
print("######################################")



#EJERCICIO5
# Calcular el IMC con calificacion delgadez severa de un paciente
# Edad del paciente
# Donde su IMC con calificacion delgadez severa se calcula de la siguiente manera
# Peso del paciente
# Sobre la talla x 2
# Mostrar ficha de IMC de delgadez severa

# Declaracion variables
paciente,edad,peso,talla,total_de_imc="",0,0.0,0.0,0.0

# INPUT
paciente=input ("Ingrese el paciente:")
edad=int(input("Ingrese la edad"))
peso=float(input("Ingrese peso"))
talla=float(input("Ingrese talla"))

# PROCESSING
total_de_imc= peso/(talla*talla)

# OUTPUT
print("###########################")
print("#   FICHA DE IMC DE DELGADEZ SEVERA #")
print("###########################")
print("# Paciente : ",paciente,"  #")
print("# Edad: ",edad,"    #")
print("# Peso: ",peso,"     #")
print("# Talla: ",talla,"        #")
print("###########################")
print("# Total del imc : ",total_de_imc,"  #")
print("######################################")


#EJERCICIO6
# Calcular el promedio final de un alumno del tercio superior
# Nombre de la universidad
# Nro de ciclo
# Donde su promedio final se calcula de la siguiente manera
# Nota curso 1 Se le suma la nota curso 2 Mas nota curso 3
# Se divide entre 3 cursos
# Mostrar ficha de promedio final

# Declaracion variables
estudiante,universidad,ciclo,nota_curso1,nota_curso2,nota_curso3,promedio_final="","",0,0.0,0.0,0.0,0.0

# INPUT
estudiante=input("Ingrese el estudiante:")
universidad=input("Ingrese la universidad:")
ciclo=int(input("Ingrese ciclo:"))
nota_curso1=float(input("Ingrese nota_curso1:"))
nota_curso2=float(input("Ingrese nota_curso2:"))
nota_curso3=float(input("Ingrese nota_curso3:"))

# PROCESSING
promedio_final= (nota_curso1+nota_curso2+nota_curso3)/3

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


#EJERCICIO7
# Calcular el total a pagar en campana 14 de poductos avon de una consultora
# Donde el total a pagar se calcula de la siguiente manera
# Cantidad producto1 x costo uni producto1
# Se le suma la cantidad producto2 x costo uni producto2
# Mostrar la boleta de pago

# Declaracion variables
consultora,empresa,producto1,cantidad_prod1,costo_uni_prod1,producto2,cantidad_prod2,costo_uni_prod2,total_a_pagar="","","",0,0.0,"",0,0.0,0.0

# INPUT
consultora=input ("Ingrese el consultora:")
empresa=input ("Ingrese la empresa:")
producto1=input("Ingrese producto1")
cantidad_prod1=int(input("Ingrese cantidad_prod1"))
costo_uni_prod1=float(input("Ingrese costo_uni_prod1"))
producto2=input("Ingrese producto2")
cantidad_prod2=int(input("Ingrese cantidad_prod2"))
costo_uni_prod2=float(input("Ingrese costo_uni_prod2"))

# PROCESSING
total_a_pagar=(cantidad_prod1*costo_uni_prod1)+(cantidad_prod2*costo_uni_prod2)


# OUTPUT
print("###########################")
print("#   BOLETA DE PAGO  #")
print("###########################")
print("# Consultora : ",consultora,"  #")
print("# Empresa: ",empresa,"     #")
print("# Producto1: ",producto1,"        #")
print("# Cantidad producto1: ",cantidad_prod1,"        #")
print("# Costo unitario producto1: ",costo_uni_prod1,"        #")
print("# Producto2: ",producto2,"        #")
print("# Cantidad producto2: ",cantidad_prod2,"        #")
print("# Costo unitario producto2: ",costo_uni_prod2,"        #")
print("###########################")
print("# Total a pagar: ",total_a_pagar,"  #")
print("######################################")


#EJERCICIO8
# Mostrar la boleta de pago
# Calcular el total que se gasta en una construccion de un baño
# Donde el total se calcula de la siguiente manera
# Costo_prod1 x la cantidad_uni_prod1
# Se le suma el costo_prod2 x la cantidad_uni_prod2 mas el costo_prod3 x la cantidad_uni_prod3
# Se le suma la mano de obra

# Declaracion variables
obra,prod1,costo_prod1,cantidad_uni_prod1,prod2,costo_prod2,cantidad_uni_prod2,prod3,costo_prod3,cantidad_uni_prod3,mano_de_obra,monto_total="","",0.0,0,"",0,0.0,"",0.0,0,0.0,0.0

# INPUT
obra=input("Ingrese el nombre de la obra:")
prod1=input("Ingrese prod1:")
costo_prod1=float(input("Ingrese costo prod1:"))
cantidad_uni_prod1=int(input("Ingrese cantidad uni prod1:"))
prod2=input("Ingrese prod2:")
costo_prod2=float(input("Ingrese costo prod2:"))
cantidad_uni_prod2=int(input("Ingrese cantidad uni prod2:"))
prod3=input("Ingrese prod3:")
costo_prod3=float(input("Ingrese costo prod3:"))
cantidad_uni_prod3=int(input("Ingrese cantidad uni prod3:"))
mano_de_obra=float(input("Ingrese la mano de obra"))

# PROCESSING
monto_total=((costo_prod1*cantidad_uni_prod1)+(costo_prod2*cantidad_uni_prod2)+(costo_prod3*cantidad_uni_prod3)+mano_de_obra)

print("###########################")
print("#   BOLETA DE PAGO  #")
print("###########################")
print("# Prod1 : ",prod1,"          #")
print("# Costo prod1 : ",costo_prod1,"         #")
print("# Cantidad uni prod1: ",cantidad_uni_prod1,"       #")
print("# Prod2 : ",prod2,"          #")
print("# Costo prod2 : ",costo_prod2,"         #")
print("# Cantidad uni prod2: ",cantidad_uni_prod2,"           #")
print("# Prod3 : ",prod3,"          #")
print("# Costo prod3 : ",costo_prod3,"         #")
print("# Cantidad uni prod3: ",cantidad_uni_prod3,"           #")
print("# Mano de obra : ",mano_de_obra,"      #")
print("###########################")
print("# Monto total: ",monto_total,"  #")
print("######################################")

#EJERCICIO9
# Calcular el monto total de compra de celulares marca iphone de un prevendedor
# Donde el monto total se calcula de la siguiente manera
# Cantidad de celulares x costo uni
# Mostrar la boleta de pago

# Declaracion variables
prevendedor,marca,empresa,cantidad_de_celulares,costo_uni,monto_total="","","",0,0.0,0.0

# INPUT
prevendedor=input("Ingrese el prevendedor:")
marca=input("Ingrese la marca:")
empresa=input("Ingrese la empresa:")
cantidad_de_celulares=int(input("Ingrese cantidad de celulares:"))
costo_uni=float(input("Ingrese costo uni:"))

# PROCESSING
monto_total=(cantidad_de_celulares*costo_uni)

print("###########################")
print("#   BOLETA DE PAGO  #")
print("###########################")
print("# Prevendedor : ",prevendedor,"          #")
print("# Marca : ",marca,"         #")
print("# Empresa: ",empresa,"       #")
print("# Cantidad de celulares : ",cantidad_de_celulares,"          #")
print("# Costo uni: ",costo_uni,"         #")
print("###########################")
print("# Monto total: ",monto_total,"  #")
print("######################################")


#EJERCICIO10
# Calcular el total a pagar en curacion y extraccion de dientes de un paciente
# Donde el total a pagar se calcula de la siguiente manera
# Cantidad de dientes para curar x costo unitario
# Se le suma la cantidad de dientes para extraer x costo unitario
# Mostrar la boleta de pago

# Declaracion variables
paciente,clinica_odontologica,cantidad_de_dientes_para_curar,costo_unitario,cantidad_de_dientes_para_extraer,costo_unitario,total_a_pagar="","",0,0.0,0,0.0,0.0

# INPUT
paciente=input ("Ingrese el paciente:")
clinica_odontologica=input ("Ingrese la clinica odontologica:")
cantidad_de_dientes_para_curar=int(input("Ingrese la cantidad de dientes para curar"))
costo_unitario=float(input("Ingrese costo unitario"))
cantidad_de_dientes_para_extraer=int(input("Ingrese la cantidad de dientes para extraer"))
costo_unitario=float(input("Ingrese costo unitario"))

# PROCESSING
total_a_pagar=(cantidad_de_dientes_para_curar*costo_uni)+(cantidad_de_dientes_para_extraer*costo_unitario)


# OUTPUT
print("###########################")
print("#   BOLETA DE PAGO  #")
print("###########################")
print("# Paciente : ",paciente,"  #")
print("# Clinica odontologica: ",clinica_odontologica,"     #")
print("# Cantidad de dientes para curar: ",cantidad_de_dientes_para_curar,"        #")
print("# Costo unitario: ",costo_unitario,"        #")
print("# Cantidad de dientes para extraer: ",cantidad_de_dientes_para_extraer,"        #")
print("# Costo unitario: ",costo_unitario,"        #")
print("###########################")
print("# Total a pagar: ",total_a_pagar,"  #")
print("######################################")


