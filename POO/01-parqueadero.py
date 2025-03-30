class Vehiculo:
    def __init__(self, placa, marca, color):
        self.placa = placa
        self.color = marca
        self.color = color

    def pico_placa(self, ultimo_digito, dia_semana):
        dias_restringidos = {
            "Lunes": [1, 2],
            "Martes": [3, 4],
            "Miercoles": [5, 6],
            "Jueves": [7, 8],
            "Viernes": [9, 0]
        }
        return ultimo_digito in dias_restringidos[dia_semana]

    def cancelar_parqueadero(self, tiempo_parqueo, tarifa_por_hora):
        return tiempo_parqueo * tarifa_por_hora

if __name__ == "__main__":
    vehiculo = Vehiculo("ABC167", "Toyota", "Azul")

    dia = "Miercoles"
    ultimo_digito = int(vehiculo.placa[-1])

    if vehiculo.pico_placa(ultimo_digito, dia):
        print("El vehículo tiene restricción de pico y placa el", dia)
    else:
        print("El vehículo NO tiene restricción de pico y placa el", dia)

    tiempo_estadia = 8
    tarifa_por_hora = 1500 
    valor_parqueo = vehiculo.cancelar_parqueadero(tiempo_estadia, tarifa_por_hora)
    print("Valor del parqueo:", valor_parqueo)
