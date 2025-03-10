
from pymata4 import pymata4
import time
import random
from config import *
from utils import mover_motores, detener


board = pymata4.Pymata4()


board.set_pin_mode_analog_input(SENSOR_CEN_IZQ)
board.set_pin_mode_analog_input(SENSOR_CEN_DER)


board.set_pin_mode_pwm_output(MOTOR_IZQ_PWM)
board.set_pin_mode_digital_output(MOTOR_IZQ_DIR1)
board.set_pin_mode_digital_output(MOTOR_IZQ_DIR2)
board.set_pin_mode_pwm_output(MOTOR_DER_PWM)
board.set_pin_mode_digital_output(MOTOR_DER_DIR1)
board.set_pin_mode_digital_output(MOTOR_DER_DIR2)

print("Modo SUMO Autónomo iniciado...")

while True:
    # Leer sensores frontales (valores de 0 a 1)
    cen_izq = board.analog_read(SENSOR_CEN_IZQ)[0] / 1023.0
    cen_der = board.analog_read(SENSOR_CEN_DER)[0] / 1023.0
    
    # Detectar borde
    if cen_izq > UMBRAL_LINEA or cen_der > UMBRAL_LINEA:
        # Retroceder
        mover_motores(board, -100, -100)
        time.sleep(0.5)
        # Girar aleatoriamente
        if random.choice([0, 1]):
            mover_motores(board, -100, 100)  # Izquierda
        else:
            mover_motores(board, 100, -100)  # Derecha
        time.sleep(0.5)
    else:
        # Avanzar recto
        mover_motores(board, 150, 150)
    
    time.sleep(0.1)