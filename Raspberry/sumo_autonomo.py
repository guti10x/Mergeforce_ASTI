from pymata4 import pymata4
import time

# Inicializar la placa Arduino
board = pymata4.Pymata4()

# Pines motores
in1 = 6  # IN1 - motor 1
in2 = 7  # IN2 - motor 1
in3 = 3  # IN3 - motor 2
in4 = 4  # IN4 - motor 2

# Pines sensores IR (para detectar el borde del ring)
sensorIR_1 = 47  # Izquierda
sensorIR_2 = 49  # Centro izquierda
sensorIR_3 = 51  # Centro derecha
sensorIR_4 = 53  # Derecha

# Pines sensor ultrasónico (para detectar oponente)
trig = 9
echo = 8

# Configurar pines de motores
board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)
board.set_pin_mode_digital_output(in3)
board.set_pin_mode_digital_output(in4)

# Configurar pines de sensores IR como entrada
sensors = [sensorIR_1, sensorIR_2, sensorIR_3, sensorIR_4]
for sensor in sensors:
    board.set_pin_mode_digital_input(sensor)

# Configurar sensor ultrasónico
board.set_pin_mode_sonar(trig, echo)

""" Move forward - both motors forward """
def move_forward(duration=2):
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 1)
    board.digital_write(in4, 0)
    time.sleep(duration)
    stop_motors()

""" Move backward - both motors reverse """
def move_backward(duration=2):
    board.digital_write(in1, 0)
    board.digital_write(in2, 1)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(duration)
    stop_motors()

""" Turn right - left motor forward, right motor backward """
def turn_right(duration=0.5):
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(duration)
    stop_motors()

""" Turn left - right motor forward, left motor backward """
def turn_left(duration=0.5):
    board.digital_write(in1, 0)
    board.digital_write(in2, 1)
    board.digital_write(in3, 1)
    board.digital_write(in4, 0)
    time.sleep(duration)
    stop_motors()

""" Stop all motors """
def stop_motors():
    board.digital_write(in1, 0)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 0)

""" Get distance from ultrasonic sensor """
def get_distance():
    time.sleep(0.1)  # Pequeña espera para estabilidad
    return board.sonar_read(trig)[0]  # Distancia en cm

try:
    while True:
        # Leer sensores IR (bordes del ring)
        sensor_values = [board.digital_read(sensor)[0] for sensor in sensors]

        # Leer distancia al oponente
        distance = get_distance()
        
        print(f"Sensors: {sensor_values}, Distance: {distance} cm")

        # **Evitar caer del ring** - Si un sensor IR detecta blanco, hay peligro de salir
        if sensor_values[0] == 0 or sensor_values[3] == 0:  
            move_backward(0.3)  # Retroceder
            turn_right(0.3)  # Girar para evitar caer

        # **Atacar** - Si el oponente está cerca (< 20 cm), avanzar
        elif distance is not None and distance < 20:  
            move_forward(0.2)

        # **Buscar oponente** - Si no hay detección, girar para buscar
        else:
            turn_left(0.2)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    board.shutdown()
