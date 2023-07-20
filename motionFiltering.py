import cv2

captureObj = cv2.VideoCapture(0)
subtractorObj = cv2.createBackgroundSubtractorMOG2(20, 50)

while(True):
    
    ret, frame = captureObj.read()
    
    if ret:
        changeFrame = subtractorObj.apply(frame)
        cv2.imshow('ChangeFrame', changeFrame)
    
    if cv2.waitKey(5) == ord('q'):
        break
    
captureObj.release()
cv2.destroyAllWindows()