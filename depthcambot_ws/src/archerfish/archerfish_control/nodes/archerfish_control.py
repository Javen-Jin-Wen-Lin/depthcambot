#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import sys, select, os
import math

if os.name == 'nt':
  import msvcrt, time
else:
  import tty, termios

stepmove = 0.1

amove = 1.0
rmove = 0.0

def getKey():
    if os.name == 'nt':
        timeout = 0.1
        startTime = time.time()
        while(1):
            if msvcrt.kbhit():
                if sys.version_info[0] >= 3:
                    return msvcrt.getch().decode()
                else:
                    return msvcrt.getch()
            elif time.time() - startTime > timeout:
                return ''

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def change_joint_state():

    global amove
    global rmove
    
    rospy.init_node('arobot_publisher', anonymous=True)
    puba = rospy.Publisher('/arobot/joint1_position_controller/command', Float64, queue_size=10)
    pubb = rospy.Publisher('/arobot/joint2_position_controller/command', Float64, queue_size=10)
    
    rospy.sleep(1.0)
    
    rate = rospy.Rate(10)  # Publish at a rate of 10 Hz
    
    while not rospy.is_shutdown():
    
        joint_state = JointState()
        joint_state.header.stamp = rospy.Time.now()
        joint_state.name = ['revolutejoint', 'aimjoint'] 
        
        key = getKey()
        
        if key == 'w' :
        
            amove += stepmove
            
        elif key == 's' :
        
            amove -= stepmove
            
        elif key == 'a' :
        
            rmove += stepmove
            
        elif key == 'd' :
        
            rmove -= stepmove
           
        else:
            if (key == '\x03'):
                break
        
        joint_state.position = [rmove, amove]
        
        puba.publish(amove)
        pubb.publish(rmove)
       
        rate.sleep()

if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
        
    try:
        change_joint_state()
    except rospy.ROSInterruptException:
        pass
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

