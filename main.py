from docplex.mp.model import Model
import time

# Modelo
modelo = Model(name="Pociones_EnteroMixto")

poc = {
    1: {"nombre": "Elixir de la vida", "xp": 15, "tiempo": 10, "max": 10},
    2: {"nombre": "Regeneración", "xp": 5, "tiempo": 5, "max": float('inf')},
    3: {"nombre": "Daño instantáneo", "xp": 10, "tiempo": 3, "max": 25},
    4: {"nombre": "Respiración bajo el agua", "xp": 6, "tiempo": 2, "max": float('inf')},
    5: {"nombre": "Explosión instantánea", "xp": 10, "tiempo": 3.5, "max": float('inf')},
    6: {"nombre": "Veneno", "xp": 7, "tiempo": 2.5, "max": float('inf')},
    7: {"nombre": "Aumento de fuerza", "xp": 5, "tiempo": 2, "max": float('inf')},
    8: {"nombre": "Resistencia al fuego", "xp": 9, "tiempo": 3, "max": float('inf')},
    9: {"nombre": "Protección contra proyectiles", "xp": 8, "tiempo": 6, "max": float('inf')},
    10: {"nombre": "Caída lenta", "xp": 12, "tiempo": 4, "max": 50}
}

# Variables de decisión
x = { modelo.integer_var_dict(poc.keys(), name="x")}

# Variables binarias
y = {
    3: modelo.binary_var(name="y3"),   # Daño Instantáneo
    4: modelo.binary_var(name="y4"),   # Respiración bajo el agua
    10: modelo.binary_var(name="y10")  # Caída Lenta
}

# Restricciones
# ej: lotes minimos, restricciones excluyentes, restricciones de frecuencia

# Función objetivo: Maximizar XP

# Resolver modelo

# Análisis de resultados

# (Opcional) comparar con modelo lineal
