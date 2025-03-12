from pymata4 import pymata4
import time

# Inicializar la placa Arduino
board = pymata4.Pymata4()

# Definir pines
led_pin = 13
in1 = 6  # Entrada del primer motor
in2 = 7  # Entrada del primer motor
in3 = 3  # Entrada del segundo motor
in4 = 4  # Entrada del segundo motor

# Configurar pines
board.set_pin_mode_digital_output(led_pin)
board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)
board.set_pin_mode_digital_output(in3)
board.set_pin_mode_digital_output(in4)

try:
    while True:
        # Encender LED
        board.digital_write(led_pin, 1)
        
        # Ir recto (Ambos motores hacia adelante)
        board.digital_write(in1, 1)
        board.digital_write(in2, 0)
        board.digital_write(in3, 1)
        board.digital_write(in4, 0)
        time.sleep(2)
        
        # Ir hacia atrás (Ambos motores hacia atrás)
        board.digital_write(in1, 0)
        board.digital_write(in2, 1)
        board.digital_write(in3, 0)
        board.digital_write(in4, 1)
        time.sleep(2)
        
        # Girar a la derecha (Motor 1 adelante, Motor 2 atrás)
        board.digital_write(in1, 1)
        board.digital_write(in2, 0)
        board.digital_write(in3, 0)
        board.digital_write(in4, 1)
        time.sleep(2)
        
        # Girar a la izquierda (Motor 1 atrás, Motor 2 adelante)
        board.digital_write(in1, 0)
        board.digital_write(in2, 1)
        board.digital_write(in3, 1)
        board.digital_write(in4, 0)
        time.sleep(2)
        
        # Apagar LED
        board.digital_write(led_pin, 0)
        
        # Detener motores
        board.digital_write(in1, 0)
        board.digital_write(in2, 0)
        board.digital_write(in3, 0)
        board.digital_write(in4, 0)
        time.sleep(2)

except KeyboardInterrupt:
    print("Saliendo...")
    board.shutdown()
