import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import subprocess
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) #to select voice


def speak(audio):   #function for giving audio output
    engine.say(audio)
    engine.runAndWait()


def greetings():    # greetings according the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" I am Anna. your voice assistent. how may I help you, ")       

def command():# for taking audio commmands


    r = sr.Recognizer()
    with sr.Microphone() as source: #taking input from mic
        r.adjust_for_ambient_noise(source) #for sadjusting noice
        print("Listening...")
        
        r.pause_threshold = 1
      
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #selecting language
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")    
        speak("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":#main
    greetings()#for greeting
    while True:
    
        query = command().lower()       #converts the input into lowercase string


        #logic for performing queries

        if 'how are you' in query:
            speak('I am very well thanks for asking')
            print('I am very well thanks for asking')

        if 'what can you do' in query:
            speak('I can do some basic stuff, on just a single command of your voice. I am meant to make things easy for you. I hope you like my service')
            
        
        
           

        
        elif 'wikipedia for' in query:
            speak('Searching Wikipedia...')
            
            search_term = query.split("for")[-1]
            url = f"https://en.wikipedia.org/wiki/{search_term}"
            speak('Here is what I found on wikipedia for ' + search_term)
            webbrowser.get().open(url)
            
        elif 'find location' in query:
            location = query.split("of")[-1]
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            speak(f'Here is the location of {location} on google maps')
            webbrowser.get().open(url)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")


        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")
            
        elif 'open facebook' in query:
            webbrowser.open("https://facebook.com")

        elif 'open msbte' in query:
            speak('Opening the official website of MSBTE')
            webbrowser.open("https://msbte.org.in/")

        elif 'open google drive' in query:
            webbrowser.open("https://drive.google.com/drive/my-drive")


        elif 'search for' in query:
            search_term = query.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            speak('Here is what I found for ' + search_term)
            
            webbrowser.get().open(url)

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")  


        elif 'yeah boy' in query:   #don't mind anything from here...
            speak('yeahh boi ,lets go') 

        elif 'chal chal ave' in query:
            speak('to, chal chal ave, ')   

        elif 'chal chal ve' in query:
                    speak('to, chal chal ave') 
        elif 'adbhut' in query:
             speak('a  ti soondar') 
        elif 'yo' in query:
            speak('yaooo')          # ...to here

        elif  'open spotify'in query:
            music_dir =  'C:\\Users\Mero_Account\AppData\Roaming\Spotify\Spotify.exe' 
            os.startfile(music_dir)
            speak('opening spotee fy ,please wait')

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f'the time is : {strTime}')


        elif 'i want' in query:
            item = query.split("want")[-1]
            prefrence = query.split('from')[-1]
            
                
            url = 'https://www.amazon.com/s?k='+ item
            webbrowser.get().open(url) 
            speak(f'you can buy  {item} from here')
                




        elif 'open vs code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(codePath)


        if 'exit' in query:     #for exxiting
             speak(' Thank you  for using our project')
             exit()

        if 'wait' in query:     # to pause it for 10 seconds
            
            speak('waiting for 10 seconds ')
            print('Waiting...')
            time.sleep(10)
            speak(' i am Ready to go again')
            print('Ready to go again')
            

  
