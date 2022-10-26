from distutils.command.clean import clean
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from attr import asdict
from matplotlib.pyplot import show
from pip import main
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

from entry_page import  Ui_entrymain
from second_page_donusturulmus import Ui_second_page
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
from desig_code import Ui_MainWindow
#from desig_code import 
from desig_code import Ui_MainWindow
#from main import *
#import main

class mainn(QMainWindow):


    def __init__(self):
        super().__init__()

        self.ui = Ui_entrymain()
        
        self.ui.setupUi(self)
        self.showFullScreen()
        self.ui.one.clicked.connect(self.pic_1)
        self.ui.two.clicked.connect(self.pic_2)
        self.ui.three.clicked.connect(self.pic_3)
        self.ui.four.clicked.connect(self.pic_4)
        
        self.ui.temp_button.clicked.connect(self.temp)
        self.ui.dumen.clicked.connect(self.dumen)
        #self.ui.send_mail_button.clicked.connect(self.send_mail)
        
        
    def temp(self):
        self.ui.temp_label.setText("Your Temperatures : 36.7 C")

    def pic_1(self):
        self.ui.label.setStyleSheet("border-image: url(:/resim/1.png);")
        
    def pic_2(self):
        self.ui.label.setStyleSheet("border-image: url(:/resim/2.png);")

    def pic_3(self):
        self.ui.label.setStyleSheet("border-image: url(:/resim/3.png);")

    def pic_4(self):
        self.ui.label.setStyleSheet("border-image: url(:/resim/4.png);")


    def dumen (self):
        import main
        super().__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        #main()
        #time(1)







    def lunch_page(self):
        self.ui.deneme_line.setText("     Food List Opening...")
        time.sleep(1)
        webbrowser.open('https://www.ikcu.edu.tr/yemeklistesi')
        time.sleep(10)
        self.ui.deneme_line.setText("")


    def send_mail(self):
        

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



    def syllabus_page(self):  
        self.ui.deneme_line.setText("Opening of Syllabus Page")
        time.sleep(1)
        webbrowser.open('https://muh.ikcu.edu.tr/Share/C1E8C9D1532A5E3A3DD269C0590D61CD')   
        time.sleep(1)
        self.ui.deneme_line.setText("")
















uygulama = QApplication([])
pencere = mainn()
pencere.show()
uygulama.exec()