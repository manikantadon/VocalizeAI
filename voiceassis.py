import speech_recognition as sr #importing speech recognizing module
import pyttsx3 # Text-to-speech conversion library
import pywhatkit  # Library for various automation tasks with web services
import datetime # Module for working with dates and times
import wikipedia  # Library for querying Wikipedia articles
import requests # Library for making HTTP requests
import json # Module for working with JSON data
import webbrowser # Module for opening web browsers
import os # Module for interacting with the operating system
import smtplib # Library for sending emails using SMTP
import cv2 # OpenCV library for computer vision tasks
import time as t # Module for time-related functions
import pyautogui # Library for GUI automation and taking screenshots
import tkinter as tk # Tkinter library for GUI development
from tkinter.filedialog import * # Module for working with file dialogs
import speech_recognition as sr # Speech recognition library

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
import cv2 # OpenCV library for computer vision tasks
import time # Module for time-related functions

def take_ss():
    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename(defaultextension=".png")
    if save_path:
        screen_shot.save(save_path)
        return save_path
    
def speak(speech):
    engine.say(speech)
    engine.runAndWait()
def listen():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 4000  # Adjust this value to set the microphone sensitivity
            listener.pause_threshold = 1  # Adjust this value to set the pause duration for speech recognition
            listener.dynamic_energy_adjustment_ratio = 1.5  # Adjust this value to dynamically adjust the energy threshold
            listener.dynamic_energy_adjustment_damping = 0.15 
            print("listening...")
            voice = listener.listen(source,timeout=1.5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command
"""def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    webbrowser.open("gmail.com")
    server.starttls()
    server.sendmail('dongala565@gmail.com',to,content)
    server.close()"""
def run_vass():
    comma = listen()
    if 'play' in comma:#(1)plays song from youtube.........................
        song = comma.replace('play','')
        speak("playing "+song)
        pywhatkit.playonyt(song)
    elif 'time' in comma: #(2)can tell time (current time).................
        time=datetime.datetime.now().strftime('%H:%M %p')
        print(f'the current time is {time}')
        speak(f'the current time is {time}')
    elif 'wikipedia' in comma or 'who' in comma:#(3)searches on wikipedia..
        info = wikipedia.summary(comma,sentences=1)
        print(info)
        speak(info)
    elif 'how are you' in comma:#(4)wishes and queries.....................
        print("I am fine! how about you?")
        speak(" I am fine..")
        speak("How about you..?")
    elif 'send whatsapp message' in comma:#(5)sends whatsapp message.......
        pywhatkit.sendwhatmsg('+919948182114','hi nanna',11,24)
    elif 'repeat me' in comma:#(6)repeats what user says...................
        print('ok say something')
        speak('ok say something!')
        sentence_to_be_repeted=listen()
        print(sentence_to_be_repeted)
        speak(sentence_to_be_repeted)
    elif 'news' in comma:#(7)explains todays news reports..................
        print("reading news!")
        speak("headlines!")
        comma=comma.replace("news","")
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=11586a9e95384772821c75bd5a223382"
        news = requests.get(url).text
        news = json.loads(news)
        art = news['articles']
        c=0
        for article in art:
            print(article['title'])
            speak(article['title'])
            print(article['description'])
            speak(article['description'])
            c+=1
            if c>3:
                break
    elif 'open google' in comma:#(8)opens google...........................
        webbrowser.open("google.com")
        speak("google opened!")
        
    elif 'open youtube' in comma:#(9)opens youtube ........................
        webbrowser.open("youtube.com")
        song = listen().lower()
        speak("playing "+song)
        pywhatkit.playonyt(song)
    elif 'search browser' in comma:#(10)searches on browser.................
        speak("What should I search?")
        query = listen()
        query = query.lower()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'open command prompt' in comma:#(11)opens command prompt...........
        os.system("start cmd")
        speak("opening command prompt!")
    elif 'open whatsapp' in comma:#(12)opens web-whatsapp
        webbrowser.open("https://web.whatsapp.com/")
    """elif 'send email' in comma:
        speak("what should i send?")
        content=listen().lower()
        speak("enter another person's email.")
        to=input("enter email adderss: ")
        sendEmail(to,content)"""
    elif "screenshot" in comma:#(13)takes screenshot........................
            t.sleep(2)
            test=take_ss()
            if test:
                print("Screenshot captured!")
            else:
                print("cant taken!")
    
run_vass()
