#### Pins
in1 = 24    #DC Motor pin - direction
in2 = 23    #DC Motor pin - direction
en = 25     #DC Motor pin - PWM
clk = 17    #Encoder pin
dt = 27     #Encoder pin

### Controller Parameters
k = 0.92  #Controller Gain
t = 0.8   #Controller Time Constant
tp = 0.5  #Sampling Time


### Motor Parameters
upper_limit = 80    #Max PWM value
lower_limit = 0     #Min PWM value
starting_speed = 25 #Starting PWM value
