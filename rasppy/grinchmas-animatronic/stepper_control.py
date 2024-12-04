import RPi.GPIO as GPIO
import time

class StepperMotor:
    def __init__(self, pins):
        # Setup the GPIO pins
        self.pins = pins
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)
        
        # Stepper motor sequence (clockwise)
        self.sequence = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
        ]
        
    def cleanup(self):
        GPIO.cleanup()
        
    def turn_90_degrees(self, delay=0.001, clockwise=True):
        # 28BYJ-48 motor has 512 steps for a full rotation (8 sequences × 64 gear reduction)
        # So for 90 degrees we need 512/4 = 128 steps
        steps = 128
        
        if not clockwise:
            self.sequence.reverse()
            
        for _ in range(steps):
            for step in self.sequence:
                for i in range(4):
                    GPIO.output(self.pins[i], step[i])
                time.sleep(delay)  # Small delay between steps
                
        if not clockwise:
            self.sequence.reverse()  # Reset sequence to original order

def main():
    try:
        GPIO.setmode(GPIO.BCM)
        
        # Define the GPIO pins connected to the ULN2003 driver
        # Change these pin numbers according to your wiring
        motor_pins = [14, 15, 18, 23]
        
        # Create stepper motor instance
        motor = StepperMotor(motor_pins)
        
        print("Turning 90 degrees clockwise...")
        motor.turn_90_degrees(clockwise=True)
        time.sleep(1)
        
        print("Turning 90 degrees counter-clockwise...")
        motor.turn_90_degrees(clockwise=False)
        
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
