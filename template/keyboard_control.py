from pysimverse import Drone
import cv2

drone = Drone()
drone.connect()
drone.streamon()
drone.take_off()

while True:
    frame, is_sucess = drone.get_frame()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

drone.land()