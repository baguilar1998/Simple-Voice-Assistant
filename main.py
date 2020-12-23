import speech_recognition as sr
from Assistant import Assistant

recognizer = sr.Recognizer()
command = ''

with sr.Microphone() as source:
    print("Say a command")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    command = 'Command was not recognized'
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

assistant = Assistant()
assistant.run_command(command)