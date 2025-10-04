from ultralytics import YOLO
import cv2,math
model = YOLO("YOLO-Weights/yolov8l.pt")
from cvzone import FPS,cornerRect,putTextRect
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(5,100)
FPS=FPS()

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
while True:
    _,img = cap.read()
    results = model(img,stream=True)
    for i in results:
        boxes = i.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            bbox=x1,y1,x2-x1,y2-y1
            cornerRect(img,bbox)
            # className 
            cls = int(box.cls[0])
            # Confidence
            conf = math.ceil(box.conf[0]*100)/100
            confStr = "{} {}".format(classNames[cls],conf) # Showing the Confidence
            putTextRect(img,confStr,(max(0,x1),max(35,y1)))
    FPS.update(img,color=(0,0,255))
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break