from calcularAsistencia import calcular_asistencia #Importamos la funcion "calcular_asistencia()" para ocuparlo abajo

def mostrar_asistencia(alumnos): #creamos una funcion con un parametro alumno sin argumentos hasta el momento
    print("Alumnos con asistencia menor al 70%:")
    alguno_encontrado = False #Creamos una variable de tipo False para crear un loop
    for alumno in alumnos: #iteramos alumnon en el parametro alumnos (sin argumentos por ahora), para recorrer los datos dentro de este
        asistencia = calcular_asistencia(alumno)#Creamos una variable llamada "asistencia" para guardar la funcion "calcular_asistencia()" con un parametro alumno (sin argumentos por ahora).
        if asistencia < 70: #Verificamos si "asistencia" es menor a 70 para ejecutar el siguiente codigo
            print(f"{alumno['nombre']} {alumno['apellidos']} - Asistencia: {asistencia:.2f} %") #Si la condicion es verdadera, mostrara en pantalla los datos del parametro que seran (nombre, apellidos) y se mostrara el valor de asistencia
            alguno_encontrado = True #El valor al ser encontrado se cambia la variable a True para que deje de ejecutarse el codigo
    
    if not alguno_encontrado: #Si la variable "alguno_encontrado" sigue siendo False se ejecutara el siguiente codigo
        print("No hay alumnos con asistencia menor al 70%.") #Se mostrara en pantalla el texto