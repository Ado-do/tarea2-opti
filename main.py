from docplex.mp.model import Model

# Crear modelo
modelo = Model(name="Pociones_EnteroMixto")

# Datos de las pociones
pociones = [
    "Elixir_vida",
    "Regeneracion",
    "Dano_instantaneo",
    "Respiracion_agua",
    "Explosion",
    "Veneno",
    "Fuerza",
    "Resistencia_fuego",
    "Proteccion",
    "Caida_lenta",
]

# Bonus XP por poción
bonus_xp = [15, 5, 10, 6, 10, 7, 5, 9, 8, 12]

# Tiempo de producción (minutos)
tiempo_produccion = [10, 5, 3, 2, 3.5, 2.5, 2, 3, 6, 4]

# Variables de cantidad de pociones
x = []
for i in range(10):
    if i == 0:  # Elixir_vida
        x.append(modelo.integer_var(lb=0, ub=10, name=f"x_{i}"))
    elif i == 2:  # Dano_instantaneo
        x.append(modelo.integer_var(lb=0, ub=25, name=f"x_{i}"))
    elif i == 9:  # Caida_lenta
        x.append(modelo.integer_var(lb=0, ub=50, name=f"x_{i}"))
    else:
        x.append(modelo.integer_var(lb=0, name=f"x_{i}"))

# Variables binarias
y = []
for i in range(10):
    y.append(modelo.binary_var(name=f"y_{i}"))

# Constante M
M = 100

# Función objetivo: Maximizar XP total
objetivo = sum(bonus_xp[i] * x[i] for i in range(10))
modelo.maximize(objetivo)


# RESTRICCIONES

# Fabricar exactamente 100 pociones
modelo.add_constraint(sum(x[i] for i in range(10)) == 100, "Total_pociones")

# Tiempo total disponible (300 minutos)
modelo.add_constraint(sum(tiempo_produccion[i] * x[i] for i in range(10)) <= 300, "Tiempo_total")

# Al menos 15 pociones de curación (pociones 0 y 1)
modelo.add_constraint(x[0] + x[1] >= 15, "Minimo_curativas")

# No más pociones de explosión que de protección
modelo.add_constraint(x[4] <= x[8], "Explosion_vs_Proteccion")

# Relación entre variables binarias y continuas
for i in range(10):
    modelo.add_constraint(x[i] <= M * y[i], f"Relacion_binaria_{i}")

# Excluyentes: Caída lenta y Respiración bajo agua no pueden coexistir
modelo.add_constraint(y[3] + y[9] <= 1, "Excluyentes_Respiracion_Caida")

# Secuencia: Para fabricar Daño instantáneo, debe fabricar al menos 7 de Veneno
modelo.add_constraint(x[5] >= 7 * y[2], "Secuencia_Veneno_Dano")

# Resolver el modelo
solucion = modelo.solve()

# Mostrar resultados
print("* SOLUCIÓN ÓPTIMA")

if solucion:
    print(f"XP total máximo: {solucion.objective_value:.0f}")

    print("\nCantidad de pociones a fabricar:")

    total_pociones = 0
    total_tiempo = 0

    for i in range(10):
        cantidad = solucion.get_value(x[i])
        if cantidad > 0:
            tiempo = cantidad * tiempo_produccion[i]
            xp = cantidad * bonus_xp[i]
            total_pociones += cantidad
            total_tiempo += tiempo

            print(f"{pociones[i]:<20}: {cantidad:>2} pociones | {tiempo:>5.1f} min | {xp:>3} XP")

    print(
        f"{'TOTAL':<20}: {total_pociones:>2} pociones | {total_tiempo:>5.1f} min | {solucion.objective_value:>3.0f} XP"
    )

    # Mostrar restricciones especiales
    print("\nVerificación de restricciones:")
    print(f"- Pociones de curación: {solucion.get_value(x[0]) + solucion.get_value(x[1])} ≥ 15")
    print(f"- Explosión ≤ Protección: {solucion.get_value(x[4])} ≤ {solucion.get_value(x[8])}")
    print(f"- Veneno para Daño instantáneo: {solucion.get_value(x[5])} ≥ {7 * solucion.get_value(y[2])}")

else:
    print("No se encontró solución óptima")

