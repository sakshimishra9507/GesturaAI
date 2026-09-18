import numpy as np

def normalize_landmarks(landmarks):
    points = np.array([[p.x,p.y,p.z] for p in landmarks], dtype=np.float32)
    points -= points[0]
    scale = np.max(np.linalg.norm(points[:,:2], axis=1))
    if scale < 1e-6: scale = 1.0
    return (points / scale).flatten()
