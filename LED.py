import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
GPIO.setwarnings(False)

# Define GPIO pins for the LEDs
led_pins = [14, 15, 17, 18]

# Set all LED pins as output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Pattern 1: Blink one LED at a time
def pattern_1():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)  # Turn LED on
        time.sleep(0.5)
        GPIO.output(pin, GPIO.LOW)   # Turn LED off
        time.sleep(0.5)

# Pattern 2: All LEDs ON, then all OFF
def pattern_2():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)  # All LEDs on
    time.sleep(1)
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)   # All LEDs off
    time.sleep(1)

# Pattern 3: Toggle one by one (On-Off for each LED)
def pattern_3():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)  # Turn LED on
        time.sleep(0.5)
        GPIO.output(pin, GPIO.LOW)   # Turn LED off
        time.sleep(0.5)

# Pattern 4: Toggle all LEDs simultaneously
def pattern_4():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)  # Turn all LEDs on
    time.sleep(0.5)
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)   # Turn all LEDs off
    time.sleep(0.5)

# Main function to run the patterns
try:
    while True:
        print("Pattern 1: Blink one LED at a time")
        pattern_1()
        
        print("Pattern 2: All LEDs ON, then all OFF")
        pattern_2()
        
        print("Pattern 3: Toggle LEDs one by one")
        pattern_3()
        
        print("Pattern 4: Toggle all LEDs simultaneously")
        pattern_4()

except KeyboardInterrupt:
    print("Exiting program")

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
