import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
webcam=cv2.VideoCapture(0)
video=VideoWriter('video.avi',VideoWriter_fourcc(*'MP42'),25.0,(640,480))
while True:
    stream_ok, frame=webcam.read()    
    if stream_ok:
        cv2.imshow('webcam',frame)
        video.write(frame)
    if cv2.waitKey(1) & 0xFF==27: break
cv2.destroyAllWindows()
webcam.release() 
video.release()
    
