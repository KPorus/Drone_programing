from pysimverse import Drone
import cv2
import keyboard


def main():
    drone = Drone()
    drone.connect()
    drone.take_off()

    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0
    SPEED = 100

    while True:
        forward_backward = SPEED if keyboard.is_pressed('w') else 0
        if keyboard.is_pressed('s'):
            forward_backward = -SPEED
        drone.send_rc_control(left_right, forward_backward, up_down, yaw)

if __name__ == "__main__":
    main()


