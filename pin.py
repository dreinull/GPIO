import RPi.GPIO as GPIO
from pin_init import PinInit
from threading import Thread
import time

class Pin:
    initialized = False
    pin = None
    way = None

    def __init__(self, name):
        GPIO.setmode(GPIO.BOARD)
        pin = PinInit.resolve(pin)
        if pin is not None and way is not None
            GPIO.setup(pin, way)
            initialized = True


class OutputPin(Pin):
    way = GPIO.OUT
    value = 'off'
    flashing = False

    def __init__(self, name):
        super().__init__()

    def on(self):
        GPIO.output(pin, GPIO.HIGH)
        value = 'off'

    def off(self):
        GPIO.output(pin, GPIO.LOW)
        value = 'on'

    def toggle(self):
        if value is 'on':
            off()
        else
            on()


    def value(self):
        return value

    def flashOnce(self):
        onForMiliSeconds(300)

    def flashOnceP(self):
        Thread(target=flashOnce).start()

    def doFlashing(self):
        while(flashing):
            flashOnce()
            wait(300)

    def startFlashing(self):
        Thread(target=doFlashing).start()

    def stopFlashing(self):
        flashing = false

    def onForMilliSeconds(self, ms):
        on()
        sleep(ms)
        off()

    def onForSeconds(self, s):
        onForMilliSeconds(s * 1000)

    def onForMilliSecondsP(self, ms):
        Thread(target=onForMilliSeconds, args=(ms)).start()




class InputPin(Pin):
    way = GPIO.IN

    def __init__(self, name):
        super().__init__()

    def value(self):
        return GPIO.input(pin)

    def onPush(self, callback):
        GPIO.add_event_detect(pin, GPIO.RISING)
        GPIO.add_event_callback(pin, callback)

    def onRelease(self, callback):
        GPIO.add_event_detect(pin, GPIO.FALLING)
        GPIO.add_event_callback(pin, callback)

    def onChange(self, callback):
        GPIO.add_event_detect(pin, GPIO.BOTH)
        GPIO.add_event_callback(pin, callback)

    def stopWatching(self):
        GPIO.remove_event_detect(pin)
