from pysimverse import Drone
import time

drone = Drone()
drone.connect()

drone.take_off()
time.sleep(5)
drone.rotate(180)
time.sleep(2)
drone.rotate(-180)
time.sleep(5)

drone.land()
