import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command;

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%h:%m')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'i love you' in command:
        talk('I love you too')
    elif 'Hi alexa' or 'Hello alexa' in command:
        talk('Hi')
    elif 'How are you' in command:
        talk('me, I am good')
    elif 'thank you' in command:
        talk('welcome')
    elif 'can you' in command:
        talk('Yes, I can')
    elif 'name' in command:
        talk('my name is Alexa')
    elif 'date' in command:    
        talk('sorry, I am very busy this time.')
    elif 'favourite' or 'like' in command:
        talk('Your favourite is mom and dad')
    elif 'are you single' in command:
        talk('No, I am in relastionship with you')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        talk("I can't hear you, say it again")

while True:
    run_alexa()
