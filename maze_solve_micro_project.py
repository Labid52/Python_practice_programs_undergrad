from robot_control_class import RobotControl
rc = RobotControl()
while 1 :
    r360 = rc.get_laser(360)
    r0 = rc.get_laser(0)
    r719 = rc.get_laser(719)
    if r360 > 1 and r0 < 100 and r719 < 100:
        rc.move_straight()
        r360 = rc.get_laser(360)
        print("the value of sensor", r360)
    if r360 > 100 and r0 > 100 and r719 > 100:
        rc.stop_robot()
        print("Congratz!!, you have solved the maze")
    rc.stop_robot()

    if r360 < 1:
        if r0 > r719:
            print("the zero position", r0)
            rc.rotate(75)
        elif r719 > r0:
            print("the final position", r719)
            rc.rotate(-75)
        elif r0 == r719:
            rc.move_straight()
