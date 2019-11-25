#EJERCICIO1
# Detector de aprobar curso
alumno,curso,nota1,nota2,nota3,promedio="","",0.0,0.0,0.0,0.0

# INPUT
alumno=input ("Ingrese el alumno:")
curso=input ("Ingrese el curso:")
nota1=float(input("Ingrese nota1"))
nota2=float(input("Ingrese nota2"))
nota3=float(input("Ingrese nota3"))

# PROCESSING
promedio=(nota1+nota2+nota3)/3

# DETECTOR
# Sera alumno aprobado cuando el promedio > 10.5
alumno_aprobado=(promedio > 10.5)

# OUTPUT
print("###########################")
print("#   FICHA DE NOTA FINAL   #")
print("###########################")
print("# Alumno : ",alumno,"  #")
print("# Curso: ",curso,"     #")
print("# Nota1: ",nota1,"        #")
print("# Nota2: ",nota2,"        #")
print("# Nota3: ",nota3,"        #")
print("###########################")
print("# Promedio: ",promedio,"  #")
print("# Alumno Aprobado: ",alumno_aprobado,  "#")
print("######################################")

#EJERCICIO2
#Detector de IMC con calificacion sobrepeso
paciente,peso,talla,total="",0.0,0.0,0.0

# INPUT
paciente=input ("Ingrese el paciente:")
peso=float(input("Ingrese peso"))
talla=float(input("Ingrese talla"))

# PROCESSING
total= peso/(talla*talla)

# DETECTOR
# Sera paciente con calificacion sobrepeso cuando el total es de 24.99
paciente_con_calificacion_sobrepeso=(total > 24.99 )

# OUTPUT
print("###########################")
print("#   FICHA DE IMC  #")
print("###########################")
print("# Paciente : ",paciente,"  #")
print("# Peso: ",peso,"     #")
print("# Talla: ",talla,"        #")
print("###########################")
print("# Total: ",total,"  #")
print("# Paciente_con_calificacion_sobrepeso: ",paciente_con_calificacion_sobrepeso,  "#")
print("######################################")

#EJERCICIO3
#Detector de IMC con calificacion delgadez severa
paciente,peso,talla,total="",0.0,0.0,0.0

# INPUT
paciente=input ("Ingrese el paciente:")
peso=float(input("Ingrese peso"))
talla=float(input("Ingrese talla"))

# PROCESSING
total= peso/(talla*talla)

# DETECTOR
# Sera paciente con calificacion delgadez severa cuando el total es de < 16.00
paciente_con_calificacion_delgadez_severa=(total < 16.00 )

# OUTPUT
print("###########################")
print("#   FICHA DE IMC  #")
print("###########################")
print("# Paciente : ",paciente,"  #")
print("# Peso: ",peso,"     #")
print("# Talla: ",talla,"        #")
print("###########################")
print("# Total: ",total,"  #")
print("# Paciente_con_calificacion_delgadez_severa: ",paciente_con_calificacion_delgadez_severa,  "#")
print("######################################")

#EJERCICIO4
# Detector de merecidas vacaciones
trabajador,empresa,anios,meses,dias,total="","",0,0,0,0.0

# INPUT
trabajador=input("Ingrese el trabajador:")
empresa=input("Ingrese la empresa:")
anios=int(input("Ingrese anios:"))
meses=int(input("Ingrese meses:"))
dias=int(input("Ingrese dias:"))

# PROCESSING
total= ((anios*365)+(meses*30)+dias)

# DETECTOR
# Tendra merecidas vacaciones cuando el total es  > 1000 dias
merecidas_vacaciones=(total > 1000)

# OUTPUT
print("###########################")
print("#     HOJA DE VACACIONES     #")
print("###########################")
print("# Trabajador : ",trabajador,"  #")
print("# Empresa: ",empresa,"        #")
print("# Anios: ",anios,"           #")
print("# Meses: ",meses,"   #")
print("# Dias: ",dias,"     #")
print("###########################")
print("# Total:  ",total,"      #")
print("# Merecidas vacaciones: ",merecidas_vacaciones,  "#")
print("###########################")


#EJERCICIO5
# Detector de tercio superior
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

# DETECTOR
# Ocupara tercio superior cuando el promedio final es > 17.5
tercio_superior=(promedio_final > 17.5)

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
print("# Tercico superior: ",tercio_superior,  "#")
print("###########################")


#EJERCICIO6
# Detector de pasar pedido
cliente,empresa,producto1,cantidad_prod1,costo_uni_prod1,producto2,cantidad_prod2,costo_uni_prod2,total="","","",0,0.0,"",0,0.0,0.0

# INPUT
cliente=input ("Ingrese el cliente:")
empresa=input ("Ingrese la empresa:")
producto1=input("Ingrese producto1")
cantidad_prod1=int(input("Ingrese cantidad_prod1"))
costo_uni_prod1=float(input("Ingrese costo_uni_prod1"))
producto2=input("Ingrese producto2")
cantidad_prod2=int(input("Ingrese cantidad_prod2"))
costo_uni_prod2=float(input("Ingrese costo_uni_prod2"))

# PROCESSING
total=(cantidad_prod1*costo_uni_prod1)+(cantidad_prod2*costo_uni_prod2)

# DETECTOR
# Si pasara pedido cuando el total > 120.00
pasara_pedido=(total > 120.00)

