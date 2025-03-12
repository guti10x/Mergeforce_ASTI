from pymata4 import pymata4
import time

# Inicializar la placa Ardls

board = pymata4.Pymata4()

# Definir pines
led_pin = 13
in1 = 6 # Entrada del puente H
in2 = 7 # Entrada del puente H

# Configurar pines
board.set_pin_mode_digital_output(led_pin)
board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)

try:
    while True:
        # Encender LED
        board.digital_write(led_pin, 1)
        
        # Avanzar motor por 1 segundo
        board.digital_write(in1, 1)
        board.digital_write(in2, 0)
        time.sleep(1)
        
        # Detener motor por 1 segundo
        board.digital_write(in1, 0)
        board.digital_write(in2, 0)
        time.sleep(1)
        
        # Marcha atrás por 1 segundo
        board.digital_write(in1, 0)
        board.digital_write(in2, 1)
        time.sleep(1)
        
        # Apagar LED
        board.digital_write(led_pin, 0)
        
        # Detener motor
        board.digital_write(in1, 0)
        board.digital_write(in2, 0)
        time.sleep(2)

except KeyboardInterrupt:
    print("Saliendo...")
    board.shutdown()
