import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import smtplib
import pyaudio
from time import sleep
import time


MASTER = "Master"
def engine(userinput):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(userinput)
    engine.runAndWait()

def engineer(Userinput):
    engineer = pyttsx3.init('sapi5')
    voices1 = engineer.getProperty('voices')
    engineer.setProperty('voice', voices1[1].id)
    engineer.say(Userinput)
    engineer.runAndWait()

def UserTalk(userinput):
    engine(userinput)
def AlexaTalk(Userinput):
    engineer(Userinput)


def takemastercomand():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Lisiting......!!")
        audio = r.listen(Source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio)
            print(f"User said : {query}\n")

        except Exception as error:
            print("Please say that again")
            query = None
    return query

UserTalk("Alexa tell my infinity to set a vacation.....")
AlexaTalk("What date is your vacation starts")
UserTalk("11th may")
AlexaTalk("What time does your vacation starts")
UserTalk("6 AM")
AlexaTalk("What date your vacation end")
UserTalk("13th May")
AlexaTalk("What time does your vacation end")
UserTalk("8 AM")
AlexaTalk("What do you want minimum temperature")
UserTalk("60 Degrees")
AlexaTalk("What do you want Maximum temperature")
UserTalk("65 Degrees")
AlexaTalk("What fan speed do you want to Use")
UserTalk("Medium")
time.sleep(3)

AlexaTalk("Vacation Added successfully")