# Función para ingresar las temperaturas
def ingresar_temperaturas():
    temperaturas = []
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        temp = float(input(f"Ingrese la temperatura de {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("=== Clima Semanal - Programación Tradicional ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"Promedio semanal: {promedio:.2f}°C")

# Ejecutar
if __name__ == "__main__":
    main()

