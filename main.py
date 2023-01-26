from pocketsphinx import LiveSpeech
from recorder import Recorder
import speech_recognition as sr 
import os
from colorama import Fore
import struct
import pyaudio
import pvporcupine
import playsound
import threading
import data.commands as commands
import data.voice as voice

r = sr.Recognizer()
mic = sr.Microphone()
engine = voice.init()

def startupSound():
    playsound.playsound("./data/audio/startup.mp3")

def listening():
    playsound.playsound("./data/audio/listen.wav")

def stoppedListening():
    playsound.playsound("./data/audio/nolisten.wav")

with mic as source:
    r.adjust_for_ambient_noise(mic, duration=4)

threading.Thread(target=startupSound).start()
print("Keyword: computer")
try:
    porcupine = pvporcupine.create(access_key='M2qfpLrds0YOzDwINJ48Ehfy0ndLOKk8BL0UCCIuDPHS3rNd5hOatA==',keywords=["computer"])
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length)
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            with mic as source:
                threading.Thread(target=listening).start()
                audio = r.listen(source, timeout=10, phrase_time_limit=5)
                try:
                    data = r.recognize_google(audio)
                    if commands.checkCommands(engine, data) == False:
                        continue
                except sr.UnknownValueError:
                    threading.Thread(target=stoppedListening).start()
                except sr.RequestError as e:
                    print("Google error; {0}".format(e))
finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if pa is not None:
        pa.terminate()

