import csv

def obtener_datos(): #Creamos una funcion, donde se obtienen los datos del archivo csv (excel) para agregarlos en una lista de forma diccionarios
    lista = []
    with open(r"C:\Users\oscar\Estudios\fundamentos\Eva3\asistencia_alumnos.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";") #Guardamos los datos del csv en una variable lector_csv
        pos = 0 #Creamos una variable con pos en 0 para que salte la primera linea de la fila que contiene los datos que no nos interesan 
        for linea in lector_csv: #Iteramos con "linea" dentro de la variable lector_csv
            if pos != 0: #Si pos es distinto a 0 se ejecuta el siguiente codigo
                seccion = linea[0] #creamos una variable que guardara los datos de la columna 0 (sigla_seccion)
                rut = int(linea[1]) #creamos una variable tipo int que guardara los datos de la columna 1 (rut_alumno)
                apellidos = linea[2] + " " + linea[3] #creamos una variable que guardara los datos de la columna 2 y 3 (apellido_paterno y apellido_materno)
                nombre = linea[4] #creamos una variable que guardara los datos de la columna 4 (nombre_alumno)
                presente = float(linea[5]) #creamos una variable tipo float que guardara los datos de la columna 5 (presente)
                ausente = float(linea[6]) #creamos una variable que guardara los datos de la columna 6 (ausente)
                justificado = float(linea[7]) #creamos una variable que guardara los datos de la columna 7 (justificada)
                
                lista.append({ #Aplicamos la funcion "append()" a la variable lista, que agregara los datos de forma diccionario
                    "seccion": seccion, #llave "seccion -> valor variable seccion
                    "rut": rut, #llave "rut" -> valor variable rut
                    "nombre": nombre, #llave "nombre" -> valor variable nombre
                    "apellidos": apellidos, #llave "apellidos" -> valor variable apellidos
                    "presente": presente, #llave "presente" -> valor variable presente
                    "ausente": ausente, #llave "ausente" -> valor variable ausente
                    "justificado": justificado #llave "justificado" -> valor variable justificado
                })
            else:
                pos = 1 #la pos cambia a 1, lo cual se ejecutara el codigo de arriba al ser distinto a 0
    return lista #retornara los valores de la "lista"