from datosAlumno import obtener_datos #Importamos  la funcion "obtener_datos" para ocuparlo en el menu de abajo
from consultarAsistencia import consultar_asistencia #Importamos  la funcion "consultar_asistencia" para ocuparlo en el menu de abajo
from mostrarAsistencia import mostrar_asistencia #Importamos  la funcion "mostrar_asistencia" para ocuparlo en el menu de abajo
from asistenciaPorSeccion import contar_asistencia_bajo_70_por_seccion #Importamos  la funcion "contar_asistencia_bajo_70_por_seccion" para ocuparlo en el menu de abajo
from generarArchivo import generar_archivo_salida #Importamos  la funcion "generar_archivo_salida" para ocuparlo en el menu de abajo

def menu_principal(): #Creamos la funcion del menu llamada "menu_principal()"
    datos_alumnos = obtener_datos() #guardamos la funcion "obtener_datos" (datos del archivo csv), en una variable llamada "datos_alumnos" 
    
    print("Bienvenido!\n") 
    
    while True: #El codigo se ejecutara hasta que sea Falso
        print("Escoja su opción")
        print("1. Consultar asistencia de un alumno por RUT")
        print("2. Mostrar alumnos con asistencia menor al 70%")
        print("3. Mostrar número de alumnos con asistencia menor al 70% en una sección")
        print("4. Generar archivo de salida de alumnos por sección")
        print("5. Salir")
        
        opcion = int(input("Ingrese la opción: ")) #Variable de tipo entero/int que guardara el valor de la opcion para el menu 
        
        if opcion == 1:
            print("-"*20) #Mostramos en pantalla el "-" multiplicado por 20 (se mostrara 20 veces en total)
            consultar_asistencia(datos_alumnos) #El paramatro sera "datos_alumnos" que guarda dentro la funcion "obtener_datos" donde ese sera su argumento
            print("-"*20)
        elif opcion == 2:
            print("-"*20)
            mostrar_asistencia(datos_alumnos) #El paramatro sera "datos_alumnos" que guarda dentro la funcion "obtener_datos" donde ese sera su argumento
            print("-"*20)
        elif opcion == 3:
            print("-"*20)
            contar_asistencia_bajo_70_por_seccion(datos_alumnos) #El paramatro sera "datos_alumnos" que guarda dentro la funcion "obtener_datos" donde ese sera su argumento
            print("-"*20)
        elif opcion == 4:
            print("-"*20)
            generar_archivo_salida(datos_alumnos) #El paramatro sera "datos_alumnos" que guarda dentro la funcion "obtener_datos" donde ese sera su argumento
            print("Archivo de salida generado correctamente.")
            print("-"*20)
        elif opcion == 5:
            print("-"*20)
            print("¡Hasta luego!")
            break #Utilizamos un break para romper el ciclo del while
        else: #Si la opcion es distinto a los que se muestran en el menu se ejecutara el siguiente codigo y se repetira el while
            print("Opción inválida. Por favor, ingrese un número válido de opción.")
            print("-"*20)