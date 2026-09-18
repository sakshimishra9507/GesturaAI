import cv2, mediapipe as mp
from flask import Response
from .features import normalize_landmarks

class GestureEngine:
    def __init__(self, model):
        self.model=model
        self.mp_hands=mp.solutions.hands
        self.mp_draw=mp.solutions.drawing_utils

    def frames(self):
        cap=cv2.VideoCapture(0)
        if not cap.isOpened(): raise RuntimeError("Could not open webcam.")
        with self.mp_hands.Hands(static_image_mode=False,max_num_hands=1,
            min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
            while True:
                ok,frame=cap.read()
                if not ok: break
                frame=cv2.flip(frame,1)
                result=hands.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
                label,conf="no_hand",0.0
                if result.multi_hand_landmarks:
                    hand=result.multi_hand_landmarks[0]
                    label,conf=self.model.predict(normalize_landmarks(hand.landmark))
                    self.mp_draw.draw_landmarks(frame,hand,self.mp_hands.HAND_CONNECTIONS)
                cv2.putText(frame,f"{label} | {conf:.1%}",(20,45),
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                ok,b=cv2.imencode(".jpg",frame)
                if ok: yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n"+b.tobytes()+b"\r\n"
        cap.release()

    def stream(self):
        return Response(self.frames(),mimetype="multipart/x-mixed-replace; boundary=frame")
