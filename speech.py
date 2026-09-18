import pyttsx3
_engine=None
def speak(text):
    global _engine
    if _engine is None: _engine=pyttsx3.init()
    _engine.say(text); _engine.runAndWait()
