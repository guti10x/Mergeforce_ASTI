from pymata4 import pymata4
import time
from config import *
from utils import mover_motores, detener

board = pymata4.Pymata4()

board.set_pin_mode_analog_input(SENSOR_IZQ)
board.set_pin_mode_analog_input(SENSOR_CEN_IZQ)
board.set_pin_mode_analog_input(SENSOR_CEN_DER)
board.set_pin_mode_analog_input(SENSOR_DER)

board.set_pin_mode_pwm_output(MOTOR_IZQ_PWM)
board.set_pin_mode_digital_output(MOTOR_IZQ_DIR1)
board.set_pin_mode_digital_output(MOTOR_IZQ_DIR2)
board.set_pin_mode_pwm_output(MOTOR_DER_PWM)
board.set_pin_mode_digital_output(MOTOR_DER_DIR1)
board.set_pin_mode_digital_output(MOTOR_DER_DIR2)

print("Modo Sigue Líneas iniciado...")

while True:
    # Leer valores de los sensores (normalizados entre 0 y 1)
    izq = board.analog_read(SENSOR_IZQ)[0] / 1023.0
    cen_izq = board.analog_read(SENSOR_CEN_IZQ)[0] / 1023.0
    cen_der = board.analog_read(SENSOR_CEN_DER)[0] / 1023.0
    der = board.analog_read(SENSOR_DER)[0] / 1023.0
    
    if cen_izq > UMBRAL_LINEA and cen_der > UMBRAL_LINEA:
        mover_motores(board, 150, 150)
        print("Avanzando recto")
    elif izq > UMBRAL_LINEA or cen_izq > UMBRAL_LINEA:
        mover_motores(board, 50, 150)
        print("Girando a la izquierda")
    elif der > UMBRAL_LINEA or cen_der > UMBRAL_LINEA:
        mover_motores(board, 150, 50)
        print("Girando a la derecha")
    else:
        detener(board)
        print("Detenido")
    
    time.sleep(0.1)  