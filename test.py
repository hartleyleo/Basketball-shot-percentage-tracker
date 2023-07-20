import cv2

img = cv2.VideoCapture(0)

# variables
ix = -1
iy = -1
drawing = False

def draw_rectangle_with_drag(event, x, y, flags, param):

    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y            

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", draw_rectangle_with_drag)

while True:
    
    ret, frame = img.read()
    
    cv2.imshow("Title of Popup Window", frame)
    
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()