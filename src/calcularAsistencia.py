from datosAlumno import obtener_datos

datos_alumnos = obtener_datos() #Guardamos la funcion dentro de una variable

def calcular_asistencia(datos_alumnos): #Creamos una funcion que calculara la asisntecia del alumno
    total_clases = datos_alumnos['presente'] + datos_alumnos['ausente'] + datos_alumnos['justificado'] #Creamos una variable que guardara las sumas de 'presente' + 'ausente' + 'justificado'
    if total_clases > 0: #Verificamos si total_clases es mayor a 0 para ejecutar el siguiente codigo
        return (datos_alumnos['presente'] / total_clases) * 100 #retornara los valores de 'presente' dividido por el valor total_clases para luego multiplicar ese resultado en 100
    else:
        return 0.0 #de lo contrario se retornara un valor 0.0