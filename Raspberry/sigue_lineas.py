from pymata4 import pymata4
import time

# Inicializar la placa Arduino
board = pymata4.Pymata4()

# Pines
led_pin = 13

# MOTORES:
# Front
in1_m1 = 6  # IN1 - motor 1
in2_m1 = 7  # IN2 - motor 1
in3_m1 = 3  # IN3 - motor 2
in4_m1 = 4  # IN4 - motor 2
# BACK
in1_m2 = 11  # IN1 - motor 3
in2_m2 = 12 # IN2 - motor 3
in3_m2 = 9 # IN3 - motor 4
in4_m2 = 10 # IN4 - motor 4

# SENSORES IR:
sensorIR_1 = 47
sensorIR_2 = 49  
sensorIR_3 = 51 
sensorIR_4 = 53 

# Configurar pines
board.set_pin_mode_digital_output(led_pin)
# MOTORES
board.set_pin_mode_digital_output(in1_m1)
board.set_pin_mode_digital_output(in2_m1)
board.set_pin_mode_digital_output(in3_m1)
board.set_pin_mode_digital_output(in4_m1)
board.set_pin_mode_digital_output(in1_m2)
board.set_pin_mode_digital_output(in2_m2)
board.set_pin_mode_digital_output(in3_m2)
board.set_pin_mode_digital_output(in4_m2)
# IR
sensors = [sensorIR_1, sensorIR_2, sensorIR_3, sensorIR_4]
for sensor in sensors:
    board.set_pin_mode_digital_input(sensor)

""" Move forward - both motors forward """
def move_forward(duration=0.5):
    board.digital_write(in1_m1, 1)
    board.digital_write(in2_m1, 0)
    board.digital_write(in3_m1, 1)
    board.digital_write(in4_m1, 0)
    
    board.digital_write(in1_m2, 1)
    board.digital_write(in2_m2, 0)
    board.digital_write(in3_m2, 1)
    board.digital_write(in4_m2, 0)
    
    time.sleep(duration)
    stop_motors()

def move_forwardv2(duration=0.1):
    state = (1, 0) 

    board.digital_write(in1_m1, state[0])
    board.digital_write(in2_m1, state[1])
    board.digital_write(in3_m1, state[0])
    board.digital_write(in4_m1, state[1])

    board.digital_write(in1_m2, state[0])
    board.digital_write(in2_m2, state[1])
    board.digital_write(in3_m2, state[0])
    board.digital_write(in4_m2, state[1])

    time.sleep(duration)
    stop_motors()

""" Move backward - both motors reverse """
def move_backward(duration=0.5):
    board.digital_write(in1_m1, 0)
    board.digital_write(in2_m1, 1)
    board.digital_write(in3_m1, 0)
    board.digital_write(in4_m1, 1)
    
    board.digital_write(in1_m2, 0)
    board.digital_write(in2_m2, 1)
    board.digital_write(in3_m2, 0)
    board.digital_write(in4_m2, 1)
    time.sleep(duration)
    stop_motors()

""" Turn right - left motor forward, right motor backward """
def turn_right(duration=0.5):
    board.digital_write(in1_m1, 1) 
    board.digital_write(in2_m1, 0)
    board.digital_write(in3_m1, 0) 
    board.digital_write(in4_m1, 1)
    
    board.digital_write(in1_m2, 1) 
    board.digital_write(in2_m2, 0)
    board.digital_write(in3_m2, 0)  
    board.digital_write(in4_m2, 1)
    
    time.sleep(duration)

""" Turn left - right motor forward, left motor backward """
def turn_left(duration=0.5):
    board.digital_write(in1_m1, 0)  
    board.digital_write(in2_m1, 1)
    board.digital_write(in3_m1, 1) 
    board.digital_write(in4_m1, 0)
    
    board.digital_write(in1_m2, 0)  
    board.digital_write(in2_m2, 1)
    board.digital_write(in3_m2, 1) 
    board.digital_write(in4_m2, 0)
    
    time.sleep(duration)
    stop_motors()

""" Stop all motors """
def stop_motors(duration=0.5):
    board.digital_write(in1_m1, 0)
    board.digital_write(in2_m1, 0)
    board.digital_write(in3_m1, 0)
    board.digital_write(in4_m1, 0)
    
    board.digital_write(in1_m2, 0)
    board.digital_write(in2_m2, 0)
    board.digital_write(in3_m2, 0)
    board.digital_write(in4_m2, 0)

try:
    while True:
        # Turn on LED to indicate activity
        board.digital_write(led_pin, 1)
        
        # Read IR sensors
        sensor_values = [board.digital_read(sensor)[0] for sensor in sensors]
        print(f"Sensor A: {sensor_values[0]}, Sensor B: {sensor_values[1]}, Sensor C: {sensor_values[2]}, Sensor D: {sensor_values[3]}")

        # Movement logic
        # Si el sensor de la izquierda y derecha lee blanco estamos sigueindo la linea -> movimiento recto 
        if sensor_values[0] == 0 and sensor_values[3]==0: 
            move_forwardv2(1)
            print("front")
        # Si el sensor de la derecha lee negro es xq se va a salir -> giramos izquierda
        elif sensor_values[0] == 1:  
            turn_left(1)
            print("left")
        # Si el sensor de la izquierda lee negro es xq se va a salir -> giramos derecha
        elif sensor_values[3] == 1:  
            turn_right(1)
            print("right")
            
        # Turn off LED
        board.digital_write(led_pin, 0)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    board.shutdown()
