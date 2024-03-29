import os
import subprocess
import time
import random
import typer
import PySimpleGUI as sg
sg.theme("DarkRed1")   
sg.DEFAULT_FONT = "LilitaOne"
exitcode = random.randint(0, 500)
exitcode2 = int(exitcode)
typer.out("Welcome to Brawl Stars Utilities\n")

def load_env_file(dotenv_path, override=False):
    with open(dotenv_path) as file_obj:
        lines = file_obj.read().splitlines() 
    dotenv_vars = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", maxsplit=1)
        dotenv_vars.setdefault(key, value)

    if override:
        os.environ.update(dotenv_vars)
    else:
        for key, value in dotenv_vars.items():
            os.environ.setdefault(key, value)
def saveapikey():
    sg.theme('DarkRed1')
    layoutapi= [
    [sg.VPush()], [sg.Text('Saving an API key will allow you to access Brawl Stats', size=(10,1)), sg.InputText(key='APIKEY')],[sg.Button('Submit'), sg.Button('Cancel')], [sg.VPush()]
        
    ]
    apiwin = sg.Window('BSU-Register',
                       layoutapi,
                       element_justification='center',
                       resizable=True).Finalize()
    event, values = apiwin.read(close=True)
    if event == 'Submit':
        apikey=values['APIKEY']
        apitext="APIKEY="+apikey
        envfile=open("api.env","w")
        envfile.write(apitext)
        envfile.close()
        exit("API key saved successfully")
    else:
        apiwin.close()
        exit("Saving API key failed")
def registerbsu():
    sg.theme('DarkRed1')
    layoutregister = [
        [sg.VPush()], [sg.Text('Please enter your chances')],
        [sg.Text('Username', size=(10, 1)),
         sg.InputText(key='USERNAME')],
        [sg.Text('Brawl Tag', size=(10, 1)),
         sg.InputText(key='BRAWLTAG')],
        [sg.Text('Rare chance', size=(10, 1)),
         sg.InputText(key='RARE')],
        [
            sg.Text('Super rare chance', size=(10, 1)),
            sg.InputText(key='SRARE')
        ], [sg.Text('Epic chance', size=(10, 1)),
            sg.InputText(key='EPIC')],
        [sg.Text('Mythic chance', size=(10, 1)),
         sg.InputText(key='MYTHIC')],
        [
            sg.Text('Legendary chance', size=(10, 1)),
            sg.InputText(key='LEGENDARY')
        ],
        [
            sg.Text('Boxes opened', size=(10, 1)),
            sg.InputText(key='BOXESOPENED')
        ], [sg.Button('Submit'), sg.Button('Cancel')], [sg.VPush()]
    ]
    regwin = sg.Window('BSU-Register',
                       layoutregister,
                       element_justification='center',
                       resizable=True).Finalize()
    event, values = regwin.read(close=True)

    if event == 'Submit':
        legendaryChance = values['LEGENDARY']
        rareChance = values['RARE']
        superRareChance = values['SRARE']
        epicChance = values['EPIC']
        mythicChance = values['MYTHIC']
        username = values['USERNAME']
        boxesOpened = values['BOXESOPENED']
        brawltag = values['BRAWLTAG']
        chanceL = 1 - (1 - int(legendaryChance)**int(boxesOpened))
        chanceR = 1 - (1 - int(rareChance)**int(boxesOpened))
        chanceSR = 1 - (1 - int(superRareChance)**int(boxesOpened))
        chanceE = 1 - (1 - int(epicChance)**int(boxesOpened))
        chanceM = 1 - (1 - int(mythicChance)**int(boxesOpened))
        username2 = repr(str(username))
        username3 = "username=" + username2
        username4 = str(username3)
        brawltag2 = repr(str(brawltag))
        brawltag3 = "brawltag=" + brawltag2
        brawltag4 = str(brawltag3)
        chance2 = repr(str(chanceL))
        chanceL3 = "chance=" + chance2
        chanceL4 = str(chanceL3)
        chancerare2 = repr(str(chanceR))
        chanceR3 = "chancerare=" + chancerare2
        chanceR4 = str(chanceR3)
        chanceSuperRare2 = repr(str(chanceSR))
        chanceSR3 = "chanceSuperRare=" + chanceSuperRare2
        chanceSR4 = str(chanceSR3)
        chanceEpic2 = repr(str(chanceE))
        chanceE3 = "chanceEpic=" + chanceEpic2
        chanceE4 = str(chanceE3)
        chanceMythic2 = repr(str(chanceM))
        chanceM3 = "chanceMythic=" + chanceMythic2
        chanceM4 = str(chanceM3)
        lobby1 = random.randint(1, 5)
        Lobby1 = repr(str(lobby1))
        LOBBY1 = "brawlLobby1=" + Lobby1
        LOBBY2 = str(LOBBY1)
        bsusave = "brawltag4=" + brawltag4 + "\n" + "username4="+ username4 + "\n" + "chanceR4=" + chanceR4 + "\n" + "chanceSR4="+ chanceSR4 + "\n" + "chanceM4=" + chanceM4 + "\n"+"chanceL4=" + chanceL4 + "\n" +"chanceE4="+ chanceE4
        settings = LOBBY2
        Save = open("bsusave.py", "w")
        Save.write(bsusave)
        Save.close()
        Save2 = open("settings.py", "w")
        Save2.write(settings)
        Save2.close()
        subprocess.run(["bash", "register.sh"], check=True)
        exit("Registration successful")
    else:
        print('User cancelled')
        regwin.close()
        exit("Registration aborted")


