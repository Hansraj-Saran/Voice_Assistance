import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import random
import os
import time
import tkinter
import operator
import smtplib
import requests
import shutil
import ctypes




engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if 0<= hour<12:
        speak("Good Morning!")

    elif 12<= hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    aname = ("I am Jarvis 1 point o version.")
    speak("I am Your Assistance")
    speak(aname)
    

def takecommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query= r.recognize_google(audio, language= 'en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print("can't recognize! Say again")
        return "None"
    return query

def username():
    speak("What should i call you sir")
    name= takecommand()
    speak(f"Welcome {name}")
    speak("How may i help you, Sir")

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hansrajsaranudsar@gmail.com', 'Hans@7665')
    server.sendmail('hansrajsaranudsar@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    while True:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/?client=safari")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        
        elif 'send a mail' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                speak("Whome should i send")
                to = input("Enter recevier's Email id:\n")
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email right now")
        
        elif 'how are you' in query:
            speak("I am fine, Thank You for Asking")
            speak("How are you, Sir")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine")

        elif 'i love you' in query:
            speak("It's hard to understand")
        
        elif 'wil you be my gf' in query or 'will you be my bf' in query:
            speak("I'm not sure about, may be you should give me some time")
        
        elif 'change my name to' in query:
            query = query.replace("change my name to", "")
            aname = query
            speak(f"your new name is {aname}")
        
        elif 'change your name' in query:
            speak("What would you like to call me")
            aname = takecommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(aname)
        
        elif 'exit' in query or 'quit' in query:
            speak("Thanks for giving me your time")
            exit()
        
        elif 'who made you' in query or 'who create you' in query:
            speak("Thanks to Hansraj for giving me a life")

            
            

            
     
  
