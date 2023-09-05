cmake_minimum_required(VERSION 2.8.3)
project(archerfish_control)
find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  gazebo_msgs
  std_msgs
)

catkin_python_setup()

catkin_package(
CATKIN_DEPENDS rospy geometry_msgs gazebo_msgs std_msgs
)
include_directories()

catkin_install_python(PROGRAMS
  nodes/archerfish_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
