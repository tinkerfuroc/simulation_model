#!/usr/bin/env python2
import rospy
from std_msgs.msg import Float64
from pan_tilt_msg.msg import PanTiltCmd

pi = 3.1415927

def callback(data):
    yaw_arc = data.yaw/180.0*pi
    pitch_arc = data.pitch/180.0*pi

    yaw_pub = rospy.Publisher('/pan_tilt/pan_tilt_yaw/command', Float64, queue_size=10)
    pitch_pub = rospy.Publisher('/pan_tilt/pan_tilt_pitch/command', Float64, queue_size=10)

    yaw_pub.publish(yaw_arc)
    pitch_pub.publish(pitch_arc)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/pan_tilt_driver_node/pan_tilt_cmd", PanTiltCmd, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
