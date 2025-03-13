from pymata4 import pymata4
import time


board = pymata4.Pymata4()


led_pin = 13


in1 = 6  # IN1 - motor 1 (izquierdo)
in2 = 7  # IN2 - motor 1 (izquierdo)
in3 = 3  # IN3 - motor 2 (derecho)
in4 = 4  # IN4 - motor 2 (derecho)


sensorIR_1 = 47  # Sensor extremo izquierdo
sensorIR_2 = 49  # Sensor central izquierdo
sensorIR_3 = 51  # Sensor central derecho
sensorIR_4 = 53  # Sensor extremo derecho


board.set_pin_mode_digital_output(led_pin)
board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)
board.set_pin_mode_digital_output(in3)
board.set_pin_mode_digital_output(in4)


sensors = [sensorIR_1, sensorIR_2, sensorIR_3, sensorIR_4]
for sensor in sensors:
    board.set_pin_mode_digital_input(sensor)

# Velocidad base para los motores (0-255 para PWM, pero aquí usamos 1/0)
BASE_SPEED = 1  # Usamos 1 para avanzar, 0 para detener


def move_forward():
    """Avanzar: ambos motores hacia adelante"""
    board.digital_write(in1, BASE_SPEED)
    board.digital_write(in2, 0)
    board.digital_write(in3, BASE_SPEED)
    board.digital_write(in4, 0)

def turn_left():
    """Girar a la izquierda: motor derecho adelante, motor izquierdo atrás"""
    board.digital_write(in1, 0)
    board.digital_write(in2, BASE_SPEED)
    board.digital_write(in3, BASE_SPEED)
    board.digital_write(in4, 0)

def turn_right():
    """Girar a la derecha: motor izquierdo adelante, motor derecho atrás"""
    board.digital_write(in1, BASE_SPEED)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, BASE_SPEED)

def stop_motors():
    """Detener todos los motores"""
    board.digital_write(in1, 0)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 0)


def read_sensors():
    """Lee los valores de los sensores IR y devuelve una lista"""
    return [board.digital_read(sensor)[0] for sensor in sensors]

try:
    
    print("Calibrando sensores... (simulado)")
    time.sleep(2)  # Simula calibración

    while True:
        
        sensor_values = read_sensors()
        
        
        print(f"Sensor 1: {sensor_values[0]}, Sensor 2: {sensor_values[1]}, Sensor 3: {sensor_values[2]}, Sensor 4: {sensor_values[3]}")

        
        if sensor_values[1] == 0 and sensor_values[2] == 0:
            # Línea en el centro, avanzar recto
            move_forward()
        elif sensor_values[0] == 0:
            # Línea a la izquierda, girar a la izquierda
            turn_left()
        elif sensor_values[3] == 0:
            # Línea a la derecha, girar a la derecha
            turn_right()
        elif all(v == 1 for v in sensor_values):
            # No se detecta línea, buscarla (girar a la izquierda)
            turn_left()
        else:
            # Caso por defecto: detener
            stop_motors()

        # Pequeña pausa para no saturar la CPU
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Saliendo...")
    stop_motors()
    board.shutdown()