import argparse
from pathlib import Path
import pandas as pd, joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix

p=argparse.ArgumentParser(); p.add_argument("--data",default="data/raw/landmarks.csv"); p.add_argument("--output",default="models/gesture_model.joblib"); a=p.parse_args()
df=pd.read_csv(a.data)
if "label" not in df or len(df)<20: raise ValueError("Dataset missing or too small.")
X=df.drop(columns=["label"]); y=df["label"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
pipe=Pipeline([("scaler",StandardScaler()),("classifier",RandomForestClassifier(n_estimators=300,random_state=42,class_weight="balanced"))])
pipe.fit(Xtr,ytr); pred=pipe.predict(Xte)
print(classification_report(yte,pred)); print("Confusion matrix:\n",confusion_matrix(yte,pred))
out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); joblib.dump(pipe,out); print("Saved",out)
