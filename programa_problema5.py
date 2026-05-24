# =====================================================================
# CURSO: Fundamentos de Programación (213022)
# FASE 5: Evaluación Final POA
# ESTUDIANTE: [Tu Nombre Completo]
# PROBLEMA SELECCIONADO: Problema 5 - Matriz de Horas Trabajadas
# =====================================================================

def clasificar_jornada(total_horas):
    """
    Módulo (función) para clasificar la jornada de un recurso 
    basándose en el umbral de 40 horas semanales.
    """
    UMBRAL_HORAS = 40
    if total_horas > UMBRAL_HORAS:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

def generar_informe_horas(matriz_recursos):
    """
    Módulo encargado de procesar la matriz de datos,
    calcular las sumas de horas por recurso e imprimir el reporte final.
    """
    print("\n=================================================================")
    print("        INFORME SEMANAL DE JORNADAS - RECURSOS DEL EQUIPO        ")
    print("=================================================================")
    print(f"{'Nombre del Recurso':<20} | {'Total Horas':<12} | {'Clasificación Jornada':<20}")
    print("-" * 65)
    
    for recurso in matriz_recursos:
        nombre = recurso[0]
        # Sumar los valores numéricos de las horas (Lunes a Viernes)
        horas_semanales = sum(recurso[1:])
        
        # Invocar la función de clasificación
        clasificacion = clasificar_jornada(horas_semanales)
        
        # Imprimir fila con formato alineado
        print(f"{nombre:<20} | {horas_semanales:<12.1f} | {clasificacion:<20}")
    print("=================================================================\n")

# --- Bloque Principal del Programa ---
if __name__ == "__main__":
    # Inicializamos la matriz vacía
    matriz_horas_equipo = []
    
    print("====================================================")
    print("   SISTEMA DE REGISTRO DE HORAS LABORALES (UNAD)    ")
    print("====================================================\n")
    
    # Ciclo para capturar los datos de los 4 recursos exigidos por la guía
    DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    for i in range(4):
        print(f"--- Registro del Recurso N° {i + 1} ---")
        nombre = input("Ingrese el nombre del trabajador: ")
        
        # Lista temporal para guardar los datos de este trabajador
        fila_trabajador = [nombre]
        
        # Captura de horas para cada día de la semana
        for dia in DIAS:
            while True:
                try:
                    horas = float(input(f"  Horas trabajadas el {dia}: "))
                    if horas >= 0:
                        fila_trabajador.append(horas)
                        break
                    else:
                        print("  [Error] Las horas no pueden ser negativas. Intente de nuevo.")
                except ValueError:
                    print("  [Error] Por favor ingrese un valor numérico válido.")
        
        # Agregar la fila del trabajador a la matriz principal
        matriz_horas_equipo.append(fila_trabajador)
        print() # Salto de línea estético
        
    # Ejecutar el módulo para procesar los datos ingresados y generar el informe
    generar_informe_horas(matriz_horas_equipo)