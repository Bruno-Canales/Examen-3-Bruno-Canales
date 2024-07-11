import statistics
import random
import csv

def asignar(diccionario_trabajadores,sueldos):
    for i in diccionario_trabajadores:
        sueldo=random.randint(300000,2500000)
        sueldos.append({
            i:sueldo
        })
    print(sueldos)
    return

def calsificar(sueldos):
    if not sueldos:
        print("Primero debe inicializar sueldos")
        return
    else:
        menor_8=[]
        entre_8y2=[]
        mayor_2=[]
        sueldos_lista=[]
        for diccionario in sueldos:
            for trabajador, sueldo in diccionario.items():
                if sueldo<800000:
                    menor_8.append([trabajador,sueldo])
                if sueldo>800000 and sueldo<2000000:
                    entre_8y2.append([trabajador,sueldo])
                if sueldo>2000000:
                    mayor_2.append([trabajador,sueldo])
                sueldos_lista.append(sueldo)
        
        print("")
        print("Menores a 800.000")
        print(menor_8)
        print("")
        print("Total:",len(menor_8))

        print("")

        print("Mayores a 2.000.000")
        print(mayor_2)
        print("")
        print("Total:",len(mayor_2))
        
        print("")

        print("Entre 800.000 y 2.000.000")
        print(entre_8y2)
        print("")
        print("Total:",len(entre_8y2))

        print("")

        print("Total Sueldos:",sum(sueldos_lista))
    return

def estadisticas(sueldos):
    if not sueldos:
        print("Primero debe inicializar sueldos")
        return
    else:
        lista=[]
        for diccionario in sueldos:
            for trabajador, sueldo in diccionario.items():
                lista.append(sueldo)
        menor=min(lista)
        mayor=max(lista)
        promedio=sum(lista) / len(lista)
        media_geometrica=statistics.geometric_mean(lista)

        print("")
        print("Menor sueldo:", menor)
        print("Mayor sueldo:",mayor)
        print("Promedio sueldos:",promedio)
        print("Media geometrica:",media_geometrica)
        print("")
        return
    
def reporte(sueldos):
    if not sueldos:
        print("Primero debe inicializar sueldos")
        return
    else:
        with open("Reporte_sueldos.csv","w",newline="") as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(["Nombre","Sueldo","Descuento de Salud","Descuento de AFP","Liquido"])
            for diccionario in sueldos:
                for trabajador, sueldo in diccionario.items():
                    descuento_salud=sueldo*0.07
                    descuento_afp=sueldo*0.12
                    liquido=sueldo-descuento_afp-descuento_salud
                    escritor.writerow([trabajador,sueldo,descuento_salud,descuento_afp,liquido,""])
        print("Los sueldos se han imprimido satisfactoriamente")
        return