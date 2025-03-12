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

sensorIR_1 = 47
sensorIR_2 = 49  
sensorIR_3 = 51 
sensorIR_4 = 53 

# Configurar pines
board.set_pin_mode_digital_output(led_pin)

board.set_pin_mode_digital_output(in1)
board.set_pin_mode_digital_output(in2)
board.set_pin_mode_digital_output(in3)
board.set_pin_mode_digital_output(in4)

# Configurar pines como entradas digitales
sensors = [sensorIR_1, sensorIR_2, sensorIR_3, sensorIR_4]
for sensor in sensors:
    board.set_pin_mode_digital_input(sensor)

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
def turn_right(duration=2):
    board.digital_write(in1, 1)
    board.digital_write(in2, 0)
    board.digital_write(in3, 0)
    board.digital_write(in4, 1)
    time.sleep(duration)
    stop_motors()

""" Turn left - right motor forward, left motor backward """
def turn_left(duration=2):
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

try:
    while True:
        # Turn on LED to indicate activity
        board.digital_write(led_pin, 1)
        
        # Read IR sensors
        sensor_values = [board.digital_read(sensor)[0] for sensor in sensors]
        
        print(f"Sensor 1: {sensor_values[0]}, Sensor 2: {sensor_values[1]}, Sensor 3: {sensor_values[2]}, Sensor 4: {sensor_values[3]}")

        # Movement logic
        if sensor_values[1] == 0 and sensor_values[2] == 0: 
            move_forward(0.1)
        elif sensor_values[0] == 0:  
            turn_left(0.1)
        elif sensor_values[3] == 0:  
            turn_right(0.1)
        elif all(v == 1 for v in sensor_values):  
            move_backward(0.5)

        # Turn off LED
        board.digital_write(led_pin, 0)
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    board.shutdown()
