import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Bhavya!")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon Bhavya!")
    
    else:
        speak("Good Evening Bhavya!")

    speak("I am dora Maam. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r = sr. Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif'play youtube music' in query:
            webbrowser.open("youtube music.com")

        elif'alexa play music' in query:
            webbrowser.open("alexa.com")

        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is{strTime}")
        
        elif'open code' in query:
            CodePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CodePath)


        



        
