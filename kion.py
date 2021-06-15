from pywhatkit.main import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googlesearch-python import search  as google

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
      engine.say(text)
      engine.runAndWait()
def take_command():      
    try:
        with sr.Microphone() as source:
            print('listning now....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'ki' in command:
                command = command.replace('ki','') 
    except:
            pass
    return command   

def run_alexa():
    command = take_command()
    print(command) 
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time) 
    elif 'who is' and 'what is a' and 'what is an' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'google' in command:
        ge = command.replace('google','')
        goog = google(ge)
        talk(goog)
    else:
        talk('Please say this again')
while True:
    run_alexa()
