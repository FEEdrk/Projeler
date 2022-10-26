from turtle import delay
from pip import main
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser

r = sr.Recognizer()



def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en-EN")
        except sr.UnknownValueError:
            print("Assistant: Excuse me I don't understand you")
            #speak("I am waiting for youu sir")
        except sr.RequestError:
            print("Assistant: System is not working")
        return voice 


def speak(string):
    tts = gTTS(text=string, lang="en", slow=False)
    file= "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)




def response(voice):

    if "hello" in voice:
        speak("Hello")

    if "how are you" in voice:
        speak("I am fine. Thanks")

    if "lunch" in voice or "food" in voice:
        speak("I am opening food list")
        time.sleep(1)
        webbrowser.get().open("https://www.ikcu.edu.tr/yemeklistesi")
        time.sleep(1)
        speak("There is food list. What else can i do for you? ")

    if "thank you" in voice or "thanks" in voice:
        speak("I am here for realizing this!")

    if "hungry" in voice:
        webbrowser.get().open("https://sks.ikcu.edu.tr/Share/8E45AC6AD3CD2DAA1FC8DEF079DFEBB1")
        speak("This is food list of march, anything else")

    if "see you later" in voice:
        speak("I will waiting for you!")
        main
        

    if "close" in voice:
        speak("System closing.!")
        exit() #shutdown assistant

    if "what day" in voice:
        today = time.strftime("%A")
        speak(today)

    if "what time" in voice or "clock" in voice:
        selection =["it is:","my clock shows: ","the time is: ","i am looking now:  it's: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection+clock)

    if "note" in voice:
        speak("You need to name notefile, what is the filename")
        txtFile = record() + ".txt"
        speak("I'm listening!")
        theText = record()
        f = open(txtFile,"w",encoding="utf-8")
        f.writelines(theText)
        f.close()
        speak("I finished noting!")
            
    if "google" in voice:
        speak("What are we looking for on google?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("I am listing for {} on Google.".format(search))






speak("Voice Assistant Activating.")

time.sleep(1)
speak("What can i do for you") 





while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)


