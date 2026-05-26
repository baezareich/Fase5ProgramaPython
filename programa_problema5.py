# --- Registro de Horas Trabajadas ---

nombres = []
total_horas_todos = []

print("=== SISTEMA DE REGISTRO DE HORAS ===")

# Ciclo que se repite 4 veces
for i in range(4):
    print("\n--- Registro del Trabajador N°", i + 1, "---")
    
    # Entrada de nomrbres:
    nombre_usuario = input("Ingrese el nombre del trabajador: ")
    nombres.append(nombre_usuario)
    
    # Pedimos las horas
    lunes = float(input("Horas lunes: "))
    martes = float(input("Horas martes: "))
    miercoles = float(input("Horas miercoles: "))
    jueves = float(input("Horas jueves: "))
    viernes = float(input("Horas viernes: "))
    
    # Suma:
    suma = lunes + martes + miercoles + jueves + viernes
    total_horas_todos.append(suma)

# --- Informe Final ---
print("\n" + "="*30)
print("     INFORME SEMANAL")
print("="*30)

for i in range(4):
    print("Trabajador:", nombres[i])
    print("Total horas:", total_horas_todos[i])
    
    if total_horas_todos[i] > 40:
        print("Clasificación: Sobretiempo")
    else:
        print("Clasificación: Horario Estándar")
    print("-" * 20)
