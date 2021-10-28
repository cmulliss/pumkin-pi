from pumpkinpi import PumpkinPi
from time import sleep

pumpkin = PumpkinPi()

pumpkin.off()  # Just to make sure our pumpkin starts off.

pumpkin.sides.left.blink()
pumpkin.eyes.right.blink()
while True:
    pumpkin.toggle()
    sleep(0.5)
