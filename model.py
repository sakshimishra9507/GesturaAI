from pathlib import Path
import joblib, numpy as np

class GestureModel:
    def __init__(self, path):
        self.path=Path(path); self.pipeline=None; self.loaded=False
        if self.path.exists():
            try:
                self.pipeline=joblib.load(self.path); self.loaded=True
            except Exception: pass

    def predict(self, features):
        if not self.loaded: return "model_not_trained", 0.0
        probs=self.pipeline.predict_proba([features])[0]
        i=int(np.argmax(probs))
        return str(self.pipeline.classes_[i]), float(probs[i])
