import googlesearch
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
#from decouple import config




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
        print("good morning!")

    elif hour >=12 and hour<18:
        speak("good afternoon!")
        print("good afternoon!")
    else:
        speak("good evening!")
        print("good evening!")

    speak("I am Nezuko please tell me how may i help you")
    print("I am Nezuko please tell me how may i help you")




def takeCommand():
    #it takes microphone input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)


        print("say that again please....")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #Logic 
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            #result2 = googlesearch.search(query,num_results=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'hey' in query:
            speak("Hello how may i help you!")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open pinterest' in query:
            webbrowser.open("https://in.pinterest.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        #elif 'stop' in query:
         #   music_dir = 'C:\\music'
          #  songs = os.listdir(music_dir)
           # os.stopfile(os.path.join(music_dir, songs[0]))



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime} ")

        elif ' date' in query:
            strDate = datetime.date.today().strftime("%D:M:%Y")
            speak(f"Mam, the DATE is {strDate} ")

        elif 'Open code' in query:
            codePath = "C:\\Users\\asmit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        elif 'exit' in query:
            exit()

       


