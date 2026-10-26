from pysimverse import Drone
import time

drone = Drone()
drone.connect()

drone.take_off()
drone.set_speed(60)
drone.rotate(-75)
drone.move_forward(200)

drone.rotate(125)
drone.move_forward(120)

drone.rotate(20)
drone.move_forward(400)
drone.land()

