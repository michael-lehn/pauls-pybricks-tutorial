from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from sfz import MotorPair

hub = PrimeHub()

m_left = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
m_right = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
m = MotorPair(m_left, m_right)

sensor_left = ColorSensor(Port.D)
sensor_middle = ColorSensor(Port.C)
sensor_right = ColorSensor(Port.F)

sensor = [sensor_left, sensor_middle, sensor_right]

print(f"sensor_middle: {sensor_middle.reflection()}")

while sensor_middle.reflection() > 50:
    m.run_angle(-360, 360, wait=False)
    print(f"sensor_middle: {sensor_middle.reflection()}")
    wait(5)
