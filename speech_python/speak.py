from gtts import gTTS
import os    

tts = gTTS(text="This is the pc speaking", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")
