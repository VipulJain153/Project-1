import mediapipe as mp
import cv2

mp_hands =mp.solutions.hands
mpHands = mp_hands.Hands()
mp_pose =mp.solutions.pose
mpPose = mp_pose.Pose()
mp_face =mp.solutions.face_detection
mpface = mp_face.FaceDetection(0.71,1)
mp_mesh =mp.solutions.face_mesh
mpMesh = mp_mesh.FaceMesh(max_num_faces=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(5, 80)
cap.set(10, 0)

drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=1,color=(0,255,0))
Spec = mpDraw.DrawingSpec(thickness=1,color=(0,255,0))

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    results = mpHands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for i in results.multi_hand_landmarks:
            for j in i.landmark:
                pass
            for k in results.multi_handedness:
                print(k.classification[0].label)
            mpDraw.draw_landmarks(img,i,mp_hands.HAND_CONNECTIONS,mpDraw.DrawingSpec(color=(205, 39, 95),thickness=4,circle_radius=4),mpDraw.DrawingSpec(color=(205, 39, 95)))
    results = mpPose.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if results.pose_landmarks:
            for j in results.pose_landmarks.landmark:
                pass
            mpDraw.draw_landmarks(img,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,mpDraw.DrawingSpec(color=(87, 202, 254),thickness=4,circle_radius=4),mpDraw.DrawingSpec(color=(87, 202, 254)))
    results = mpface.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if results.detections:
         for i in results.detections:
              print(i.location_data.relative_bounding_box)
              print(i.score)
              mpDraw.draw_detection(img,i,mpDraw.DrawingSpec(thickness=4,circle_radius=4,color=(251, 219, 72)),mpDraw.DrawingSpec(color=(251, 219, 72),thickness=6))
    results = mpMesh.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if results.multi_face_landmarks:
        for i in results.multi_face_landmarks:
            for j in i.landmark:
                pass
            mpDraw.draw_landmarks(img,i,mp_mesh.FACEMESH_CONTOURS,mpDraw.DrawingSpec(color=(211, 210, 0),thickness=4,circle_radius=4),mpDraw.DrawingSpec(color=(211, 210, 0)))
            mpDraw.draw_landmarks(img,i,mp_mesh.FACEMESH_TESSELATION,drawSpec,Spec)
    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
