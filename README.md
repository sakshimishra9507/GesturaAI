# Gestura AI

## An Intelligent Real-Time Hand Gesture Recognition and Human–Computer Interaction System Using Artificial Intelligence and Computer Vision

Gestura AI is a Python-based computer vision and machine learning project that detects hand landmarks from a webcam, classifies gestures in real time, displays confidence scores, stores recognition history, and provides a foundation for gesture-driven text input and human–computer interaction.

### Stack
- Python 3.10+
- OpenCV
- MediaPipe
- NumPy
- scikit-learn
- Joblib
- Flask
- SQLite
- pyttsx3

### Pipeline
Camera -> MediaPipe hand landmarks -> normalized feature extraction -> machine learning classifier -> predicted gesture/confidence -> dashboard/history/optional actions

### Starter gesture classes
`open_palm`, `fist`, `thumbs_up`, `thumbs_down`, `peace`, `ok`, `point`, `rock`, `call_me`, `stop`

### Features
- Real-time webcam gesture recognition
- Landmark-based feature extraction
- Training pipeline for custom gestures
- Flask web dashboard for live recognition and history
- SQLite-backed history storage
- Optional text-to-speech feedback via `pyttsx3`
- Safe default behavior with no destructive actions enabled by default

### Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

### Train custom gesture data
```bash
python collect_data.py --label thumbs_up --samples 500
python train_model.py
```

Repeat the data collection step for each gesture class you want the model to learn. The trained model is saved to `models/gesture_model.joblib`.

### Project structure
```text
GesturaAI/
├── app.py                  # Flask app and dashboard
├── actions.py              # Gesture action helpers
├── collect_data.py         # Data collection utility for label creation
├── train_model.py          # Model training pipeline
├── model.py                # Model loading and inference helpers
├── vision.py               # Camera and MediaPipe processing
├── features.py             # Feature extraction utilities
├── database.py             # SQLite database interactions
├── speech.py               # Text-to-speech wrapper
├── base.html               # Base HTML template
├── index.html              # UI entry point
├── history.html            # Gesture history page
├── style.css               # Front-end styling
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── *.md                    # Project documentation and specifications
└── tests                   # Project tests (if added in future)
```

### Academic evaluation guidance
Report dataset size, class balance, accuracy, precision, recall, F1 score, confusion matrix, FPS, latency, and cross-user testing. Do not claim production-grade accuracy until measurements are collected on your own dataset and usage conditions.

### Safety
Computer-control actions are disabled by default. Do not map gestures to destructive or security-sensitive actions without authentication, confirmation, confidence thresholds, logging, and explicit user consent.

### Documentation index
- `PROJECT_OVERVIEW.md` — high-level overview of the system
- `AI_ML_METHODOLOGY.md` — AI/ML methodology and model design
- `API.md` — API overview and endpoints
- `DATABASE.md` — data storage design and schema
- `SRS.md` — software requirements specification
- `ROADMAP.md` — project roadmap and milestones
- `DEPLOYMENT.md` — deployment notes
- `TESTING.md` — validation and testing guidance
- `CONTRIBUTING.md` — contribution workflow
- `SECURITY.md` — vulnerability reporting
- `SECURITY_PRIVACY.md` — privacy and security notes
- `FILE_INDEX.md` — repository file inventory
- `DEMO_SCRIPT.md` — demo walkthrough
- `FINAL_YEAR_REPORT_OUTLINE.md` — academic report structure
- `FUTURE_SCOPE.md` — future directions

### Related documentation
See `ROADMAP.md` and the project documentation files above for the complete development plan, design notes, and implementation background.
