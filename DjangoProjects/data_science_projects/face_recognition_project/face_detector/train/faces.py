import numpy as np
import cv2
import pickle
import matplotlib.pyplot as plt

#find location of cv2 library package, open shell, import cv2, print(cv2.__file__)
cascade_path_face = "C:/Users/MNorthrop/Anaconda3/envs/MyDjangoEnv/lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
cascade_path_eye = "C:/Users/MNorthrop/Anaconda3/envs/MyDjangoEnv/lib/site-packages/cv2/data/haarcascade_eye.xml"
cascade_path_smile = "C:/Users/MNorthrop/Anaconda3/envs/MyDjangoEnv/lib/site-packages/cv2/data/haarcascade_smile.xml"

face_cascade = cv2.CascadeClassifier(cascade_path_face)  #Capture front of face in image
eye_cascade = cv2.CascadeClassifier(cascade_path_eye)  #Capture eye region of face in image
smile_cascade = cv2.CascadeClassifier(cascade_path_smile) #Capture smile of face in image

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.read("./recognizors/face-trainner.yml")

labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
    	#print(x,y,w,h)
    	roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
    	roi_color = frame[y:y+h, x:x+w]

    	# recognize? deep learned model predict keras tensorflow pytorch scikit learn
    	id_, conf = recognizer.predict(roi_gray)
    	if conf>=4 and conf <= 85:
    		#print(5: #id_)
    		#print(labels[id_])
    		font = cv2.FONT_HERSHEY_SIMPLEX
    		name = labels[id_]
    		color = (255, 255, 255)
    		stroke = 2
    		cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

    	img_item = "7.png"
    	cv2.imwrite(img_item, roi_color)

    	color = (255, 0, 0) #BGR 0-255 
    	stroke = 2
    	end_cord_x = x + w
    	end_cord_y = y + h
    	cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    	#subitems = smile_cascade.detectMultiScale(roi_gray)
    	#for (ex,ey,ew,eh) in subitems:
    	#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # Display the resulting frame
    plt.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#find location of cv2 library package, open shell, import cv2, print(cv2.__file__)
# cascade_path = "C:/Users/MNorthrop/Anaconda3/envs/MyDjangoEnv/lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
# face_cascade = cv2.CascadeClassifier(cascade_path)  #Capture front of face in image
# video_capture = cv2.VideoCapture(0)

#Build Classifier

# while(True):
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(
#         gray, 
#         scaleFactor=1.5, 
#         minNeighbors=5,
#         )

#     for (x,y,w,h) in faces:

#         print(x,y,w,h)
#         # Draw region of interest
#         roi_gray = gray[y:y+h, x:x+w]  #shows (y_coordinate_start, y_coordinate_end)
#         roi_color = frame[y:y+h, x:x+w]
#         img_item = "my_image.png"
#         cv2.imwrite(img_item, roi_color)

#         #draw a rectangle
#         color = (255, 0, 0)  #BGR 0 - 255
#         stroke = 2  # defines line thickness
#         end_coord_x = x + w
#         end_cord_y = y + h
#         cv2.rectangle(frame, (x,y), (end_coord_x, end_cord_y), color, stroke)  #draws on the frame with start/end coordinates x and y then define color & thickness of frame

#     # Display the resulting frame
#     cv2.imshow('frame', frame)

#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# # When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()


##--------------------------------------------------------------------------------------------------###

# #2. Create a frame object
# check, frame = cam.read()

# print(check)
# print(frame)  #Prints live matrix of image

# #3.  Show the Frame!
# cv2.imshow('Capturing', frame)

# #4 Press any key to exit
# cv2.waitKey(0)

# #2. Shutdown the camera
# cam.release()