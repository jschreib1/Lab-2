import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep # import time.sleep()
GPIO.setwarnings(False)

def callback_fn(p):
  #ramp up
  #print('Registered')
  if p == inp1:
    pwm2.start(0) # initiate PWM at 0% duty cycle
    for dc in range(51): #loop duty cycle from 0 to 100
      pwm2.ChangeDutyCycle(dc)   # set duty cycle
      sleep(0.01)
  #ramp down
    for d in range(51):
      pwm2.ChangeDutyCycle(51-d)
      sleep(0.01)
      pwm2.stop()
  elif p == inp2:
    pwm3.start(0) # initiate PWM at 0% duty cycle
    for dc in range(51): #loop duty cycle from 0 to 100
      pwm3.ChangeDutyCycle(dc)   # set duty cycle
      sleep(0.01)
  #ramp down
    for d in range(51):
      pwm3.ChangeDutyCycle(51-d)
      sleep(0.01)
      pwm3.stop()

GPIO.setmode(GPIO.BCM) # BCM for GPIO *port* numbering
pins = {}
p1 = 4
p2 = 17
p3 = 13
inp1 = 23
inp2 = 24
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT)
GPIO.setup(inp1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(inp2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

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

'''
GPIO.add_event_detect(inp1, 
GPIO.FALLING,
callback=callback_fn(p2), 
bouncetime=100)
'''
#Event Detect for pin 3
GPIO.add_event_detect(inp2, 
GPIO.RISING,
callback=callback_fn, 
bouncetime=100)

'''
GPIO.add_event_detect(inp2, 
GPIO.FALLING,
callback=callback_fn(p3), 
bouncetime=100)
'''
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

finally:
  GPIO.cleanup()