import pyttsx3                         
import speech_recognition as sr       
import datetime                       
import os                             
import ctypes
import cv2
#import pywintypes
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pywhatkit
import psutil
import speedtest
from twilio.rest import Client
import sys
import pyjokes
import wolframalpha
import instaloader
import selenium
from pywikihow import search_wikihow
import time
import requests
#import PyDictionary
#from PyDictionary import PyDictionary as Diction
from bs4 import BeautifulSoup
import newsapi
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import pyautogui
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)
    print("the current date is:")
    print(date,month,year)

def wishMe():
    date()
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good morning, its {tt}")
        print(f"Good morning, its {tt}")

    elif hour>=12 and hour<18:
        speak(f"good afternoon, its {tt}")
        print(f"Good afternoon, its {tt}")

    else:
        speak(f"Good evening, its {tt}")
        print(f"Good evening, its {tt}")

    speak("I am jarvis sir please tell how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=8,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        speak("Say that again please....")
        return "none"
    return query

def news():
    main_url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=d8e8c66e6dda46afafbccca3fe0b0c50')
    
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: ",head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def music():
    speak("Tell Me The Name Of The Song")
    musicName = takeCommand()

    if "All Black" in musicName:
        os.startfile("D:\\Dj all sons\\NEW SONG\\All Black.mp3")

    if "Chaska" in musicName:
        os.startfile("D:\\Dj all sons\\NEW SONG\\Chaska.mp3")

    else:
        kit.playonyt(musicName)

    speak("Your Songs Has Been Started! , Enjoy Sir...")

"""def openDict():
        speak("Activated Dictionary")
        speak("sir tell me the problem")
        prob1 = takeCommand()

        if 'meaning' in prob1:
            prob1 = prob1.replace("Jarvis","")
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("meaning of","")
            result = Diction.meaning(prob1)
            speak(f"The Meaning of {prob1} is {result}")

        elif 'synonym' in prob1:
            prob1 = prob1.replace("Jarvis","")
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("synonym of","")
            result = Diction.synonym(prob1)
            speak(f"The synonym of {prob1} is {result}")

        elif 'antonym' in query:
            prob1 = prob1.replace("Jarvis","")
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("antonym of","")
            result = Diction.antonym(prob1)
            speak(f"The antonym of {prob1} is {result}")

        speak("Exited Dictionary")"""


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "who are you" in query or "define yourself" in query:
            speak("J.A.R.V.I.S. is a example of artificial intelligence that was developed or coded by Ayush saini for his college project. I can do some task for user choice ")
            print("J.A.R.V.I.S. is a example of artificial intelligence that was developed or coded by Ayush saini for his college project. I can do some task for user choice ")
            
        elif "your name" in query:
            speak("Sir bascially Ayush told my name is JARVIS thats name means Just A Rather Very Intelligent System")
            print("Sir bascially Ayush told my name is JARVIS thats name means Just A Rather Very Intelligent System")

        elif "website" in query:
            speak("Ok Sir , Launching....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace("%20","")
            query = query.replace("  ","")
            web1 = query.replace("open","")
            web2 = 'https://www.'+ web1 + '.com'
            webbrowser.open(web2)
            speak("Launched Sir")

        elif "open pictures" in query:
            npath = "C:\\Users\\ayush\\Pictures\\ayush saini pics" 
            os.startfile(npath)

        elif "open word" in query:
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe" 
            os.startfile(npath)

        elif "open c drive" in query:
            npath = "C:"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "volume up" in query:
            pyautogui.press("volumeup")
        
        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute " in query:
            pyautogui.press("volumemute")

        elif "music" in query:
            music()
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\New folder\\2018"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is{ip}")
            print("your IP address is{ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube search" in query:
            speak("Ok sir , This is what I found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("done sir")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "maps" in query:
            webbrowser.open("https://www.google.com/maps/place/Bohra+Masjid+Harda/@22.3387752,77.0893898,403m/data=!3m1!1e3!4m13!1m7!3m6!1s0x397d70da30805abf:0x1368c14a9092d58b!2sHarda,+Madhya+Pradesh+461331!3b1!8m2!3d22.3466702!4d77.0889583!3m4!1s0x397d70d879c45901:0xe8a8d93f164fa386!8m2!3d22.3374815!4d77.0888491")


        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                    0,
                                                    "C:\\Users\\ayush\\Pictures\\wallpaper\\127091-download-hd-wallpapers-for-windows-10-1920x1080.jpg",
                                                    0)
            speak("Background changed succesfully")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'Full Screen' in query:
            keyboard.press('f')

        elif 'theatre mode' in query:
            keyboard.press('t')

        elif 'miniplayer' in query:
            keyboard.press('i')

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'Open a new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'Open a new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif "screnshot" in query:
            kk = pyautogui.screenshot()
            kk.save('C:\\Users\\ayush\\Desktop\\project')


        elif "play song on youtube" in query:
            kit.playonyt("Ellie Goulding - Love Me Like You Do - Fifty Shades of Grey")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")

#to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close notepad++" in query:
            speak("okay sir, closing notepad++")
            os.system("taskkill /f /im notepad++.exe")

        elif "close google chrome" in query:
            speak("okay sir, closing google chrome")
            os.system("taskkill /f /im google chrome .exe")

        elif "close netbeans" in query:
            speak("okay sir, closing netbeans")
            os.system("taskkill /f /im netbeans.exe")

        elif "close VLC media prayer" in query:
            speak("okay sir, closing VLC media prayer")
            os.system("taskkill /f /im VLC.exe")

        elif "close Powerpoint" in query:
            speak("okay sir, closing Powerpoint")
            os.system("taskkill /f /im Powerpoint.exe")

        elif "close word" in query:
            speak("okay sir, closing word")
            os.system("taskkill /f /im WINWORD.exe")

        elif "close control panel" in query:
            speak("okay sir, closing control panel")
            os.system("taskkill /f /im control.exe")

        elif "close Excel" in query:
            speak("okay sir, closing Excel")
            os.system("taskkill /f /im EXCEL.exe")

        elif "close WinRAR" in query:
            speak("okay sir, closing WinRAR")
            os.system("taskkill /f /im WinRAR.exe")

        elif "close Microsoft Edge" in query:
            speak("okay sir, closing Microsoft Edge")
            os.system("taskkill /f /im msedge.exe")

        elif "close ONENOTE" in query:
            speak("okay sir, closing ONENOTE")
            os.system("taskkill /f /im ONENOTE.exe")

######################################################################################################################################
######################################################################################################################################
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me the news" in query:
            speak("wait sir we are fetching news for you")
            news()

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==10:
                music_dir = "C:\\Users\\ayush\\Desktop\\project\\MUSIC"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

#to find a python jokes
        elif "tell me a joke" in query:
            jokes = pyjokes.get_joke()
            speak(jokes)
            print(jokes)

#--------------to check a instagram profile------
        elif "instagram profile" in query:
            speak("sir please enter the username correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to downlooad the profile picture of this account")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()#pip install instaloader
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir")
            else:
                pass

#------------------  to take screenshot
        elif "take screenshot" in query:
            speak("sir please tell me the name of the screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder . now i am ready for other work")

#------------------to hide files and folders
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or visible for everyone")
            condition = takeCommand().lower()
            if "hidden" in condition:
                os.system("attrib +h /s /d") #os module
                speak("sir , all the files in this folder are now hidden")
                
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir all the files os this folder are now visible")

            elif "leave it" in condition:
                speak("ok sir")

#-------------------------- search anything 
        elif "activate how to mod" in query:
            speak("How how to mod is activated please tell me what you want to know")
            how = takeCommand()
            try:
                if "exit" or "close" in how:
                    speak("okay sir how to do mod is closed")
                    break
                else:
                    max_results = 1
                    how_to = search_wikihow(how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak("sorry  sir, I am not able to find this")

#----------------check battery percentage
        elif "how much power left" in query or "how much power we have" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("sir we have to connect our system to charging port please find some charging port to continue this work")
            elif percentage<=15 and percentage<=30:
                speak("sir we don't have enough power to work, please connect to charging port then we have to continue this work")
            elif percentage<=15:
                speak("sir we have very less power, please connect to charging the system otherwise the system will be shutdown")

#------------------to check the internet speed
        elif "internet speed" in query:
            import speedtest
            #st = speedtest.Speedtest()
            #dl = st.download()
            #up = st.upload()
            #speak(f"sir we have {dl} bit per second downloading speed and {up} bits per second uploading speed")
            #print(f"sir we have {dl} bit per second downloading speed and {up} bits per second uploading speed")
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")

#-------------- to send message        
        elif "send message" in query:
            speak("sir what should i say")
            msz = takeCommand()

            account_sid = 'AC48e70c5fc745c58f5a77d68036236c4c'
            auth_token = '53ec82ca1f03b6cd93b21ebf45ca53dd'

            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body= msz,
                    from_='+17047434756',
                    to='+916261236062'
                )

            print(message.sid)

#------------to set and activate alarm
        elif "alarm" in query:
            speak("sir please tell me the time to set alarm, for example, set alarm to 5:30 am")
            tt = takeCommand()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            import Myalarm
            Myalarm.alarm(tt)

#--------------open mobile camera 
        elif "open mobile camera" in query:
            import urllib.request
            import cv2 
            import numpy as np
            import time
            URL = "http://192.168.43.54:8080//shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;

            cv2.destroyAllWindows()

#-------------to call the person
        elif "call" in query:
            speak("Wait sir i can call")
            from twilio.rest import Client

            account_sid = 'AC48e70c5fc745c58f5a77d68036236c4c'
            auth_token = '53ec82ca1f03b6cd93b21ebf45ca53dd'

            client = Client(account_sid, auth_token)

            callable = client.calls \
                .create(
                    twiml='<Response><Say>This is testing call from jarvis side</Response></Say>',
                    from_='+17047434756',
                    to='+916261236062'
                )

            print(callable.sid)



        
