from flask import Flask
import RPi.GPIO as GPIO
import pygame
import threading
import time

pygame.mixer.init()

led_event = threading.Event()
alarm_event = threading.Event()
wait_event = threading.Event()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


app = Flask(__name__)   # Create an instance of flask called "app"

@app.route("/wait/<string:level>")
def stop(level):
	wait_event.clear()
	def waitInput(level, wait_event):
		while (1):
			if GPIO.input(3)== False:
				led_event.set()
				alarm_event.set()
			else:
				time.sleep(2)
	if level == '1':
		s = threading.Thread(target=waitInput, args=(level, wait_event))
		s.start()
		return "waiting button"
	else: 
		wait_event.set()
		return "not waiting"

#s = threading.Thread(target = stop)
#s.start()

@app.route("/")         # This is our default handler, if no path is given
def index():
	return "hello"

@app.route('/led/<string:level>')
def led(level):
	led = 2
	led_event .clear()
	def blink(level,led_event):
		while (1):
			GPIO.output(led, int(level))
			time.sleep(0.3)
			GPIO.output(led, 0)
			time.sleep(0.3)
			if led_event.is_set():
				break
	if level == '1':
		x = threading.Thread(target=blink, args=(level,led_event))
		x.start()
		return "blinking"
	else:
		led_event.set()
		GPIO.output(led, 0)
		return"led off"

@app.route('/alarm/<string:level>')
def alert(level):
	alarm_event.clear()
	def ring(level, alarm_event):
		while(1):
			pygame.mixer.init()
			sound = pygame.mixer.Sound("3alert.wav")
			pygame.mixer.Sound.play(sound)
			time.sleep(4)
			pygame.mixer.Sound.stop(sound)
			if alarm_event.is_set():
				break

	if level == '1':
		y = threading.Thread(target=ring, args=(level, alarm_event))
		y.start()
		return "ring"

	else:
		alarm_event.set()
		return "stopped ringing"

if __name__ == "__main__":
    app.run(host='10.104.80.77', port=5000)
