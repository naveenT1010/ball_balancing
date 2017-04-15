def extract_feature(image, feature_type):
	contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	area = cv2.contourArea(contour[-1])
	if area > 300:
		moment = cv2.moments(contour[-1])
		if feature_type is "base":
			BASE_CENTROID.x = int(moments['m10']/moments['m00'])
			BASE_CENTROID.y = int(moments['m01']/moments['m00'])
		elif feature_type is "front":
			BALL_CENTROID.x = int(moments['m10']/moments['m00'])
			BALL_CENTROID.y = int(moments['m01']/moments['m00'])