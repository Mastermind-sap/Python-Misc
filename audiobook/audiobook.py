import pyttsx3
book=open(r"book.txt") #input the location of text file you want to hear in the quotes
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
