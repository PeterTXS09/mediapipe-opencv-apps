import cv2

video = cv2.VideoCapture('video.mp4')

while True:
    check, img = video.read()
    imgRz = cv2.resize(img, (720, 360))
    cv2.imshow('Video UPCH', imgRz)
    cv2.waitKey(20)