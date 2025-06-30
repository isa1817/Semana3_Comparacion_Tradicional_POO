class ClimaDia:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

class ClimaSemana:
    def __init__(self):
        self.dias = []

    def ingresar_datos(self):
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
            temp = float(input(f"Ingrese la temperatura de {dia}: "))
            self.dias.append(ClimaDia(dia, temp))

    def promedio_semanal(self):
        total = sum(d.temperatura for d in self.dias)
        return total / len(self.dias)

if __name__ == "__main__":
    print("=== Clima Semanal - POO ===")
    semana = ClimaSemana()
    semana.ingresar_datos()
    promedio = semana.promedio_semanal()
    print(f"Promedio semanal: {promedio:.2f}°C")
