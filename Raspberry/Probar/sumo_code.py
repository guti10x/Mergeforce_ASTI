from pymata4 import pymata4
import time
import random


board = pymata4.Pymata4()


in1 = 6  # IN1 - motor 1 (izquierdo)
in2 = 7  # IN2 - motor 1 (izquierdo)
in3 = 3  # IN3 - motor 2 (derecho)
in4 = 4  # IN4 - motor 2 (derecho)


sensorIR_1 = 47  # Sensor frontal izquierdo
sensorIR_2 = 49  # Sensor frontal central izquierdo
sensorIR_3 = 51  # Sensor frontal central derecho
sensorIR_4 = 53  # Sensor frontal derecho


board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)
board.set_pin_mode_digital_output(in3)
board.set_pin_mode_digital_output(in4)


sensors = [sensorIR_1, sensorIR_2, sensorIR_3, sensorIR_4]
for sensor in sensors:
    board.set_pin_mode_digital_input(sensor)


def move_forward(duration=0.1):
    """Avanzar: ambos motores hacia adelante"""
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 1)
    board.digital_write(in4, 0)
    time.sleep(duration)
    stop_motors()

def move_backward(duration=0.5):
    """Retroceder: ambos motores hacia atrás"""
    board.digital_write(in1, 0)
    board.digital_write(in2, 1)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(duration)
    stop_motors()

def turn_right(duration=0.5):
    """Girar a la derecha: motor izquierdo adelante, motor derecho atrás"""
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(duration)
    stop_motors()

def turn_left(duration=0.5):
    """Girar a la izquierda: motor derecho adelante, motor izquierdo atrás"""
    board.digital_write(in1, 0)
    board.digital_write(in2, 1)
    board.digital_write(in3, 1)
    board.digital_write(in4, 0)
    time.sleep(duration)
    stop_motors()

def stop_motors():
    """Detener todos los motores"""
    board.digital_write(in1, 0)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 0)


try:
    while True:
        # Leer los valores de los sensores IR (0 = línea detectada, 1 = no línea)
        sensor_values = [board.digital_read(sensor)[0] for sensor in sensors]
        
        # opcional, para depuración
        print(f"Sensor 1: {sensor_values[0]}, Sensor 2: {sensor_values[1]}, Sensor 3: {sensor_values[2]}, Sensor 4: {sensor_values[3]}")

        # Estrategia para SUMO
        if sensor_values[1] == 0 or sensor_values[2] == 0:  # Sensores frontales detectan línea
            move_backward(0.5)  # Retroceder para alejarse del borde
            # Girar aleatoriamente para cambiar dirección
            if random.choice([0, 1]):
                turn_left(0.5)
            else:
                turn_right(0.5)
        elif sensor_values[0] == 0:  # Sensor lateral izquierdo detecta línea
            turn_right(0.5)  # Girar a la derecha para alejarse del borde
        elif sensor_values[3] == 0:  # Sensor lateral derecho detecta línea
            turn_left(0.5)  # Girar a la izquierda para alejarse del borde
        else:
            move_forward(0.1)  # Avanzar si no hay línea detectada

except KeyboardInterrupt:
    print("Saliendo...")
    stop_motors()
    board.shutdown()