import cv2, requests


# define the URL to our face detection API
url="http://localhost:8000/face_detection/detect/"
# headers={'User-Agent': 'Definitely-Not-Requests'} 
# r = requests.get(url, headers)

##--------------Image 1---------------##

## IMAGE TO READ is the variable taking into account the directory where the image file is stored.
## GIVE THE FULL PATH

# use our face detection API to find faces in images via image URL
image_to_read = cv2.imread("C:/Users/MNorthrop/codingDojo/Coding-Dojo-Projects/DjangoProjects/face_detection_project/face_detection_project/media/image5.jpg")
tracker = {"url": "https://image.ibb.co/cPrdgS/image5.jpg"}
req = requests.post(url, data=tracker).json()
print("image5.jpg: {}".format(req))

# loop over the faces and draw them on the image
for (w,x,y,z) in req["faces"]:
    cv2.rectangle(image_to_read, (w,x), (y,z), (0, 255, 0), 2)

# show the output image
cv2.imshow("image5.jpg", image_to_read)
cv2.waitKey(0)




## USE THE cURL script to return details about the number of faces the program API detected from the image, 
## including their sizes

### DEPLOYING THE CURL SCRIPT ###
## On the CLI enter the following command to test our API: 
## curl -X POST "http://localhost:8000/face_detection/detect/"-d "url=https://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg";echo""
## curl -X POST "http://localhost:8000/face_detection/detect/"-d url="https://image.ibb.co/cPrdgS/image5.jpg";echo""
