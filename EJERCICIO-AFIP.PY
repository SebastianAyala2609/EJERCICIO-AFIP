nombre = str(input("Introduce tu nombre completo: "))
categoria_actual = input("introduce tu categoria actual de monotributo. EJ: ‘A’: ") 
actividad_principal = input("introduce actividad principal de monotributo. EJ:‘SERVICIOS’/‘VENTAS’: ")
monotributo_unificado = input("¿estas adherido al monotributo unificado? Responda SI/NO según corresponda: ")
cuota_actual = float(input("introduce el importe de tu cuota actual del monotributo: ")) 
facturacion_anual = float(input("introduce el total anual facturado: "))
print("A continuación introduce el monto total facturado en los meses 1, 4, 7 y 10: ")
facturacion_estimada_mes1 = float(input("Total facturado en el mes 1: "))
facturacion_estimada_mes4 = float(input("Total facturado en el mes 4: "))
facturacion_estimada_mes7 = float(input("Total facturado en el mes 7: "))
facturacion_estimada_mes10 = float(input("Total facturado en el mes 10: "))
facturacion_anual_estimada = facturacion_estimada_mes1 * 3 + facturacion_estimada_mes4 * 3 + facturacion_estimada_mes7 * 3 + facturacion_estimada_mes10 * 3

#cuando existen 3 elem: el 1° es la cuota mensual, el 2° es el monto max. de fact. de la categ.
#Y el 3° es el importe fijo de ARBA/MONOT. UNIFIC. 
#cuando existen 4 elem: el 1° es la cuota mensual de "SERVIC", 
# el 2° la cuota mensual de "Ventas", el 3° el monto max. de fact. de la categ. 
# y el 4 es el importe fijo de ARBA/MONOT. UNIFIC. 

cat_a = ("Tu nueva categoria es: CATEGORIA A", 3334.24, 466201.59, 289)
cat_b = ("Tu nueva categoria es: CATEGORIA B", 3728.29, 693002.36,556)
cat_c = ("Tu nueva categoria es: CATEGORIA C", 4262.11, 4190.06, 970203.30,876)
cat_d = ("Tu nueva categoria es: CATEGORIA D", 5025.96, 4907.34, 1335604.55,1477)
cat_e = ("Tu nueva categoria es: CATEGORIA E", 6601.71, 5936.55, 1764006.01,2415)
cat_f = ("Tu nueva categoria es: CATEGORIA F", 7902.06, 6825.92, 2205007.51,3229)
cat_g = ("Tu nueva categoria es: CATEGORIA G", 9216.76, 7772.01, 2646009.01,4119)
cat_h = ("Tu nueva categoria es: CATEGORIA H", 16114.67, 13445.60, 3276011.15,8649)
cat_i = ("Tu nueva categoria es: CATEGORIA I", 19328.05, 3666612.48,10744)
cat_j = ("Tu nueva categoria es: CATEGORIA J", 22197.62, 4202114.31,12844)
cat_k = ("Tu nueva categoria es: CATEGORIA K", 25090.13, 4662015.87,14828)
               
print("LOS DATOS INGRESADOS SON:")
print(f"Nombre completo: {nombre}")
print(f"Categoria actual monotributo: {categoria_actual}, {actividad_principal} ")
print(f"Cuota actual monotributo: ${cuota_actual} ")
print(f"Facturación anual ${facturacion_anual}")
print(f"Total estimado de facturación anual ${facturacion_anual_estimada}")
print(f"Facturación mes 1: ${facturacion_estimada_mes1} ")
print(f"Facturación mes 4: ${facturacion_estimada_mes4} ")
print(f"Facturación mes 7: ${facturacion_estimada_mes7} ")
print(f"Facturación mes 10: ${facturacion_estimada_mes10} ")

#CATEGORIA A 
if facturacion_anual <= 466201.59: 
    print(f"{cat_a[0]}: {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_a[1]}"),
    print(f"Facturación maxima anual: ${cat_a[2]} "),
    print(f"Facturación promedio mensual: ${round(cat_a[2]/12,2)} "),

#CATEGORIA B 
if facturacion_anual > 466201.59 and facturacion_anual <= 693002.36: 
    print(f" {cat_b[0]}: {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_b[1]}"),
    print(f"Facturación maxima anual: ${cat_b[2]} "),
    print(f"Facturación promedio mensual: ${round(cat_b[2]/12,2)} "),

#CATEGORIA C 
if facturacion_anual > 693002.36 and facturacion_anual <= 970203.30 and actividad_principal == "SERVICIOS":
    print(f"{cat_c[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_c[1]} "),
    print(f"Facturación maxima anual: ${cat_c[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_c[3]/12,2)} "),


if facturacion_anual > 693002.36 and facturacion_anual <= 970203.30 and actividad_principal == "VENTAS":
    print(f"{cat_c[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_c[2]} "),
    print(f"Facturación maxima anual: ${cat_c[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_c[3]/12,2)} "),

