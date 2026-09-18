import argparse,csv,time
from pathlib import Path
import cv2, mediapipe as mp
from gestura.features import normalize_landmarks

p=argparse.ArgumentParser()
p.add_argument("--label",required=True); p.add_argument("--samples",type=int,default=500)
p.add_argument("--output",default="data/raw/landmarks.csv"); a=p.parse_args()
out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
new=not out.exists(); cap=cv2.VideoCapture(0)
if not cap.isOpened(): raise RuntimeError("Webcam unavailable.")
api=mp.solutions.hands; count=0
with api.Hands(static_image_mode=False,max_num_hands=1,min_detection_confidence=.5,min_tracking_confidence=.5) as hands, out.open("a",newline="") as f:
    w=csv.writer(f)
    if new: w.writerow(["label"]+[f"f{i}" for i in range(63)])
    print("Collecting",a.label,"Press q to stop.")
    while count<a.samples:
        ok,frame=cap.read()
        if not ok: break
        frame=cv2.flip(frame,1); r=hands.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        if r.multi_hand_landmarks:
            x=normalize_landmarks(r.multi_hand_landmarks[0].landmark); w.writerow([a.label]+x.tolist()); count+=1
        cv2.putText(frame,f"{a.label}: {count}/{a.samples}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow("Gestura Dataset Collector",frame)
        if cv2.waitKey(1)&0xFF==ord("q"): break
        time.sleep(.01)
cap.release(); cv2.destroyAllWindows()
print("Saved",count,"samples to",out)
