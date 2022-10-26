from distutils.command.clean import clean
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from attr import asdict
import urllib3


from desig_code import Ui_MainWindow

import requests, json
import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html
from selenium import webdriver
from datetime import datetime
import webbrowser
import locale
import speech_recognition as sr
import time

from info_1 import Ui_info_1
from info_2 import Ui_Info_2
locale.setlocale(locale.LC_ALL, 'turkish')

from smtplib import SMTP

from turtle import delay
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser



from selenium.webdriver.firefox import firefox_profile

from second_page import Secondpage

from PyQt5 import QtCore, QtGui, QtWidgets



class main(QMainWindow):


    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()
        self.ui.lunch_button.clicked.connect(self.lunch_page)

        self.ui.send_mail_button.clicked.connect(self.send_mail)

        self.ui.syllabus_button.clicked.connect(self.syllabus_page)

        self.ui.assistant_button.clicked.connect(self.assis)

        
        self.secondp = Secondpage()


        self.ui.buylunch.clicked.connect(self.buylunch)

        self.ui.search.clicked.connect(self.info_faculty)
 












    def buylunch(self):
        
        
        webbrowser.open('https://akillikart.ikc.edu.tr/')
        




    def info_faculty(self):
        
        selected_index = self.ui.comboBox.currentIndex()

        if selected_index == 1:
            self.window = QMainWindow()
            self.ui = Ui_info_1()
            self.ui.setupUi(self.window)
            self.window.show()

        if selected_index == 2:
            self.window = QMainWindow()
            self.ui = Ui_Info_2()
            self.ui.setupUi(self.window)
            self.window.show()


        #if selected_index == 3:
        #    self.window = QMainWindow()
        #    self.ui = Ui_info_3()
        #    self.ui.setupUi(self.window)
         #   self.window.show()


        #if selected_index == 4:
        #    self.window = QMainWindow()
        #   self.ui = Ui_info_4()
        #    self.ui.setupUi(self.window)
        #    self.window.show()









    def lunch_page(self):
        self.ui.label_9.setText("     Food List Opening...")
        time.sleep(1)
        webbrowser.open('https://www.ikcu.edu.tr/yemeklistesi')
        time.sleep(2)
        self.ui.label_9.setText("")

    def send_mail(self):
        self.ui.label_9.setText("     Mail Sending...")

        try:
            subject = "test"
            message = "deneme"
            content = "subject: {0}\n\n".format(subject,message)

            my_username = "silkoreis11@gmail.com"
            my_password = "silkojinx11"

            sendTo = "furkanfeedarkemre@gmail.com"

            mail = SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(my_username,my_password)
            mail.sendmail(my_username, sendTo, content.encode("utf-8"))
            print("Mail sent")
            playsound("aa.mp3")
            
        except Exception as e:
            print("Mail can't sent\n{0}".format(e))
        
        time.sleep(2)
        self.ui.label_9.setText("")

    def syllabus_page(self):  
        self.ui.label_9.setText("Opening of Syllabus Page")
        time.sleep(1)
        webbrowser.open('https://muh.ikcu.edu.tr/Share/C1E8C9D1532A5E3A3DD269C0590D61CD')   
        time.sleep(2)
        self.ui.label_9.setText("")
        



    def assis(self): 
        
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

                #exit() #shutdown assistant

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
            
            else :
                break
        #import assistant
        

            










uygulama = QApplication([])
pencere = main()
pencere.show()
uygulama.exec()
