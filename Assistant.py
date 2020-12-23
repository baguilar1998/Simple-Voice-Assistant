import pyttsx3
from OpenCommandTranslator import OpenCommandTranslator
import time


class Assistant:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 120)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def run_command(self, command):

        command = command.upper()

        if 'OPEN' in command:
            name = command[command.find(" ")+1:]
            if OpenCommandTranslator.program_exists(name):
                self.engine.say('Opening ' + name)
                self.engine.runAndWait()
                OpenCommandTranslator.open(name)

        elif "SET A TIMER" in command:
            # Run a timer
            time_list = [0,0,0]
            time_index = {'HOURS': 0, 'MINUTES': 1, 'SECONDS': 2}
            current_digit = 0
            for i in command.split():
                if i.isdigit():
                    current_digit = int(i)
                else:
                    for key in time_index.keys():
                        if i in key:
                            if 'S' not in i:
                                i = i +'S'
                            time_list[time_index[i]] = current_digit
                            current_digit = 0
            seconds = (time_list[0] * 3600) + (time_list[1] * 60) + time_list[2]
            self.engine.say('Timer has begun')
            self.engine.runAndWait()
            time.sleep(seconds)
            self.engine.say("Timer has ended")
            self.engine.runAndWait()
