import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep # import time.sleep()

def callback_fn(pin):
  #ramp up
  pin.start(0) # initiate PWM at 0% duty cycle
  for dc in range(101): #loop duty cycle from 0 to 100
    pin.ChangeDutyCycle(dc)   # set duty cycle
    sleep(0.01)
  #ramp down
  for d in range(101):
    pin.ChangeDutyCycle(100-d)
    sleep(0.01)

GPIO.setmode(GPIO.BCM) # BCM for GPIO *port* numbering
p1 = 4
p2 = 17
p3 = 18
inp1 = 23
inp2 = 24
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT) 

f = 1000 # frequency (Hz)
dc = 50 # duty cycle (%)
pwm1 = GPIO.PWM(p1,f)
pwm2 = GPIO.PWM(p2,f)
pwm3 = GPIO.PWM(p3,f)

#Event Detection for pin 2
GPIO.add_event_detect(inp1, 
GPIO.RISING,
callback=callback_fn, 
bouncetime=100)

GPIO.add_event_detect(inp1, 
GPIO.FALLING,
callback=callback_fn, 
bouncetime=100)

#Event Detect for pin 3
GPIO.add_event_detect(inp2, 
GPIO.RISING,
callback=callback_fn, 
bouncetime=100)

GPIO.add_event_detect(inp2, 
GPIO.FALLING,
callback=callback_fn, 
bouncetime=100)

try:
  while True:
    GPIO.output(p1,0)
    sleep(0.5)
    GPIO.output(p1,1)
    sleep(0.5)
except KeyboardInterrupt:
  print("\nShutting down...")
except Exception as e:
  print('\ne')

GPIO.cleanup()