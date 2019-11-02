# camera_info_publisher

## Requirements
- ROS kinetic or melodic

## Usage
```
cd YOUR_ROS_WS
git clone https://github.com/amslabtech/camera_info_publisher 
catkin build
source devel/setup.bash
roslaunch camera_info_publisher camera_info_publisher.launch
```

## Node
### camera_info_publisher
- Subscribed topic
  - /camera_info (sensor_msgs/CanmeraInfo)
