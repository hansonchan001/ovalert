
import RPi.GPIO as GPIO
import time

led = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

def led(level):
    while True:
        GPIO.output(led, 1) #led on
        time.sleep(0.3)
        GPIO.output(led, 0) #led off
        time.sleep(0.3)

led()