# OUTPUT
print("###########################")
print("#   FICHA DE PASAR PEDIDO  #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Empresa: ",empresa,"     #")
print("# Producto1: ",producto1,"        #")
print("# Cantidad producto1: ",cantidad_prod1,"        #")
print("# Costo unitario producto1: ",costo_uni_prod1,"        #")
print("# Producto2: ",producto2,"        #")
print("# Cantidad producto2: ",cantidad_prod2,"        #")
print("# Costo unitario producto2: ",costo_uni_prod2,"        #")
print("###########################")
print("# Total: ",total,"  #")
print("# Pasara pedido: ",pasara_pedido,  "#")
print("######################################")


#EJERCICIO7
# Detector de recibir liquidacion
obrero,empresa,anios_de_trabajo,meses_de_trabajo,dias_de_trabajo,tiempo_total="","",0,0,0,0.0

# INPUT
obrero=input ("Ingrese el obrero:")
empresa=input ("Ingrese la empresa:")
anios_de_trabajo=int (input ("Ingrese los años:"))
meses_de_trabajo=int (input("Ingrese los meses" ))
dias_de_trabajo=int (input("Ingrese los dias"))

# PROCESSING
tiempo_total=((anios_de_trabajo*360)+(meses_de_trabajo*30)+(dias_de_trabajo))

# DETECTOR
# Recibira liquidacion si el tiempo total > 3000 dias
recibira_liquidacion=(tiempo_total > 3000)

# OUTPUT
print("###########################")
print("#   HOJA DE LIQUIDACION   #")
print("###########################")
print("# Obrero : ",obrero,"  #")
print("# Empresa: ",empresa,"     #")
print("# Anios de trabajo: ",anios_de_trabajo,"        #")
print("# Meses de trabajo: ",meses_de_trabajo,"       #")
print("# Dias de trabajo: ",dias_de_trabajo,"        #")
print("###########################")
print("# Tiempo total:" ,tiempo_total,"        #")
print("# Recibira liquidacion: ",recibira_liquidacion,"  #")
print("######################################")


#EJERCICIO8
# Detector de comprador compulsivo
cliente,producto,cant,costo_uni,total="","",0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_uni=float(input("Ingrese costo uni:"))

# PROCESSING
total=cant*costo_uni

# DETECTOR
# Sera comprador compulsivo cuando el total > 150
comprador_compulsivo=(total > 150)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto: ",producto,"        #")
print("# Cantidad: ",cant,"           #")
print("# CostoUnitario: S/. ",costo_uni," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# Comprador Compulsivo: ",comprador_compulsivo,  "#")
print("###########################")

#EJERCICIO9
# Detector de avance de una persona
obrero,empresa,trabajo,nro_javas,total_de_ajies_por_min,horas_trabajadas,total="","","",0,0,0,0

# INPUT
obrero=input ("Ingrese el obrero:")
empresa=input ("Ingrese la empresa:")
trabajo=input ("Ingrese el trabajo:")
nro_javas=int (input ("Ingrese el nro de javas:"))
total_de_ajies_por_min=int (input("Ingrese el total de ajies por min" ))
horas_trabajadas=int (input("Ingrese las horas trabajadas"))

# PROCESSING
total=(total_de_ajies_por_min*horas_trabajadas)

# DETECTOR
# Sera personal de avance si su total es > 1000
personal_de_avance=(total > 1000)

# OUTPUT
print("###########################")
print("#   HOJA DE AVANCE DE PERSONAL  #")
print("###########################")
print("# Obrero : ",obrero,"  #")
print("# Empresa: ",empresa,"     #")
print("# Trabajo: ",trabajo,"        #")
print("# Nro javas: ",nro_javas,"       #")
print("# Total de ajies por min: ",total_de_ajies_por_min,"        #")
print("# Horas trabajadas:", horas_trabajadas,"     #")
print("###########################")
print("# Total:" ,total,"        #")
print("# Personal de avance: ",personal_de_avance,"  #")
print("######################################")


#EJERCICIO10
# Detector de aprobar sustentacion de tesis de un alumno
alumno,universidad,nota1,nota2,nota3,promedio_de_sustentacion="","",0.0,0.0,0.0,0.0

# INPUT
alumno=input ("Ingrese el alumno:")
universidad=input ("Ingrese la universidad:")
nota1=float(input("Ingrese nota1"))
nota2=float(input("Ingrese nota2"))
nota3=float(input("Ingrese nota3"))

# PROCESSING
promedio_de_sustentacion=(nota1+nota2+nota3)/3

# DETECTOR
# Sera alumno aprobado cuando el promedio de sustentacion > 15
alumno_aprobado=(promedio_de_sustentacion> 15)

# OUTPUT
print("###########################")
print("#   FICHA DE NOTA DE SUSTENTACION  #")
print("###########################")
print("# Alumno : ",alumno,"  #")
print("# Universidad: ",universidad,"     #")
print("# Nota1: ",nota1,"        #")
print("# Nota2: ",nota2,"        #")
print("# Nota3: ",nota3,"        #")
print("###########################")
print("# Promedio de sustentacion: ",promedio_de_sustentacion,"  #")
print("# Alumno Aprobado: ",alumno_aprobado,  "#")
print("######################################")
