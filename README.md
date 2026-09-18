# Gestura AI
## An Intelligent Real-Time Hand Gesture Recognition and Human–Computer Interaction System Using Artificial Intelligence and Computer Vision

Gestura AI is a Python AI/ML project that detects hand landmarks from a webcam, classifies gestures, displays confidence, stores recognition history, and provides a foundation for gesture-to-text/speech and safe computer-control features.

### Stack
Python 3.10+, OpenCV, MediaPipe, NumPy, scikit-learn, Joblib, Flask, SQLite, pyttsx3.

### Pipeline
Camera -> MediaPipe Hand Landmarks -> Normalized Features -> ML Classifier -> Gesture/Confidence -> Dashboard/History/Optional Actions

### Starter gesture classes
`open_palm`, `fist`, `thumbs_up`, `thumbs_down`, `peace`, `ok`, `point`, `rock`, `call_me`, `stop`

### Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

### Train
```bash
python scripts/collect_data.py --label thumbs_up --samples 500
python scripts/train_model.py
```
Repeat collection for each class. The model is saved to `models/gesture_model.joblib`.

### Academic evaluation
Report dataset size, class balance, accuracy, precision, recall, F1, confusion matrix, FPS, latency and cross-user testing. Do not claim production accuracy until it has been measured on your own dataset.

### Safety
Computer-control actions are disabled by default. Do not map gestures to destructive or security-sensitive actions without authentication, confirmation, confidence thresholds, logging and an emergency disable switch.

See `ROADMAP.md` and `docs/` for the complete project plan.
