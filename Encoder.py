# Class to monitor a rotary encoder and update a value.  You can either read the value when you need it, by calling getValue(), or
# you can configure a callback which will be called whenever the value changes.

import RPi.GPIO as GPIO

class Encoder:

    def __init__(self, leftPin, rightPin, callback=None):
        self.leftPin = leftPin
        self.rightPin = rightPin
        self.value = 0
        self.a = 0
        self.b = 0
        self.direction = None
        self.callback = callback
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.leftPin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        GPIO.setup(self.rightPin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        GPIO.add_event_detect(self.leftPin, GPIO.RISING, callback=self.transitionOccurred)
        GPIO.add_event_detect(self.rightPin, GPIO.RISING, callback=self.transitionOccurred)

    def transitionOccurred(self, channel):
        if channel == self.leftPin:  #Obrot w lewo
            if self.b:
                self.value = self.value + 1
                self.direction = "L"
                self.a = 0
                self.b = 0
            else:
                self.a = 1
        else:
            if self.a:
                self.value = self.value - 1
                self.direction = "R"
                self.a = 0
                self.b = 0
            else:
                self.b = 1

    def getValue(self):
        return self.value

    def clearValue(self):
        self.value = 0

    def testCb(self, channel):
        print(f'Cb {channel}')
