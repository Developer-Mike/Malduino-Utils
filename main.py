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

#region Open
lf_open = ttk.LabelFrame(root, text="File")

bt_open = ttk.Button(lf_open, text="Open File", command=open_file)
bt_open.grid(row=0, column=0)

lf_open.pack(fill=tk.BOTH, pady=5, padx=5, expand=True)
#endregion

#region Run
lf_run = ttk.LabelFrame(root, text="Run")

lb_delay = ttk.Label(lf_run, text="Additional Delay: ")
lb_delay.grid(row=0, column=0)

additional_delay = tk.StringVar(root)
additional_delay.set("0")
et_delay = ttk.Entry(lf_run, textvariable=additional_delay)
et_delay.grid(row=0, column=1)

bt_run = ttk.Button(lf_run, text="Run Script", command=lambda:executor.Executor(current_file, additional_delay.get()))
bt_run.grid(row=0, column=2)

lf_run.pack(fill=tk.BOTH, pady=5, padx=5, expand=True)
#endregion

#region Save
lf_save = ttk.LabelFrame(root, text="Save")

target_language_short = tk.StringVar(root)
target_language_short.set("-")
om_language = ttk.OptionMenu(lf_save, target_language_short, *("-", "-", *languages.languages.keys()))
om_language.grid(row=0, column=0)

bt_translate = ttk.Button(lf_save, text="Translate and Move Script to SD", command=lambda:translator.translate(current_file, target_language_short.get()))
bt_translate.grid(row=0, column=1)

lf_save.pack(fill=tk.BOTH, pady=5, padx=5, expand=True)
#endregion

#open_file()
current_file = r"C:\Users\delta\Desktop\MalduinoUtils\test.txt"
root.mainloop()