#CATEGORIA D 
if facturacion_anual > 970203.30 and facturacion_anual <= 1335604.55 and actividad_principal == "SERVICIOS": 
    print(f"{cat_d[0]},{actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_d[1]} "),
    print(f"Facturación maxima anual: ${cat_d[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_d[3]/12,2)} "),

    
if facturacion_anual > 970203.30 and facturacion_anual <= 1335604.55 and actividad_principal == "VENTAS":
    print(f"{cat_d[0]},{actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_d[2]} "),
    print(f"Facturación maxima anual: ${cat_d[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_d[3]/12,2)} "),

    
#CATEGORIA E
if facturacion_anual > 1335604.55 and facturacion_anual <= 1764006.01 and actividad_principal == "SERVICIOS":
    print(f"{cat_e[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_e[1]} "),
    print(f"Facturación maxima anual: ${cat_e[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_e[3]/12,2)} "),


elif facturacion_anual > 1335604.55 and facturacion_anual <= 1764006.01 and actividad_principal == "VENTAS":
    print(f"{cat_e[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_e[2]} "),
    print(f"Facturación maxima anual: ${cat_e[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_e[3]/12,2)} "),

#CATEGORIA F
elif facturacion_anual > 1764006.01 and facturacion_anual <= 2205007.51 and actividad_principal == "SERVICIOS":
    print(f"{cat_f[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_f[1]} "),
    print(f"Facturación maxima anual: ${cat_f[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_f[3]/12,2)} "),
    

elif facturacion_anual > 1764006.01 and facturacion_anual <= 2205007.51 and actividad_principal == "VENTAS":
    print(f"{cat_f[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_f[2]} "),
    print(f"Facturación maxima anual: ${cat_f[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_f[3]/12,2)} "),

#CATEGORIA G
elif facturacion_anual > 2205007.51 and facturacion_anual <= 2646009.021 and actividad_principal == "SERVICIOS":
    print(f"{cat_g[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_g[1]} "),
    print(f"Facturación maxima anual: ${cat_g[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_g[3]/12,2)} "),

elif facturacion_anual > 2205007.51 and facturacion_anual <= 2646009.021 and actividad_principal == "VENTAS":
    print(f"{cat_g[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_g[2]} "),
    print(f"Facturación maxima anual: ${cat_g[3]} "),
    print(f"Facturación promedio mensual: ${round(cat_g[3]/12,2)} "),

#CATEGORIA H
elif facturacion_anual > 2646009.01 and facturacion_anual <= 3276011.15 and actividad_principal == "SERVICIOS":
    print(f"{cat_h[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_h[1]} "),
    print(f"Facturación maxima anual: ${cat_h[4]} "),
    print(f"Facturación promedio mensual: ${round(cat_h[3]/12,2)} "),
    
elif facturacion_anual > 2646009.01 and facturacion_anual <= 3276011.15 and actividad_principal == "VENTAS":
    print(f"{cat_h[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_h[2]} "),
    print(f"Facturación maxima anual: ${cat_h[4]} "),
    print(f"Facturación promedio mensual: ${round(cat_h[3]/12,2)} "),
    

#CATEGORIA I
elif facturacion_anual > 3276011.15 and facturacion_anual <= 3666612.48:
    print(f"{cat_i[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_i[1]} "),
    print(f"Facturación maxima anual: ${cat_i[2]} ")
    print(f"Facturación promedio mensual: ${round(cat_i[2]/12,2)} "),
    

#CATEGORIA J
elif facturacion_anual > 3666612.48 and facturacion_anual <= 4202015.87:
    print(f"{cat_j[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_j[1]} "),
    print(f"Facturación maxima anual: ${cat_j[2]} "),
    print(f"Facturación promedio mensual: ${round(cat_j[2]/12,2)} "),

#CATEGORIA K
elif facturacion_anual > 4202015.87 and facturacion_anual <= 4662015.87:
    print(f"{cat_k[0]}, {actividad_principal}"),
    print(f"Nueva cuota mensual: ${cat_k[1]} "),
    print(f"Facturación maxima anual: ${cat_k[2]} "),
    print(f"Facturación promedio mensual: ${round(cat_k[2]/12,2)} "),

#COMIENZAN LAS FACTURACIONES ESTIMADAS

#CATEGORIA A 
if facturacion_anual_estimada <= 466201.59:
    print(f"{cat_a[0][0:18]} estimada es:{cat_a[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_a[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_a[2]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_a[2]/12,2)} ")

#CATEGORIA B 
elif facturacion_anual_estimada > 466201.59 and facturacion_anual_estimada <= 693002.36:
    print(f"{cat_b[0][0:18]} estimada es:{cat_b[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_b[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_b[2]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_b[2]/12,2)} "),

#CATEGORIA C 
elif facturacion_anual_estimada > 693002.36 and facturacion_anual_estimada <= 970203.30 and actividad_principal == "SERVICIOS":
    print(f"{cat_c[0][0:18]} estimada es:{cat_c[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_c[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_c[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_c[3]/12,2)} "),

elif facturacion_anual_estimada > 693002.36 and facturacion_anual_estimada <= 970203.30 and actividad_principal == "VENTAS":
    print(f"{cat_c[0][0:18]} estimada es:{cat_c[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_c[2]} "),
    print(f"Facturación maxima anual estimada: ${cat_c[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_c[3]/12,2)} "),


