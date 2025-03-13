from pymata4 import pymata4
import time

board = pymata4.Pymata4()

led_pin = 13
board.set_pin_mode_digital_output(led_pin)
while True:
	board.digital_write(led_pin,1)  # Encender LED
	time.sleep(1)
	board.digital_write(led_pin,0)  # Apagar LED
	time.sleep(1)

print("LED controlado correctamente.")
