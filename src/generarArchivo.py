import csv
from calcularAsistencia import calcular_asistencia

def generar_archivo_salida(alumnos):
    sigla_seccion = input("Ingrese la sigla-sección para generar el archivo de salida (ej. A-01): ")
    nombre_archivo = f"asistencia_{sigla_seccion}.csv"
    
    with open(nombre_archivo, "w", newline="") as archivo_salida:
        escritor = csv.writer(archivo_salida, delimiter=";")
        escritor.writerow(["RUT", "Apellidos", "Nombre", "Asistencia Actual (%)"])
        
        for alumno in alumnos:
            if alumno['seccion'] == sigla_seccion:
                asistencia = calcular_asistencia(alumno)
                escritor.writerow([alumno['rut'], alumno['apellidos'], alumno['nombre'], f"{asistencia:.2f}"])