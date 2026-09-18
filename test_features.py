from types import SimpleNamespace
from gestura.features import normalize_landmarks

def test_feature_length():
    pts=[SimpleNamespace(x=.1*i,y=.2*i,z=.01*i) for i in range(21)]
    assert len(normalize_landmarks(pts))==63
