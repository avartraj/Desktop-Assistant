import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyaudio

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back hacker!!")
    speak("Welcome back hacker!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning hacker!!")
        print("Good Morning hacker!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon hacker!!")
        print("Good Afternoon hacker!!")
        
    elif hour >= 16 and hour < 24:
        speak("Good Evening hacker!!")
        print("Good Evening hacker!!")
    else:
        speak("Good Night hacker, See You Tommorrow")

    speak("Janeman at your service hacker, please tell me how may I help you.")
    print("Janeman at your service hacker, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\KISHAN\\OneDrive\\Documents\\Janeman 2.0\\ss3.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "hu r u" in query:
            speak("I'm Janu created by hacknomious and I'm a hacker voice assistant.")
            print("I'm Janu created by hacknomious and I'm a hacker voice assistant.")

        elif "how r u" in query:
            speak("I'm fine hacker, What about you?")
            print("I'm fine hacker, What about you?")

        elif "fine" in query:
            speak("Glad to hear that hacker!!")
            print("Glad to hear that hacker!!")

        elif "good" in query:
            speak("Glad to hear that hacker!!")
            print("Glad to hear that hacker!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait hacker, I'm searching...")
                query = query.replace("wikipedia","https://www.wikipedia.com")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page hacker, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com")
        elif "open coursera" in query:
            wb.open("coursera.org")
        elif "open github" in query:
            wb.open("github.com")
        elif "open stackoverflow" in query:
            wb.open("stackoverflow.com")
        elif "open try hack me" in query:
            wb.open("tryhackme.com")

        elif "open google" in query:
            wb.open("google.com") 
        elif "open linkdin"in query:
            wb.open("linkdin.com")        
        elif "play music" in query:
            music_dir = "C:\\Users\\USER\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")


        elif "offline" in query:
            quit()

