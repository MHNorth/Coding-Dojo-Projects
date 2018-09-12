import numpy as np
import cv2
import matplotlib.pyplot as plt

capture_img = cv2.VideoCapture(0)
print(capture_img)

while(True):
    # Capture frame-by-frame
    ret, frame = capture_img.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
capture_img.release()
cv2.destroyAllWindows()