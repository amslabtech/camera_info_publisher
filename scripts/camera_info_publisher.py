#!/usr/bin/env python
import rospy
import yaml
from sensor_msgs.msg import CameraInfo
import sys

def CameraInfo_Loader(file_name):
    
    #with open(file_name, "r") as f:
    #    calib_data = yaml.load(f)
    try:
        with open(file_name, "r") as f:
            calib_data = yaml.load(f)
            msg = CameraInfo()
            msg.width = calib_data["image_width"]
            msg.height = calib_data["image_height"]
            msg.K = calib_data["camera_matrix"]["data"]
            msg.D = calib_data["distortion_coefficients"]["data"]
            msg.R = calib_data["rectification_matrix"]["data"]
            msg.P = calib_data["projection_matrix"]["data"]
            msg.distortion_model = calib_data["distortion_model"]
            
        return msg
    
    except IOError:
        print("##########ERROR!!!##########")
        print("Can't open "+file_name)
        print("############################")
        rospy.signal_shutdown("file_open_error")

    #msg = CameraInfo()
    #msg.width = calib_data["image_width"]
    #msg.height = calib_data["image_height"]
    #msg.K = calib_data["camera_matrix"]["data"]
    #msg.D = calib_data["distortion_coefficients"]["data"]
    #msg.R = calib_data["rectification_matrix"]["data"]
    #msg.P = calib_data["projection_matrix"]["data"]
    #msg.distortion_model = calib_data["distortion_model"]
    
    #return msg

if __name__ == "__main__":
    
    rospy.init_node("camera_info_publisher", anonymous=True)
    
    if rospy.has_param('~FILE_NAME'):
        file_name = rospy.get_param('~FILE_NAME')
    
    if rospy.has_param('~FRAME_ID'):
        frame_id = rospy.get_param('~FRAME_ID')

    camera_info = CameraInfo_Loader(file_name)

    camera_info_publisher = rospy.Publisher("/camera_info", CameraInfo, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        camera_info.header.frame_id  = frame_id
        camera_info.header.stamp = rospy.Time.now()
        camera_info_publisher.publish(camera_info)
        rate.sleep()