def loginbsu():
    sg.theme('DarkRed1')

    loginlayout = [[sg.VPush()], [sg.T("")],
                   [
                       sg.Text("Choose a file: "),
                       sg.Input(key='FILEPATH', size=(45, 1)),
                       sg.FileBrowse(file_types=(("BSU Files", "*.bsu"), ))
                   ], [sg.Button("Submit"), [sg.VPush()]]]

    loginwin = sg.Window("BSU-Login",
                         loginlayout,
                         element_justification='center',
                         resizable=True).Finalize()
    while True:
        event, values = loginwin.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Submit":
            filepath = values["FILEPATH"]
            filepath2 = str(filepath)
            subprocess.run(["bash", "login.sh", filepath2], check=True)
            break
    loginwin.close()


layoutmenu = [[sg.VPush()], [sg.Text("Login/Register Menu")],
              [sg.Button("Login")], [sg.Button("Save API Key")], [sg.Button("Register")],
              [sg.Button("QuickLogin")], [sg.VPush()]]

accwin = sg.Window('BSU-Login/Register',
                   layoutmenu,
                   element_justification='center',
                   resizable=True).Finalize()
while True:
    event, values = accwin.read()
    if event == 'Login':
        loginbsu()
        break
    if event == 'Register':
        registerbsu()
    if event == 'Save API Key':
        saveapikey()
    if event == sg.WIN_CLOSED:
        exit("Program aborted")
    if event == 'QuickLogin':
        if os.path.isfile('bsusave.py') and os.path.isfile('settings.py'):
            break
        else:
            exit("Make sure you have logged in at least once")

accwin.close()
from bsusave import chance, chancerare, chanceSuperRare, chanceEpic, chanceMythic
from settings import brawlLobby1
if brawlLobby1 == 1:
    typer.out("Lobby 1 has been picked\n")
if brawlLobby1 == 2:
    typer.out("Lobby 2 has been picked\n")
if brawlLobby1 == 3:
    typer.out("Lobby 3 has been picked\n")
optionslayout = [[sg.VPush()],[sg.Text("Select from Utilities")], [sg.Button("Settings")],
                 [sg.Button("Chance calculator")], [sg.Button("Brawl stats")],
                 [sg.Button("Save Maker")], [sg.Button("Update BSU")],[sg.VPush()]]
optionswin = sg.Window('BSU-Utilities', optionslayout,element_justification='center',resizable=True).Finalize()
while True:
    event, values = optionswin.read(close=True)
    if event == 'Brawl stats':
        subprocess.run(["python", "brawlstats.py"], check=True)
    if event == 'Update BSU':
        subprocess.run(["bash", "updater.sh"], check=True)
        exit(exitcode2)
    if event == 'Settings':
        subprocess.run(["python", "brawlsettings.py"], check=True)
        exit(exitcode2)
    if event == 'Save Maker':
        print(
            "This only works with files created with the power point calculator"
        )
        time.sleep(5)
        subprocess.run(["bash", "adder.sh"], check=True)
        exit(exitcode2)
    if event == 'Chance calculator':
        break
    if event == sg.WIN_CLOSED:
        exit(exitcode2)
optionswin.close()
CHANCERARE = "Rare-" + chancerare + "%"
CHANCESUPERRARE = "Super Rare-" + chanceSuperRare + "%"
CHANCEEPIC = "Epic-" + chanceEpic + "%"
CHANCEMYTHIC = "Mythic-" + chanceMythic + "%"
CHANCELEGENDARY = "Legendary-" + chance + "%"
rare_color = "#21FA35"
super_color = "#0831FF"
epic_color = "#A335C7"
mythic_color = "#FF0F00"
legendary_color = "#FFF928"

backgroundlayout = [
]
chancelayout = [[sg.VPush()], [sg.Text(CHANCERARE, text_color=rare_color)],
                [sg.Text(CHANCESUPERRARE, text_color=super_color)],
                [sg.Text(CHANCEEPIC, text_color=epic_color)],
                [sg.Text(CHANCEMYTHIC, text_color=mythic_color)],
                [sg.Text(CHANCELEGENDARY, text_color=legendary_color)],
                [sg.VPush()]]
chancewin = sg.Window('BSU-Chance Calculator',
                      chancelayout,
                      element_justification='center',
                      resizable=True).Finalize()

while True:
    event, values = chancewin.read(close=True)
    sg.bind()
    if event == sg.WIN_CLOSED:
        break
chancewin.close()
