from pysimverse import Drone

drone = Drone()
drone.connect()

drone.take_off()
drone.set_speed(80)
drone.rotate(-35)
drone.move_forward(400)

drone.rotate(150)
drone.move_down(80)
drone.move_forward(455)

drone.land()

