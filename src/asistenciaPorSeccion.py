from calcularAsistencia import calcular_asistencia #Importamos la funcion "calcular_asistencia" para utilizarlo más abajo

def contar_asistencia_bajo_70_por_seccion(alumnos): #Creamos una funcion con un parametro "alumnos" sin argumentos por ahora
    seccion_deseada = input("Ingrese la sección deseada (ej. A-01): ") #Creamos una variable tipo string llamada "seccion_deseada" que guardara los datos ingresados por el usuario
    contador = 0 #Creamos una variable "contador" en 0, para guardar la cantidad de alumnos que tengan bajo 70% segun la seccion 
    for alumno in alumnos: #Iteramos alumno en el parametro alumnos (sin argumentos por ahora) para recorrer los datos de esta
        if alumno['seccion'] == seccion_deseada: #Verificamos si la iteracion alumno con valor 'seccion' es igual a la variable con su dato, se ejecutara el sigueinte codigo
            asistencia = calcular_asistencia(alumno) #Si la condicion es verdadera, se crea una variable "asistencia" guardara la funcion calcular_asistencia() con un parametro sin argumentos (por ahora).
            if asistencia < 70: #Verificamos si la variable "asistencia" es menor a 70
                contador += 1 #Sumamos el contador por cada alumno con asistencia menor a 70
    print(f"Número de alumnos con asistencia menor al 70% en la sección {seccion_deseada}: {contador}") #Se muestra por pantalla la seccion y la cantidad de alumnos con asistencia menor a 70