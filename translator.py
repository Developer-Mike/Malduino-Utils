import psutil
import os
import languages


def translate(source_path, target_lang):
    if target_lang not in languages.languages:
        return
    target_lang_chars = languages.languages[target_lang]

    with open(source_path, "r") as file:
        text = file.readlines()

    edited_text = ""
    for line in text:
        if line.upper().startswith("REM"):
            edited_text += line
            continue

        for char in line:
            if char in target_lang_chars:
                edited_text += target_lang_chars[char]
            else:
                edited_text += char

    target_path = None
    for partion in psutil.disk_partitions():
        if "removable" in partion.opts.split(","):
            target_path = os.path.join(partion.mountpoint, os.path.basename(source_path))

    with open(target_path, "w") as file:
        file.write(edited_text)

#os.system(f'powershell $driveEject = New-Object -comObject Shell.Application; $driveEject.Namespace(17).ParseName("""{target_path.split(":")[0]}:""").InvokeVerb("""Eject""")')