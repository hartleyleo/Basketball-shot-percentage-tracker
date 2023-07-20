import cv2
import numpy as np

captureObj = cv2.VideoCapture(0)

shotTotal = 0
successfulShots = 0
shotPercentage = 0
font = cv2.QT_FONT_NORMAL

while(True):
    
    ret, frame = captureObj.read()
    
    # SHOT TOTAL
    cv2.putText(frame,                  #image
                f'Score: {shotTotal}',  #text
                (0,18),                 #location
                font, 0.7,              #font & scale
                (255, 255, 255),        #color
                2, cv2.LINE_4           #thickness & lineType
                )
    
    # SUCCESSFUL SHOT TOTAL
    cv2.putText(frame,                                      #image
                f'Successful shots: {successfulShots}',     #text
                (0,45),                                     #location
                font, 0.7,                                  #font & scale
                (255, 255, 255),                            #color
                2, cv2.LINE_4                               #thickness & lineType
                )
    
    # SHOT PERCENTAGE
    cv2.putText(frame,                                      #image
                f'Shot precentage: {shotPercentage}',       #text
                (0,75),                                     #location
                font, 0.7,                                  #font & scale
                (255, 255, 255),                            #color
                2, cv2.LINE_4                               #thickness & lineType
                )
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
    
captureObj.release()
cv2.destroyAllWindows()