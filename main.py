from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from sfz import MotorPair

hub = PrimeHub()

m_left = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
sensor_left = ColorSensor(Port.D)


m_left.run(360)
wait(1000)
m_left.stop()

print(f"sensor_middle: {sensor_left.reflection()}")
