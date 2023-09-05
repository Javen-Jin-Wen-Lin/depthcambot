#!/usr/bin/env python 3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

def callback(data):
    # Process the data from the topic
    # Extract point cloud data from the PointCloud2 message
    pc_data = pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=True)

    # Access and manipulate the point cloud data as needed
    for i, point in enumerate(pc_data, start=1):
        x, y, z = point
        print(f"Point {i}: x = {x}, y = {y}, z = {z}")
        # Do something with x, y, z values

def listener():
    rospy.init_node('depth_points_listener', anonymous=True)
    rospy.Subscriber("/my_camera/depth/points", PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

