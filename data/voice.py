import pyttsx3

def init():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    return engine

def say(engine, text):
    engine.say(text)
    engine.runAndWait()
