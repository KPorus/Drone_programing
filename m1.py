from pysimverse import Drone
import time

drone = Drone()
drone.connect()

drone.take_off()
drone.set_speed(30)
drone.rotate(50)
drone.move_forward(340)
drone.land()