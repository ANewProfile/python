from stepper_control import StepperMotor
import time
import RPi.GPIO as GPIO

class OscillatingMotor(StepperMotor):
    def turn_20_degrees(self, duration=1, clockwise=True):
        # 20 degrees = (512 steps / 360 degrees) * 20 degrees ≈ 34 steps
        steps = 34
        
        delay = duration / steps
        
        if not clockwise:
            self.sequence.reverse()
            
        for _ in range(steps):
            for step in self.sequence:
                for i in range(4):
                    GPIO.output(self.pins[i], step[i])
                time.sleep(duration)  # Small delay between steps
                
        if not clockwise:
            self.sequence.reverse()
    
    def turn_40_degrees(self, delay=0.001, clockwise=True):
        # 40 degrees = (512 steps / 360 degrees) * 40 degrees ≈ 68 steps
        steps = 68
        
        if not clockwise:
            self.sequence.reverse()
            
        for _ in range(steps):
            for step in self.sequence:
                for i in range(4):
                    GPIO.output(self.pins[i], step[i])
                time.sleep(delay)  # Small delay between steps
                
        if not clockwise:
            self.sequence.reverse()

def oscillate_for_duration(motor, duration_seconds):
    end_time = time.time() + duration_seconds
    
    while time.time() < end_time:
        # Turn 30 degrees (clockwise)
        motor.turn_40_degrees(delay=0.008, clockwise=True)
        
        # slight delay
        time.sleep_ms(75)
        
        # Turn back 30 degrees (counterclockwise)
        motor.turn_40_degrees(delay=0.008, clockwise=False)

def main():
    try:
        GPIO.setmode(GPIO.BCM)
        
        # Define the GPIO pins connected to the ULN2003 driver
        motor_pins = [17, 6, 22, 26]
        motor = OscillatingMotor(motor_pins)
        
        print("Starting 18-second oscillation between -20 and +20 degrees...")
        oscillate_for_duration(motor, 18)
        
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()