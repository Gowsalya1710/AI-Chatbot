from email.mime import audio
from unicodedata import name
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good  morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("i    am    one    of    the    mediguide     i    give  all  the  information   that  you     want   and  out  of  the   thing      i   will  refer  wikipedia   and give  ")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...............")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("wait   for   few  minutes")
        query=r.recognize_google(audio,language='en-in')
        print("user   said",query)
    except Exception as e:
        print(e)
        speak("say   that   again   please")
    return query
    
if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if "fever" in query:
            speak("asprin")
        elif "stomach pain" in query:
            speak("ioperamide")
        elif "skin allergy" in query:
            speak("caladryl lotion") 
        elif "ulcer" in query:
            speak("omeprazole,alumina,magnesia")
        elif "acidity" in query:
            speak("protonix")
        elif "headache" in query:
            speak("paracetamol")
        
        elif  "wikipedia" in query:
            speak("searching   in   wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According  to  wikipedia ")
            speak(results)
            
            
            
        else:
            speak("use word wikipedia")
        
    

        
    

    





    
    