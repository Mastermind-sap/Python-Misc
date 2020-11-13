import speech_recognition as sr
import pyaudio
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("speak now")
        audio = r3.listen(source)
        print (r2.recognize_sphinx(audio))
