import os
from flask import Flask, render_template, jsonify, request
from gestura.database import init_db, save_prediction, recent_predictions
from gestura.model import GestureModel
from gestura.vision import GestureEngine

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "change-me")
init_db()
model = GestureModel(os.getenv("MODEL_PATH", "models/gesture_model.joblib"))
engine = GestureEngine(model)

@app.get("/")
def index(): return render_template("index.html")

@app.get("/history")
def history(): return render_template("history.html", records=recent_predictions(100))

@app.get("/api/health")
def health(): return jsonify(status="ok", model_loaded=model.loaded)

@app.post("/api/prediction")
def prediction():
    p = request.get_json(silent=True) or {}
    save_prediction(str(p.get("label","unknown")), float(p.get("confidence",0)))
    return jsonify(saved=True)

@app.get("/video_feed")
def video_feed(): return engine.stream()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
