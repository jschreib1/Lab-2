import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep # import time.sleep()

GPIO.setmode(GPIO.BCM) # BCM for GPIO *port* numbering
p1 = 4
p2 = 17
p3 = 18
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT) 

f = 1 # frequency (Hz)
dc = 50 # duty cycle (%)
pwm1 = GPIO.PWM(p1,f)
pwm2 = GPIO.PWM(p2,f)
pwm3 = GPIO.PWM(p3,f)

try:
  while True:
    GPIO.output(p1,0)
    sleep(0.5)
    GPIO.output(p1,1)
    sleep(0.5)
    GPIO.output(p2,0)
    sleep(0.5)
    GPIO.output(p2,1)
    sleep(0.5)
    GPIO.output(p3,0)
    sleep(0.5)
    GPIO.output(p3,1)
    sleep(0.5)
except KeyboardInterrupt:
  print("\nShutting down...")
except Exception as e:
  print('\ne')

GPIO.cleanup()