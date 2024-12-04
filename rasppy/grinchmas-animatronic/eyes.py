import RPi.GPIO as GPIO
import time
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

def blink():
    # Close eyes (90 degrees counterclockwise)
    left_motor.turn_90_degrees(clockwise=False, delay=0.002)
    right_motor.turn_90_degrees(clockwise=False, delay=0.002)
    time.sleep(0.2)  # Keep eyes closed briefly
    
    # Open eyes (90 degrees clockwise)
    left_motor.turn_90_degrees(clockwise=True, delay=0.002)
    right_motor.turn_90_degrees(clockwise=True, delay=0.002)

def main():
    try:
        start_time = time.time()
        end_time = start_time + 18  # Run for 18 seconds total
        
        while time.time() < end_time:
            blink()  # Perform one blink
            
            # Wait for remainder of 3-second interval
            # (unless we've reached the end time)
            time_remaining = end_time - time.time()
            if time_remaining > 0:
                time.sleep(min(5, time_remaining))
    
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        left_motor.cleanup()
        right_motor.cleanup()

if __name__ == "__main__":
    main()
