import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

import translator, languages, executor

root = tk.Tk()
root.title("Malduino Utils")
current_file = None

def open_file():
    global current_file

    current_file = filedialog.askopenfilename()

bt_open = ttk.Button(root, text="Open File", command=open_file)
bt_open.grid(row=0, column=0)

bt_run = ttk.Button(root, text="Run Script", command=lambda:executor.Executor(current_file, additional_delay.get()))
bt_run.grid(row=0, column=1)

lb_delay = ttk.Label(root, text="Additional Delay: ")
lb_delay.grid(row=1, column=0)

additional_delay = tk.StringVar(root)
additional_delay.set("0")
et_delay = ttk.Entry(root, textvariable=additional_delay)
et_delay.grid(row=1, column=1, columnspan=2)

target_language_short = tk.StringVar(root)
target_language_short.set("-")
om_language = ttk.OptionMenu(root, target_language_short, *("-", "-", *languages.languages.keys()))
om_language.grid(row=2, column=0)

bt_translate = ttk.Button(root, text="Translate and Move Script to SD", command=lambda:translator.translate(current_file, target_language_short.get()))
bt_translate.grid(row=2, column=1)

#open_file()
current_file = r"C:\Users\delta\Desktop\MalduinoUtils\test.txt"
root.mainloop()