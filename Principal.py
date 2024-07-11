import Funciones as fn

diccionario_trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]

while True:
    try: 
        print("------------------------------")
        print("--------MENU PRINCIPAL--------")
        print("------------------------------")
        print("1. Asignar sueldos aleatorios ")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas ")
        print("4. Reporte de sueldos ")
        print("5. Salir")
        opc=int(input("Ingrese opción: "))
        if opc == 1:
            fn.asignar(diccionario_trabajadores,sueldos)
        elif opc == 2:
            fn.calsificar(sueldos)
        elif opc == 3:
            fn.estadisticas(sueldos)
        elif opc == 4:
            fn.reporte(sueldos)
        elif opc == 5:
            print("Programa creado por Bruno Canales, Rut 20.481.554-2")
            print("Saliendo...")
            break
        elif opc== 0:
            print("¿¿Porqué marcaste 0??")
        elif opc== 6:
            print("Es enserio...?? jajaja")
    except:
        print("Ingrese un dato válido")