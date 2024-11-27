#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
FrontL = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
FrontR = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
BottomL = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
BottomR = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)
ConveyorMotor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
ClawMotor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, True)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration


myVariable = 0


def when_started1():
    global myVariable


when_started1()


#motor1 is FL
#motor2 is FR
#motor3 is BL
#motor4 is BR
#motors 2 and 4 are set to reverse



def axis3_changed():
    while controller_1.axis3.position() > 25 or controller_1.axis3.position() < -25:
        FrontL.spin(FORWARD)
        FrontR.spin(FORWARD)
        BottomL.spin(FORWARD)
        BottomR.spin(FORWARD)
        FrontL.set_velocity(controller_1.axis3.position()/2, PERCENT)
        FrontR.set_velocity(controller_1.axis3.position()/2, PERCENT)
        BottomL.set_velocity(controller_1.axis3.position()/2, PERCENT)
        BottomR.set_velocity(controller_1.axis3.position()/2, PERCENT)
    
    FrontL.stop()
    FrontR.stop()
    BottomL.stop()
    BottomR.stop()

def axis4_changed():
    while controller_1.axis4.position() > 25 or controller_1.axis4.position() < -25:
        FrontL.spin(FORWARD)
        FrontR.spin(FORWARD)
        BottomL.spin(FORWARD)
        BottomR.spin(FORWARD)

        FrontL.set_velocity(controller_1.axis4.position()/2, PERCENT)
        FrontR.set_velocity(-controller_1.axis4.position()/2, PERCENT)
        BottomL.set_velocity(-controller_1.axis4.position()/2, PERCENT)
        BottomR.set_velocity(controller_1.axis4.position()/2, PERCENT)

    FrontL.stop()
    FrontR.stop()
    BottomL.stop()
    BottomR.stop()

def axis1_changed():
    while controller_1.axis1.position() > 25 or controller_1.axis1.position() < -25:
        FrontL.spin(FORWARD)
        FrontR.spin(FORWARD)
        BottomL.spin(FORWARD)
        BottomR.spin(FORWARD)

        FrontL.set_velocity(controller_1.axis1.position()/4, PERCENT)
        FrontR.set_velocity(-controller_1.axis1.position()/4, PERCENT)
        BottomL.set_velocity(controller_1.axis1.position()/4, PERCENT)
        BottomR.set_velocity(-controller_1.axis1.position()/4, PERCENT)

    FrontL.stop()
    FrontR.stop()
    BottomL.stop()
    BottomR.stop()
    

controller_1.axis3.changed(axis3_changed)
controller_1.axis4.changed(axis4_changed)
controller_1.axis1.changed(axis1_changed)

#press is to monitor how many time our button to start the motor was pressed
conveyor_press = 0
def conveyor():
    global conveyor_press
    conveyor_press = 1 - conveyor_press
    if conveyor_press == 0:
        ConveyorMotor.set_velocity(0, PERCENT)
        ConveyorMotor.stop()
    elif conveyor_press == 1:
        ConveyorMotor.spin(FORWARD)
        ConveyorMotor.set_velocity(45, PERCENT)


controller_1.buttonR1.pressed(conveyor)

def conveyor_back():
    ConveyorMotor.set_velocity(-45, PERCENT)
    ConveyorMotor.spin(FORWARD)

def conveyor_stop():
    ConveyorMotor.set_velocity(0, PERCENT)
    ConveyorMotor.stop()

controller_1.buttonR2.pressed(conveyor_back)
controller_1.buttonR2.released(conveyor_stop)

claw_press = 0
def claw_button_press():
    global claw_press
    claw_press = 1 - claw_press
    if claw_press == 1:
        ClawMotor.spin_for(FORWARD, 120, DEGREES)
    elif claw_press == 0:
        ClawMotor.spin_for(REVERSE,120, DEGREES)

controller_1.buttonL1.pressed(claw_button_press)



def autonomous():
   # Start by driving forward 500 mm 
    FrontL.spin(FORWARD)
    FrontR.spin(FORWARD)
    BottomL.spin(FORWARD)
    BottomR.spin(FORWARD)
    wait(2, SECONDS)
    FrontL.stop()
    FrontR.stop()
    BottomL.stop()
    BottomR.stop()
    pass

while True:
    if(FrontL.temperature(PERCENT) > 85):
        brain.screen.print("FrontL OVERHEATING")
    if(FrontR.temperature(PERCENT) > 85):
        brain.screen.print("FrontR OVERHEATING")
    if(BottomR.temperature(PERCENT) > 85):
        brain.screen.print("BottomR OVERHEATING")
    if(BottomL.temperature(PERCENT) > 85):
        brain.screen.print("BottomL OVERHEATING")
    if(ConveyorMotor.temperature(PERCENT) > 85):
        brain.screen.print("ConveyorMotor OVERHEATING")
    if(ClawMotor.temperature(PERCENT) > 85):
        brain.screen.print("ClawMotor OVERHEATING")




'''
AUTONOMOUS REQUIREMENTS:
At least three (3) Scored Rings
A minimum of two (2) Stakes with at least(1) Ring Scored
Neither Robot contacting / breaking the plane of the Starting Line
At least one (1) Robot contacting the Ladder


make robot go forward 40 inches forward, spin 180 degrees and then move remaining 6.64 inches to
the goalpost, grip onto it with our claw. we will move one more inch forward to align with 
the donut to our left (or right depending on our color) then we will turn 90 degrees. we will then move
24 inches forward and then feed in the donut that we moved to, pushing it into the goalpost we have
attached. then we will move 90 degrees again. move 24 inches and feed in the next donut. we then rotate
90 degrees and move 47.50 inches to pick up the other teams donut, but rotate 90 degrees again and move
11.15 inches to pick up the last donut. after that, to not break the starting plane, we move back 34.64
inches to touch the ladder as well, then we are done.






'''