#CATEGORIA D 
elif facturacion_anual_estimada > 970203.30 and facturacion_anual_estimada <= 1335604.55 and actividad_principal == "SERVICIOS":
    print(f"{cat_d[0][0:18]} estimada es:{cat_d[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_d[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_d[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_d[3]/12,2)} "),
    
    
elif facturacion_anual_estimada > 970203.30 and facturacion_anual_estimada <= 1335604.55 and actividad_principal == "VENTAS":
    print(f"{cat_d[0][0:18]} estimada es:{cat_d[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_d[2]} "),
    print(f"Facturación maxima anual estimada: ${cat_d[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_d[3]/12,2)} "),
    
#CATEGORIA E
elif facturacion_anual_estimada > 1335604.55 and facturacion_anual_estimada <= 1764006.01 and actividad_principal == "SERVICIOS":
    print(f"{cat_e[0][0:18]} estimada es:{cat_e[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_e[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_e[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_e[3]/12,2)} "),


elif facturacion_anual_estimada > 1335604.55 and facturacion_anual_estimada <= 1764006.01 and actividad_principal == "VENTAS":
    print(f"{cat_e[0][0:18]} estimada es:{cat_e[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_e[2]} "),
    print(f"Facturación maxima anual estimada: ${cat_e[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_e[3]/12,2)} "),

#CATEGORIA F
elif facturacion_anual_estimada > 1764006.01 and facturacion_anual_estimada <= 2205007.51 and actividad_principal == "SERVICIOS":
    print(f"{cat_f[0][0:18]} estimada es:{cat_f[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_f[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_f[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_f[3]/12,2)} "),
    

elif facturacion_anual_estimada > 1764006.01 and facturacion_anual_estimada <= 2205007.51 and actividad_principal == "VENTAS":
    print(f"{cat_f[0][0:18]} estimada es:{cat_f[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_f[2]} "),
    print(f"Facturación maxima anual estimada: ${cat_f[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_f[3]/12,2)} "),

#CATEGORIA G
elif facturacion_anual_estimada > 2205007.51 and facturacion_anual_estimada <= 2646009.021 and actividad_principal == "SERVICIOS":
    print(f"{cat_g[0][0:18]} estimada es:{cat_g[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_g[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_g[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_g[3]/12,2)} "),

elif facturacion_anual_estimada > 2205007.51 and facturacion_anual_estimada <= 2646009.021 and actividad_principal == "VENTAS":
    print(f"{cat_g[0][0:18]} estimada es:{cat_g[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_g[2]} "),
    print(f"Facturación maxima anual estimada: ${cat_g[3]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_g[3]/12,2)} "),

#CATEGORIA H
elif facturacion_anual_estimada > 2646009.01 and facturacion_anual_estimada <= 3276011.15 and actividad_principal == "SERVICIOS":
    print(f"{cat_h[0][0:18]} estimada es:{cat_h[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_h[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_h[4]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_h[3]/12,2)} "),
    
elif facturacion_anual_estimada > 2646009.01 and facturacion_anual_estimada <= 3276011.15 and actividad_principal == "VENTAS":
    print(f"{cat_h[0][0:18]} estimada es:{cat_h[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_h[2]} "),
    print(f"Facturación maxima anual estimada: ${cat_h[4]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_h[3]/12,2)} "),
    

#CATEGORIA I
elif facturacion_anual_estimada > 3276011.15 and facturacion_anual_estimada <= 3666612.48:
    print(f"{cat_i[0][0:18]} estimada es:{cat_i[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_i[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_i[2]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_i[2]/12,2)} "),
    

#CATEGORIA J
elif facturacion_anual_estimada > 3666612.48 and facturacion_anual_estimada <= 4202015.87:
    print(f"{cat_j[0][0:18]} estimada es:{cat_j[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_j[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_j[2]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_j[2]/12,2)} "),

#CATEGORIA K
elif facturacion_anual_estimada > 4202015.87 and facturacion_anual_estimada <= 4662015.87:
    print(f"{cat_k[0][0:18]} estimada es:{cat_k[0][22:34]}, {actividad_principal}"),
    print(f"Nueva cuota mensual estimada: ${cat_k[1]} "),
    print(f"Facturación maxima anual estimada: ${cat_k[2]} "),
    print(f"Facturación promedio mensual estimada: ${round(cat_k[2]/12,2)} "),


if facturacion_anual_estimada > facturacion_anual: 
    print("Tu facturación anual estimada es superior a tu facturación anual declarada") 
elif facturacion_anual_estimada < facturacion_anual: 
    print("Tu facturación anual declarada es superior a tu facturación anual estimada") 
else:
    print("Tu facturación anual declarada es igual a tu facturación anual estimada") 

if monotributo_unificado == "SI" or monotributo_unificado == "si" or monotributo_unificado == "Si":
     print("Estas adherido al monotributo unificado")
else: 
     print("No te encontras adherido al monotributo unificado")
    
