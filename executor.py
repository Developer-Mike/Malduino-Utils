import keyboard
import time
import threading


class Executor():
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
        elif function.startswith("REPLAY"):
            for _ in range(int(argument)):
                self._execute_line(self.last_line)
        elif function.startswith("GUI"):
            keyboard.press_and_release(f"cmd+{argument}")
        else:
            if not keyboard.is_modifier(function):
                    return

            executed_text = None
            current_function = self._get_modifier_from_function(function)
            current_argument = argument
            while keyboard.is_modifier(current_function):
                if executed_text is None:
                    executed_text = function
                else:
                    executed_text += f"+{function}"

                current_function, current_argument = self._function_parser(current_argument)
                current_function = self._get_modifier_from_function(current_function)
            


        time.sleep(self.default_delay)
        time.sleep(self.additional_delay)

    def _get_modifier_from_function(self, function):
        if function == "HI":
            return "HO"

        return function

    def _function_parser(self, line):
        splitted_line = line.split(" ")
        return splitted_line[0], " ".join(splitted_line[1:])