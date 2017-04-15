#!/usr/bin/env python

from __future__ import print_function
import cv2
import rospy
from geometry_msgs.msg import Twist

def main():
	# pub = rospy.Publisher('angles', Twist, queue_size=10)
	rospy.init_node('feeder', anonymous=True)
	rospy.loginfo("Program has started!!")

	cap = cv2.VideoCapture(0)

	while(cap.isOpened() and not rospy.is_shutdown()):
		check, frame = cap.read()

		if (check == False):
			rospy.logerr("Couldnt get feed from the camers. Exiting!")
			break
		elif(check == True):
			cv2.imshow("Direct Feed", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	rospy.loginfo("Program Completed.")
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()