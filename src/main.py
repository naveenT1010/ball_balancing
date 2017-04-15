#!/usr/bin/env python

from __future__ import print_function
import cv2
import rospy
from geometry_msgs.msg import Point, Twist
import my_constants
import features.py

def cb(x):
	pass

def main():
	# pub = rospy.Publisher('angles', Twist, queue_size=10)
	rospy.init_node('feeder', anonymous=True)
	rospy.loginfo("Program has started!!")

	cap = cv2.VideoCapture(0)
	frame_h, frame_w = cap.get(3), cap.get(4)

	cv2.namedWindow("Direct Feed", cv2.WINDOW_NORMAL)
	cv2.namedWindow("Detected", cv2.WINDOW_NORMAL)
	cv2.namedWindow("Settings", cv2.WINDOW_NORMAL)

	cv2.createTrackbar("HUE L", "Settings", 0, 179, cb)
	cv2.createTrackbar("HUE H", "Settings", 179, 179, cb)
	cv2.createTrackbar("SAT L", "Settings", 0, 255, cb)
	cv2.createTrackbar("SAT H", "Settings", 255, 255, cb)
	cv2.createTrackbar("VAL L", "Settings", 0, 255, cb)
	cv2.createTrackbar("VAL H", "Settings", 255, 255, cb)

	while(cap.isOpened() and not rospy.is_shutdown()):
		check, frame = cap.read()

		if (check == False):
			rospy.logerr("Couldnt get feed from the camers. Exiting!")
			break
		elif(check == True):
			# Direct feed from camera
			cv2.imshow("Direct Feed", frame)

			# converting the rgb image into hsv color space
			hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

			# getting the values of HSV trackbars
			hsv_l = (cv2.getTrackbarPos("HUE L", "Settings"), cv2.getTrackbarPos("SAT L", "Settings"), cv2.getTrackbarPos("VAL L", "Settings"))
			hsv_h = (cv2.getTrackbarPos("HUE H", "Settings"), cv2.getTrackbarPos("SAT H", "Settings"), cv2.getTrackbarPos("VAL H", "Settings"))
			
			# creating a binary image using the HSV values
			mask = cv2.inRange(hsv_frame, hsv_l, hsv_h)

			cv2.imshow("Detected", mask)

			user_input_key = cv2.waitKey(1) & 0xFF

			if user_input_key == ord('b'):
				extract_feature(mask, "base")
			elif user_input_key == ord('f'):
				extract_feature(mask, "front")
			elif user_input_key == ord('q'):
				break

	rospy.loginfo("Program Completed.")
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()