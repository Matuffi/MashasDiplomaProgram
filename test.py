import PySimpleGUI as sg
import DiplomaAutomation as auto

name_in_file = "names.txt"
lastname_in_file = "lastnames.txt"
diploma_template = "diploma.jpg"
output_path = "./out"
font_name = "CASTELAR.TTF"


sg.theme("Dark Amber")
#
# layout = [
# [sg.Text("Filename")],
# [sg.Input(), sg.FileBrowse()],
# [sg.OK(), sg.Button("Exit")]
# ]
#
# window = sg.Window("Title", layout)
#
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == "Exit":
#         break
#     print(event, values)
#
# window.close()
#
# sg.Popup(event,values[0])

##############################

layout = [
[sg.T("Automatic diploma filling program")],
[sg.FileBrowse("Template image", key="-BROWSE_TEMPLATE-", target="temp_show", size=12), sg.Text(key="temp_show", size=30)],
[sg.FileBrowse("Font file", key="-BROWSE_FONT-", target="font_show", size=12), sg.Text(key="font_show", size=30)],
[sg.FileBrowse("Name list", key="-BROWSE_NAME-", target="name_show", size=12), sg.Text(key="name_show", size=30)],
[sg.FileBrowse("*Last name list", key="-BROWSE_LAST_NAME-", target="last_name_show", size=12), sg.Text(key="last_name_show", size=30)],
[sg.Text("Output folder: "), sg.Input(size=20, key="-OUTPUT_PATH-")],
[sg.Text("Debugg: "), sg.Text(key="-DEBUGG-")],
[sg.Button("Run"), sg.Button("Exit"), sg.Button("Test")]
]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    # print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "Test":
        print(event, values)
    if event == "Run":
        if not (values["-BROWSE_TEMPLATE-"] or values["-BROWSE_FONT-"] or values["-BROWSE_NAME-"]):
            window["-DEBUGG-"].update("not enough data")
            continue

        output_path = "./" + values["-OUTPUT_PATH-"] if values["-OUTPUT_PATH-"] != "" else "./out"
        diploma_template = values["-BROWSE_TEMPLATE-"]
        font_name = values["-BROWSE_FONT-"]
        name_in_file = values["-BROWSE_NAME-"]
        lastname_in_file = values["-BROWSE_LAST_NAME-"] if values["-BROWSE_LAST_NAME-"] != "" else ""

        # print(output_path, diploma_template, font_name, name_in_file, lastname_in_file)
        auto.startAutomation(output_path, diploma_template, font_name, name_in_file, lastname_in_file)
        # window["-OUT-"].update(values["-IN-"])
        # print(values["-BROWSE-"])

window.close()
