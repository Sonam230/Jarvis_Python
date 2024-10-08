import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

#pip install pocketsphinx

recognizer = sr. Recognizer()
engine = pyttsx3.init()
newsapi= "a25987f0291444bd8e44e55ac8159900"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")   
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
        #parse the json respnse
           data=r.json()
        #Extract the articles
           articles=data.get('article', [])
        #print the headlines
           for article in articles:
              speak(article['title'])

    else:
        #let openAi handle the request
        pass
      
        
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen  for the wake word "Jarvis"
        #obtain audio from the microphone
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
             with sr.Microphone() as source:
               print("Listening...")
               audio = r.listen(source,timeout=3, phrase_time_limit=3)
               word = r.recognize_google(audio)
             if(word.lower() =="jarvis"):
                 speak("Ya")
                 #Listen for command  
                 with sr.Microphone() as source:
                   print("Jarvis Active..")
                   audio = r.listen(source)
                   command= r.recognize_google(audio)

                   processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
