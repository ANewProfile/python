import RPi.GPIO as GPIO
from time import sleep_ms
from stepper_control import StepperMotor

# set board mode
GPIO.setmode(GPIO.BCM)

# setup output pins
left_eye = (14, 15, 18, 23)
for pin in left_eye:
    GPIO.setup(pin, GPIO.OUT)
    
right_eye = (24, 25, 8, 7)
for pin in right_eye:
    GPIO.setup(pin, GPIO.OUT)

# Initialize stepper motors
left_motor = StepperMotor(left_eye)
right_motor = StepperMotor(right_eye)

# functions
def left_open():
    left_motor.turn_90_degrees(clockwise=True)

def left_close():
    left_motor.turn_90_degrees(clockwise=False)

def right_open():
    right_motor.turn_90_degrees(clockwise=True)

def right_close():
    right_motor.turn_90_degrees(clockwise=False)

# variables
running = True
i = 0
between_blinks = 5

# main loop
try:
    while running:
        # check to stop
        if i >= 300*between_blinks:  # temporary condition
            running = False
        
        # check if ready to blnk
        if i % (10*between_blinks) == 0:
            if (i / (10*between_blinks)) % (20*between_blinks) == 0:
                left_open()
                right_open()
            else:
                left_close()
                right_close()
        else:
            i += 1
            sleep_ms(100)
finally:
    # Cleanup GPIO
    left_motor.cleanup()
    right_motor.cleanup()
