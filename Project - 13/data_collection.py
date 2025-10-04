import cv2
import numpy as np
import pandas as pd
import os
arr1 = []
arr2 = []
arr3 = []
# cap = cv2.VideoCapture(0)
# imgType = "sad"
# count =0 

# while True:
#     success, img = cap.read()
#     cv2.imshow('Image', img)
#     key= cv2.waitKey(1) 
#     if key == ord('q'):
#         break
#     elif key == ord('s'):
#         cv2.imwrite(f'data/{imgType}{count}.png',img)
#         count+=1
l1 = list(filter(lambda x:x.startswith("smile"),os.listdir("data")))
for x in l1:
    # arr1.append(cv2.imread(f'data/{x}'))
    img=cv2.imread(f'data/{x}')
    break
# df1 =pd.DataFrame(arr1,columns=["data"])
# df1["label"] = "Smile"

# l2 = list(filter(lambda x:x.startswith("sad"),os.listdir("data")))
# for x in l2:
#     arr2.append(cv2.imread(f'data/{x}'))
# df2=pd.DataFrame(arr2,columns=["data"])
# df2["label"] = "Sad"

# l3 = list(filter(lambda x:x.startswith("neutral"),os.listdir("data")))
# for x in l3:
#     arr3.append(cv2.imread(f'data/{x}'))
# df3 =pd.DataFrame(arr3,columns=["data"])
# df3["label"] = "Neutral"

# pd.concat([df1,df2,df3]).to_csv("data.csv")
