# utils.py
import time
from config import MOTOR_IZQ_PWM, MOTOR_IZQ_DIR1, MOTOR_IZQ_DIR2, MOTOR_DER_PWM, MOTOR_DER_DIR1, MOTOR_DER_DIR2

def mover_motores(board, vel_izq, vel_der):
    """Controla motores con velocidades entre -255 y 255."""
    # Motor izquierdo
    if vel_izq >= 0:
        board.digital_write(MOTOR_IZQ_DIR1, 1)
        board.digital_write(MOTOR_IZQ_DIR2, 0)
        board.analog_write(MOTOR_IZQ_PWM, min(vel_izq, 255))
    else:
        board.digital_write(MOTOR_IZQ_DIR1, 0)
        board.digital_write(MOTOR_IZQ_DIR2, 1)
        board.analog_write(MOTOR_IZQ_PWM, min(-vel_izq, 255))
    
    # Motor derecho
    if vel_der >= 0:
        board.digital_write(MOTOR_DER_DIR1, 1)
        board.digital_write(MOTOR_DER_DIR2, 0)
        board.analog_write(MOTOR_DER_PWM, min(vel_der, 255))
    else:
        board.digital_write(MOTOR_DER_DIR1, 0)
        board.digital_write(MOTOR_DER_DIR2, 1)
        board.analog_write(MOTOR_DER_PWM, min(-vel_der, 255))

def detener(board):
    """Detiene los motores."""
    mover_motores(board, 0, 0)