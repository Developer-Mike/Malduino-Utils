import keyboard
import time
import threading


class Executor():
    _special_keys = {
        "CTRL" : None, 
        "GUI" : "cmd", 
        "SHIFT" : None,
        "ALT_LEFT" : "alt",
        "ALT_RIGHT" : "alt gr",
        "CAPSLOCK" : None,
        "ENTER" : None,
        "DELETE" : "del",
        "BACKSPACE" : None,
        "ESC" : None,
        "INSERT" : None,
        "SPACE" : None,
        "TAB" : None,
        "DOWN" : None,
        "LEFT" : None,
        "RIGHT" : None,
        "UP" : None,
        "F1" : None, "F2" : None, "F3" : None, "F4" : None, "F5" : None, "F6" : None, "F7" : None, "F8" : None, "F9" : None, "F10" : None, "F11" : None, "F12" : None}

    additional_delay = 0
    default_delay = 0
    default_char_delay = 0
    last_line = None

    def __init__(self, script_path, additional_delay):
        self.additional_delay = int(additional_delay) / 1000

        t = threading.Thread(target=self._execute, args=[script_path])
        t.start()

    def _execute(self, script_path):
        with open(script_path, "r") as file:
            script_content = file.readlines()

        for line in script_content:
            line = line.strip()

            self._execute_line(line)
            self.last_line = line
            

    def _execute_line(self, line):
        function, argument = self._function_parser(line)
        print(function, argument)
        
        if function.startswith("REM") or function.startswith("LOCALE"):
            return
        elif function.startswith("DELAY"):
            time.sleep(int(argument) / 1000)
        elif function.startswith("DEFAULTDELAY"):
            self.default_delay = int(argument) / 1000
        elif function.startswith("DEFAULTCHARDELAY"):
            self.default_char_delay = int(argument) / 1000
        elif function.startswith("STRING"):
            keyboard.write(argument, delay=self.default_char_delay)
        elif function.startswith("REPLAY") or function.startswith("REPEAT"):
            for _ in range(int(argument)):
                self._execute_line(self.last_line)
        else:
            if not self._is_special_key(function):
                    return

            current_argument = line
            is_special_key = True
            text_to_execute = None
            while is_special_key:
                current_function, current_argument = self._function_parser(current_argument)
                is_special_key = self._is_special_key(current_function)

                if text_to_execute is None:
                    text_to_execute = self._get_modifier_from_function(current_function)
                else:
                    text_to_execute += f"+{self._get_modifier_from_function(current_function)}"

                
            
            print("######", text_to_execute)
            keyboard.press_and_release(text_to_execute)

        time.sleep(self.default_delay)
        time.sleep(self.additional_delay)

    def _is_special_key(self, key):
        return key in self._special_keys

    def _get_modifier_from_function(self, function):
        if function in self._special_keys:
            return self._special_keys[function].lower()

        return function.lower()

    def _function_parser(self, line):
        splitted_line = line.split(" ")
        return splitted_line[0], " ".join(splitted_line[1:])