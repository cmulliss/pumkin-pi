from pumpkinpi import PumpkinPi
from time import sleep

# Define a function to control our Pumpkin which takes a PumpkinPi as an argument.

# instance of pumpkin class, object to use in python
pumpkin = PumpkinPi()

pumpkin.off()

# all lights on
pumpkin.sides.on()

# eyes
pumpkin.eyes.left.on()


def pump_eyes(pumpkin):

    pumpkin.eyes.left.blink(
        0.1, 0.1, 0, 0, 3
    )  # Blink on for .1 seconds, off for .1 seconds, do not fade and do this 12 times.
    sleep(3)
    pumpkin.eyes.right.blink(
        0.1, 0.1, 0, 0, 3
    )  # Blink on for .1 seconds, off for .1 seconds, do not fade and do this 12 times.

    pumpkin.off()


pumpkin = PumpkinPi(pwm=True)

while True:
    pump_eyes(pumpkin)
else:
    pumpkin.close()
