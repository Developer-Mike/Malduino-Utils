import keyboard
from pynput.keyboard import Key
import time


class Executor():
    default_delay = 0
    default_char_delay = 0
    last_line = None

    def __init__(self, script_path, additional_delay):
        with open(script_path, "r") as file:
            script_content = file.readlines()
        
        for line in script_content:
            self._execute_line(line)
            self.last_line = line
            

    def _execute_line(self, line):
        function, argument = self._function_parser(line)
            
        if function.startswith("REM"):
            return
        elif function.startswith("DELAY"):
            time.sleep(int(argument))
        elif function.startswith("DEFAULTDELAY"):
            self.default_delay = int(argument)
        elif function.startswith("DEFAULTCHARDELAY"):
            self.default_char_delay = int(argument)
        elif function.startswith("STRING"):
            keyboard.write(argument, delay=self.default_char_delay)
        elif function.startswith("REPLAY"):
            for _ in range(int(argument)):
                self._execute_line(self.last_line)
        elif function.startswith("GUI"):
            keyboard.press(Key.cmd)
            keyboard.press(argument)
            keyboard.release(Key.cmd)
        elif function.startswith("REM"):
            pass

        time.sleep(self.default_delay)
        time.sleep(self.additional_delay)

    def _function_parser(self, line):
        splitted_line = line.split(" ")
        return splitted_line[0], " ".join(splitted_line[1:])