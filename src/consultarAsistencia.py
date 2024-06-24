from calcularAsistencia import calcular_asistencia #Importamos la funcion "calcular_asistencia" para ocuparlo mas abajo

def consultar_asistencia(alumnos): #Creamos una funcion con parametro "alumnos" sin argumentos por ahora
    rut_alumno = int(input("Ingrese rut del alumno para ver asistencia: ")) #Creamos una variable tipo entero/int para guardar un valor ingresado por el usuario
    alumno_encontrado = None #Creamos una variable "alumno_encontrado" con un valor None por defecto (sin valor)
    for alumno in alumnos: #Iteramos alumno en el parametrom alumnos (sin argumentos por ahora), para recorrer los datos dentro del parametro
        if alumno["rut"] == rut_alumno: #Si la iteracion "alumno" con valor ["rut"] es igual == a la variable rut_alumno, se ejecutara el siguiente codigo
            alumno_encontrado = alumno #Si la condicion es verdadera, se guarda la iteracion alumno con sus datos en la variable alumno_encontrado
            break #Break para cerrar el ciclo
    
    if alumno_encontrado: #Si alumno_encontrado tiene un valor, se ejecutara el sigueinte codigo
        print(f"Asistencia del alumno {alumno_encontrado['nombre']} {alumno_encontrado['apellidos']}:") #Mostramos en pantalla la variable "alumno_econtrado" y su valor de diccionario nombre y apellidos
        print(f"Presente: {alumno_encontrado['presente']}") #Mostramos en pantalla la variable "alumno_econtrado" y su valor de diccionario presente
        print(f"Ausente: {alumno_encontrado['ausente']}") #Mostramos en pantalla la variable "alumno_econtrado" y su valor de diccionario ausente
        print(f"Justificado: {alumno_encontrado['justificado']}") #Mostramos en pantalla la variable "alumno_econtrado" y su valor de diccionario justificado
        asistencia = calcular_asistencia(alumno_encontrado) #Guardamos en una variable llamada "asistencia" la funcion "calcular_asistencia()" con parametro alumno_encontrado
        print(f"Asistencia actual: {asistencia:.2f}%") #Mostramos en pantalla la variable "asistencia". PD: la funcion .2f es para mostrar un numero decimal
    else: #Si alumno_encontrado no tiene datos guardados
        print("Alumno no encontrado") #Se mostrara en pantalla el siguiente texto