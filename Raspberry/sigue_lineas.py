from pymata4 import pymata4
import time

# Inicializar la placa Arduino
board = pymata4.Pymata4()

# Pines
led_pin = 13
in1 = 6  # IN1 - motor 1
in2 = 7  # IN2 - motor 1
in3 = 3  # IN3 - motor 2
in4 = 4  # IN4 - motor 2

# Configuraracción pines
board.set_pin_mode_digital_output(led_pin)
board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)
board.set_pin_mode_digital_output(in3)
board.set_pin_mode_digital_output(in4)

"""Ambos motores giren hacia adelante"""
def mover_adelante(tiempo=2):
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 1)
    board.digital_write(in4, 0)
    time.sleep(tiempo)
    detener_motores()

"""Ambos motores giren hacia atrás"""
def mover_atras(tiempo=2):
    board.digital_write(in1, 0)
    board.digital_write(in2, 1)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(tiempo)
    detener_motores()

""" Giro derecha - motor izquierdo vaya adelante y el derecho atrás"""
def girar_derecha(tiempo=2):
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(tiempo)
    detener_motores()

"""Gito izquierdo - motor derecho vaya adelante y el izquierdo atrás"""
def girar_izquierda(tiempo=2):
    board.digital_write(in1, 0)
    board.digital_write(in2, 1)
    board.digital_write(in3, 1)
    board.digital_write(in4, 0)
    time.sleep(tiempo)
    detener_motores()

"""Detener ambos motores"""
def detener_motores():
    board.digital_write(in1, 0)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 0)

try:
    while True:
        # Encender LED para indicar actividad
        board.digital_write(led_pin, 1)

        # Movimientos secuenciales
        mover_adelante(2)
        mover_atras(2)
        girar_derecha(2)
        girar_izquierda(2)

        # Apagar LED
        board.digital_write(led_pin, 0)
        time.sleep(2)

except KeyboardInterrupt:
    print("Saliendo...")
    detener_motores()
    board.shutdown()
