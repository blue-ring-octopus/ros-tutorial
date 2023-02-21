#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:10:44 2023

@author: barc
"""

import rospy
from geometry_msgs.msg import Twist
  
def talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x=1
        msg.angular.z=1
        pub.publish(msg)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass