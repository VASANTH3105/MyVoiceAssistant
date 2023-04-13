# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia
# pip install pyjokes


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say("alexa here  ")
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass  # nothing occurs

    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        # talk('playing songs for you')
        # print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  # %H 24hrs format
        print(time)
        talk('Current time is '+time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'are you in relationship' in command:
        talk("Yes I am in a relationship with wifi")
    elif 'joke' in command:
        # joke = pyjokes.get_jokes()
        # print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        # print(joke)
        # talk(joke)
    else:
        talk('Please say that again')


while True:
    run_alexa()
