import tkinter as tk
from tkinter import filedialog

import translator, languages, executor

root = tk.Tk()
root.title("Malduino Utils")
current_file = None

def open_file():
    global current_file

    current_file = filedialog.askopenfilename()

bt_open = tk.Button(root, text="Open File", command=open_file)
bt_open.grid(row=0, column=0)

bt_run = tk.Button(root, text="Run Script", command=lambda:executor.Executor(current_file, additional_delay.get()))
bt_run.grid(row=0, column=1)

lb_delay = tk.Label(root, text="Additional Delay: ")
lb_delay.grid(row=1, column=0)

additional_delay = tk.StringVar(root)
additional_delay.set("0")
et_delay = tk.Entry(root, textvariable=additional_delay)
et_delay.grid(row=1, column=1, columnspan=2)

target_language_short = tk.StringVar(root)
target_language_short.set("-")
om_language = tk.OptionMenu(root, target_language_short, "-", *languages.languages.keys())
om_language.grid(row=2, column=0)

bt_translate = tk.Button(root, text="Translate and Move Script to SD", command=lambda:translator.translate(current_file, target_language_short.get()))
bt_translate.grid(row=2, column=1)

#open_file()
current_file = r"C:\Users\delta\Desktop\MalduinoUtils\test.txt"
root.mainloop()