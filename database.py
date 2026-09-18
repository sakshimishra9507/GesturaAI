import os, sqlite3
from pathlib import Path
from datetime import datetime
DB=Path(os.getenv("DATABASE_PATH","data/gestura.db"))

def _connect():
    DB.parent.mkdir(parents=True,exist_ok=True); return sqlite3.connect(DB)

def init_db():
    with _connect() as c:
        c.execute('CREATE TABLE IF NOT EXISTS predictions (id INTEGER PRIMARY KEY AUTOINCREMENT,label TEXT NOT NULL,confidence REAL NOT NULL,created_at TEXT NOT NULL)')

def save_prediction(label,confidence):
    with _connect() as c:
        c.execute('INSERT INTO predictions(label,confidence,created_at) VALUES (?,?,?)',(label,confidence,datetime.utcnow().isoformat()))

def recent_predictions(limit=100):
    with _connect() as c:
        c.row_factory=sqlite3.Row
        return [dict(r) for r in c.execute('SELECT * FROM predictions ORDER BY id DESC LIMIT ?',(limit,)).fetchall()]
