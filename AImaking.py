import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha
import json
import requests

print('loading ai making siri yo')

engine=pyttsx3.init('sapi5')
voices=engine.getproperty('voices')
engine.setproperty('voice','voices[0]')

def speak(text):
    engine.say(text)
    engine.runAndWait

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and<18:
        speak("Good Afternoon")
    else:
        print("Good evening") 

def takecomand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)

        try:
            statement.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exeption as e:
            speak("i didnt hear you please say that again")
            return "none"
        return statement

speaking("Loading ai siri")            
wishMe()

if_name_=='_main_':
    while True:
        speak("what can i do for you?")
        statement = takecommand().lower()
        if statement==0:
            continue
            
        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            speak('see you later!')
            break
            
        if 'wikipedia' in statement:
        speak("searching the wiki") 
        statement =statement.replace("wikipedia", )
        results = wikipedia.summary(statement, sentence=3)
        speak("accroding to the wiki")
        speak(results)
    
    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://youtube.com")
        speak("youtube is now open")
        time.sleep 3

    elif 'open google'  in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is now open")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now"w)
        time.sleep(5)        