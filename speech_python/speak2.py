import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="s1.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("hello")
