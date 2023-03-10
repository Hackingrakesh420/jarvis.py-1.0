import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("good Afternoon Boss!")

    else:
        speak("good Evening Boss!")
    
    speak("I am jarvis 1.0 how can help you")       
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....") 
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")  

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"     
    return query

if __name__ =="__main__":
    wishme()
    while True:
    #if 1:
     query = takeCommand().lower()

     if 'wikipedia' in query:
           speak('Searching Wikipedia.....')
           query = query.replace("Wikipedia", " ")
           results = wikipedia.summary(query, sentences = 2)
           speak("According to wikipedia")
           print(results)
           speak(results)
 
     elif 'open youtube' in query:  
         webbrowser.open("youtube.com")

     elif 'open google' in query:  
         webbrowser.open("google.com")  

     elif 'open Gmail' in query:  
         webbrowser.open("Gmail.google.com")   

     elif 'open stackoverflow' in query:  
         webbrowser.open("stackoverflow.com")    

     elif 'play music' in query:  
        music_dir = 'D:\\Non Critical\\songs\\my music1'    
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

     elif'the time'in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(F"boss, the time is {strTime}") 


     elif 'open code' in query:
         codepath = "D:\\ADMIN\\Microsoft VS Code\\Code.exe"         
         os.startfile(codepath)
          
     elif 'open whatsapp 1'in query:
         whatsapppath1 = 'C:\\Users\\ADMIN\\OneDrive\\Desktop'
         os.startfile( whatsapppath1)
         
     elif 'open whatsapp 2'in query:
         whatsapppath2 = 'C:\\Users\\ADMIN\\OneDrive\\Desktop'
         os.startfile( whatsapppath2)    



         


