import RPi.GPIO as GPIO
class Motor:
    MotorIn1 = 0
    MotorIn2 = 0
    MotorEn = 0

    def __init__(self,MotorIn1,MotorIn2,MotorEn) -> None:
        self.MotorIn1 = MotorIn1
        self.MotorIn2 = MotorIn2
        self.MotorEn = MotorEn

    def configure(self,ext_In1,ext_In2,ext_En,ext_PWM_freq):
        self.MotorIn1 = ext_In1
        self.MotorIn2 = ext_In2
        self.MotorEn = ext_En
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.MotorIn1,GPIO.OUT)
        GPIO.setup(self.MotorIn2,GPIO.OUT)
        GPIO.setup(self.MotorEn,GPIO.OUT)
        PWM = GPIO.PWM(self.MotorEn,ext_PWM_freq)
        PWM.start(25)
        return PWM

    def change_direction(self,ext_direction) -> None:
        if ext_direction == "Forward":
            print("Forward 25%")
            GPIO.output(self.MotorIn1,GPIO.HIGH)
            GPIO.output(self.MotorIn2,GPIO.LOW)
        if ext_direction == "Backward":
            print("Forward 25%")
            GPIO.output(self.MotorIn1,GPIO.LOW)
            GPIO.output(self.MotorIn1,GPIO.HIGH)

    def change_velocity(self,PWM,ext_cycle) -> None:
        if ext_cycle <= 75 and ext_cycle > 0 :
            PWM.ChangeDutyCycle(ext_cycle)
        else:
            print("Niewłaściwa wartość wypełnienia")

    def stop(self) -> None:
        GPIO.cleanup()
