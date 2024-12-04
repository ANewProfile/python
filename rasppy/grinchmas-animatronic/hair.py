from stepper_control import StepperMotor
import time
import RPi.GPIO as GPIO

def rotate_for_duration(motor, duration_seconds, clockwise=True):
    end_time = time.time() + duration_seconds
    
    while time.time() < end_time:
        motor.turn_90_degrees(clockwise)
        # No delay needed between rotations since turn_90_degrees already has small delays

def main():
    try:
        # Using the same pins as defined in your stepper_control.py
        motor_pins = [17, 6, 22, 26]
        motor = StepperMotor(motor_pins)
        
        print("Starting 3-second rotation...")
        rotate_for_duration(motor, 3)
        
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()