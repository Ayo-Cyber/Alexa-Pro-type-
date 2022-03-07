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
    engine.say(text)
    engine.runAndWait()


def try_commands():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            listener.adjust_for_ambient_noise(source)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    instruct = try_commands()
    print(instruct)
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruct:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who is' in instruct:
        person = instruct.replace('who is', '')
        info = wikipedia.summary(person, 2)
        talk(info)
        print(info)
    elif 'what is ' in instruct:
        answer = instruct.replace('what is', '')
        info_1 = wikipedia.summary(answer, 2)
        talk(info_1)
        print(info_1)
    elif 'joke' in instruct:
        talk(pyjokes.get_joke())
    else:
        talk("I didn't get you well the first time .")


while True:
    run_alexa()
