from pymata4 import pymata4
import time

# Inicializar la placa
board = pymata4.Pymata4()

# Pines
sensorIR_pin = 7  
led_pin = 13

# Configurar pines
board.set_pin_mode_digital_input(sensorIR_pin)
board.set_pin_mode_digital_output(led_pin)

while True:
    # Leemos valor sensor IR
    sensor_value = board.digital_read(sensorIR_pin)[0]  # Corregido: sensorIR_pin en lugar de sensor_pin
    
    # Si obtiene 0 -> negro
    if sensor_value == 1:
        # Encendemos LED
        board.digital_write(led_pin, 1)  
        print("Negroo → LED encendido")
    
    # Si obtiene 1-> blanco
    else: 
        board.digital_write(led_pin, 0)  # Corregido: board en lugar de ard
        print("Blanco → LED apagado")

    time.sleep(0.5)
