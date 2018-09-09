from django.shortcuts import render
import numpy as np
import urllib
import json
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

##---------- Face Detection Views ----------##

 # define the path to the face detector
face_detector_path = "C:/Users/MNorthrop/codingDojo/Coding-Dojo-Projects/DjangoProjects/face_recognition_project/cascades/haarcascade_frontalface_default.xml"
 
@csrf_exempt
def requested_url(request):  #This is our actual view

	# initialize the data dictionary to be returned by the request
	default = {"success": False}  #Because there is no detection yet
 
	# check to see if this is a post request and check for https
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image_to_read = read_image(stream=request.FILES["image"])
 
		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url_provided = request.POST.get("url", None)
 
			# if the URL is None, then return an error
			if url_provided is None:
				default["error_value"] = "There is no URL provided."

				return JsonResponse(default)

### START WRAPPING OF COMPUTER VISION APP
# Insert code here to process the image and update
# the `data` dictionary with your results
### END WRAPPING OF COMPUTER VISION APP
 
			# load the image and convert
			image_to_read = read_image(url=url_provided)
 
		# convert the image to grayscale, load the face cascade detector,
		# and detect faces in the image
		image_to_read = cv2.cvtColor(image_to_read, cv2.COLOR_BGR2GRAY)
		detector_value = cv2.CascadeClassifier(face_detector_path)
		values = detector_value.detectMultiScale(image_to_read, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
 
		# construct a list of bounding boxes from the detection
		values = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in values]
 
		# update the data dictionary with the faces detected
		default.update({"num_faces": len(values), "faces": values, "success": True})
 
	# return a JSON response
	return JsonResponse(default)
 
 # Function that reads an image from our disk, URL or stream into OpenCV format.
def read_image(path=None, stream=None, url=None):
    #### primarily URL #####
	# but if the path is not None, then load the image from your local repository
	if path is not None:
		image = cv2.imread(path)
 
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			response = urllib.request.urlopen(url)
			data_temp = response.read()
 
		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data_temp = stream.read()
 
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data_temp), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image