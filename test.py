from lib import PySimpleGUI as sg

import DiplomaAutomation as auto
import os

name_in_file = "names.txt"
lastname_in_file = "lastnames.txt"
diploma_template = "diploma.jpg"
output_path = "./out"
font_name = "CASTELAR.TTF"

raw_font_list = os.listdir(r'C:\Windows\fonts')
font_list = ["-Custom-"]
for i in raw_font_list:
    if "ttf" in i or "TTF" in i:
        font_list.append(i)

print(font_list)


sg.theme("Dark Grey 13")

layout = [
[sg.T("Automatic diploma filling program")],
[sg.FileBrowse("Template image", key="-BROWSE_TEMPLATE-", target="temp_show", size=12, enable_events=True), sg.Text(key="temp_show", size=30)],
[sg.Combo(font_list, default_value=font_list[0], size=15, enable_events=True, key="-FONT_COMBO-"), sg.FileBrowse("Font file", key="-BROWSE_FONT-", target="font_show", size=12), sg.Text(key="font_show", size=30)],
[sg.FileBrowse("Name list", key="-BROWSE_NAME-", target="name_show", size=12), sg.Text(key="name_show", size=30)],
[sg.FileBrowse("*Last name list", key="-BROWSE_LAST_NAME-", target="last_name_show", size=12), sg.Text(key="last_name_show", size=30)],
[sg.Text("Output folder: "), sg.Input(size=20, key="-OUTPUT_PATH-")],
[sg.Text("Debugg: "), sg.Text(key="-DEBUGG-")],
[sg.Button("Run"), sg.Button("Exit"), sg.Button("Test")]
]

window = sg.Window("Title", layout)

debug_count = 0

def debug(text):
    global debug_count
    debug_count += 1
    window["-DEBUGG-"].update(f"[{str(debug_count)}] {text}")

default_font = False

while True:
    event, values = window.read()
    # print(event, values, debug_count)
    if event == sg.WIN_CLOSED or event == "Exit" and sg.popup_yes_no("U sure?") == "Yes":
        break
    if event == "-FONT_COMBO-":
        if values["-FONT_COMBO-"] == font_list[0]:
            default_font = False
        else:
            default_font = True
            print("change")
    if event == "Test":
        font_name = values["-FONT_COMBO-"] if default_font else values["-BROWSE_FONT-"]
        print(event, values, font_name)
    if event == "Run":
        if not (values["-BROWSE_TEMPLATE-"] and (values["-BROWSE_FONT-"] or default_font) and values["-BROWSE_NAME-"]):
            debug("Not enough data")
            continue

        output_path = "./" + values["-OUTPUT_PATH-"] if values["-OUTPUT_PATH-"] != "" else "./out"
        diploma_template = values["-BROWSE_TEMPLATE-"]
        font_name = values["-FONT_COMBO-"] if default_font else values["-BROWSE_FONT-"]
        name_in_file = values["-BROWSE_NAME-"]
        lastname_in_file = values["-BROWSE_LAST_NAME-"] if values["-BROWSE_LAST_NAME-"] != "" else ""

        # print(output_path, diploma_template, font_name, name_in_file, lastname_in_file)
        time = auto.startAutomation(output_path, diploma_template, font_name, name_in_file, lastname_in_file)
        # window["-OUT-"].update(values["-IN-"])
        # print(values["-BROWSE-"])

        debug(f"Run was succesful {time}s")

window.close()
