import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       # fix: getProperty (capital P)
engine.setProperty('voice', voices[0].id)  # fix: use voices[0].id properly

def speak(text):
    engine.say(text)
    engine.runAndWait()                     # fix: added ()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:          # fix: added 'hour' before <18
        speak("Good Afternoon")
    else:
        speak("Good Evening")              # fix: speak() not print()

def takecommand():                         # fix: corrected spelling
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')  # fix: r.recognize_google
            print(f"User said: {statement}\n")
        except Exception as e:             # fix: correct spelling
            speak("I didn't hear you, please say that again")
            return "none"
        return statement

speak("Loading your AI")                  # fix: speak() not speaking()
wishMe()

if __name__ == '__main__':               # fix: correct dunder syntax
    while True:
        speak("What can I do for you?")
        statement = takecommand().lower()

        if statement == "none":          # fix: check for "none" string
            continue

        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            speak('See you later!')
            break

        elif 'wikipedia' in statement:   # fix: changed 'if' to 'elif', fixed indent
            speak("Searching Wikipedia")
            statement = statement.replace("wikipedia", "")  # fix: added ""
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("YouTube is now open")
            time.sleep(3)               # fix: added ()

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is now open")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Gmail is now open")  # fix: removed stray 'w'
            time.sleep(5)