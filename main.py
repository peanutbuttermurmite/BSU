from tkinter import *
import os
import subprocess
import tkinter as tk
import time
import random
import typer
from PIL import Image, ImageTk
import enquiries
import PySimpleGUI as sg
exitcode =random.randint(0,500)
exitcode2 = int(exitcode)
typer.out("Welcome to Brawl Stars Utilities\n")
time.sleep(0.0000000001)
def registerbsu():
    sg.theme('Dark Blue 3')
    layoutregister = [
        [sg.Text('Please enter your chances')],
        [sg.Text('Username', size = (10, 1)),
         sg.InputText(key='USERNAME')],
        [sg.Text('Brawl Tag', size = (10, 1)),
         sg.InputText(key='BRAWLTAG')],
        [sg.Text('Rare chance', size =(10, 1)),
         sg.InputText(key='RARE')],
        [sg.Text('Super rare chance', size =(10, 1)),
         sg.InputText(key='SRARE')],
        [sg.Text('Epic chance', size = (10,1)),
         sg.InputText(key='EPIC')],
        [sg.Text('Mythic chance', size=(10, 1)), 
         sg.InputText(key='MYTHIC')],
        [sg.Text('Legendary chance', size=(10, 1)),
         sg.InputText(key='LEGENDARY')],
        [sg.Text('Boxes opened', size= (10, 1)),     
         sg.InputText(key='BOXESOPENED')],
        [sg.Checkbox('Use my ip address for ease of use', default=False, key="use_ip")],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    regwin = sg.Window('BSU-Register', layoutregister)
    event, values = regwin.read(close=True)

    if event == 'Submit':
        legendaryChance = values['LEGENDARY']
        rareChance = values['RARE']
        superRareChance = values['SRARE']
        epicChance = values ['EPIC']
        mythicChance = values['MYTHIC']
        username = values['USERNAME']
        boxesOpened = values['BOXESOPENED']
        brawltag = values ['BRAWLTAG']
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
        chanceL3 = "chance="+ chance2
        chanceL4 = str(chanceL3)
        chancerare2 = repr(str(chanceR))
        chanceR3 = "chancerare=" + chancerare2
        chanceR4 = str(chanceR3)
        chanceSuperRare2 = repr(str(chanceSR))
        chanceSR3 = "chanceSuperRare="+chanceSuperRare2
        chanceSR4 = str(chanceSR3)
        chanceEpic2 = repr(str(chanceE))
        chanceE3 = "chanceEpic=" + chanceEpic2
        chanceE4 = str(chanceE3)
        chanceMythic2 = repr(str(chanceM))
        chanceM3 = "chanceMythic="+chanceMythic2
        chanceM4 = str(chanceM3)
        lobby1 = random.randint(1,5)
        Lobby1 = repr(str(lobby1))
        LOBBY1 = "brawlLobby1="+Lobby1
        LOBBY2 = str(LOBBY1)
        use_ip = values["use_ip"]
        use_ip2 = repr(str(use_ip))
        USE_IP = "brawlstatsip="+use_ip2
        USE_IP2 = str(USE_IP)
        bsusave =brawltag4 + "\n" + username4 + "\n" + chanceR4 + "\n" + chanceSR4 + "\n" + chanceM4 + "\n" + chanceL4 + "\n" + chanceE4
        settings = LOBBY2 + "\n" + USE_IP2
        Save = open("bsusave.py","w")
        Save.write(bsusave)
        Save.close()
        Save2 = open("settings.py", "w")
        Save2.write(settings)
        Save2.close()
        subprocess.run(["bash","register.sh"],check=True)
        exit(exitcode2)
    else:
        print('User cancelled')
        regwin.close()
        exit(exitcode2)
  
   
    
    
  
    
def loginbsu ():

    loginlayout =  [
        [sg.T("")], [sg.Text("Choose a file: "), sg.Input(key='FILEPATH', size=(45, 1)), sg.FileBrowse(file_types=(("BSU Files", "*.bsu"),))],[sg.Button("Submit")]
    ]

    loginwin = sg.Window("BSU-Login",loginlayout)
    while True:
        event, values = loginwin.read()
        if event  == sg.WIN_CLOSED or event == "Exit":
            break
        
        if event == "Submit":
            filepath = values["FILEPATH"]
            filepath2 = str(filepath)
            subprocess.run(["bash","login.sh",filepath2],check=True)
            break
    loginwin.close()
    exit(exitcode2)
layoutmenu = [
    [sg.Text("Login/Register Menu")],
    [sg.Button("Login")],
    [sg.Button("Register")],
    [sg.Button("QuickLogin")]
]



accwin = sg.Window('BSU-Login/Register', layoutmenu)
while True:
    event, values = accwin.read()
    if event == 'Login':
        loginbsu()
        break
    if event == 'Register':
        registerbsu()
    if event == sg.WIN_CLOSED:
        exit(exitcode2)
    if event == 'QuickLogin':
        if os.path.isfile('bsusave.py') and os.path.isfile('settings.py'):
            break
        else:
            print("Make sure you have logged in at least once")
            exit(exitcode2)

accwin.close()
from bsusave import chance, chancerare, chanceSuperRare, chanceEpic, chanceMythic
from settings import brawlLobby1
if brawlLobby1 == 1:
    typer.out("Lobby 1 has been picked\n")
if brawlLobby1 == 2:
    typer.out("Lobby 2 has been picked\n")
if brawlLobby1 == 3:
    typer.out("Lobby 3 has been picked\n")
optionslayout = [
    [sg.Text("Select from Utilities")],
    [sg.Button("Settings")],
    [sg.Button("Chance calculator")],
    [sg.Button("Brawl stats")],
    [sg.Button("Power point calculator")],
    [sg.Button("Save Maker")],
    [sg.Button("Update BSU")]
]
optionswin = sg.Window('BSU-Utilities',optionslayout)
while True:  
    event, values = optionswin.read(close=True)
    if event == 'Brawl stats':
        subprocess.run(["python", "brawlstats.py"], check=True)
    if event == 'Power point calculator':
        import powerpointcalc
        print(powerpointcalc)
    exit(exitcode2)
    if event == 'Update BSU':
        subprocess.run(["bash","updater.sh"],check=True)
    exit(exitcode2)
    if event == 'Settings':
       subprocess.run(["python", "brawlsettings.py"], check=True)
    exit(exitcode2)
    if event == 'Save Maker':
        print("This only works with files created with the power point calculator")
    time.sleep(5)
    subprocess.run(["bash","adder.sh"],check=True)
    exit(exitcode2)
    if event == 'Chance calculator':
        break
    if event == sg.WIN_CLOSED:
        exit(exitcode2)
optionswin.close()
    

window = tk.Tk()
window.title("Welcome to Brawl Stars Utilities")
window.geometry('250x250')
window.bind("<x>", lambda e: window.destroy())
if brawlLobby1 == 1:
    icon = ImageTk.PhotoImage(Image.open('brawl.png'))
    label = tk.Label(window, image=icon)
    label.place(x=0, y=0, relwidth=1, relheight=1)
if brawlLobby1 == 2:
    icon2 = ImageTk.PhotoImage(Image.open('brawl2.png'))
    label2 = tk.Label(window, image=icon2)
    label2.place(x=0, y=0, relwidth=1, relheight=1)
if brawlLobby1 == 3:
    icon3 = ImageTk.PhotoImage(Image.open('brawl3.png'))
    label3 = tk.Label(window, image=icon3)
    label3.place(x=0, y=0, relwidth=1, relheight=1)
lbl = Label(window,
            text="Legendary" + " " + str(chance) + percent,
            fg="yellow1",
            bg="yellow3")
lbl.grid(column=2, row=0)
lblrare = Label(window,
                text="Rare" + " " + str(chancerare) + percent,
                fg="green1",
                bg="green3")
lblrare.grid(column=2, row=2)
lblsuperRare = Label(window,
                     text="Super Rare" + " " + str(chanceSuperRare) + percent,
                     fg="cyan",
                     bg="blue4")
lblsuperRare.grid(column=2, row=3)
lblEpic = Label(window,
                text="Epic" + " " + str(chanceEpic) + percent,
                fg="purple2",
                bg="purple4")
lblEpic.grid(column=2, row=4)
lblMythic = Label(window,
                  text="Mythic" + " " + str(chanceMythic) + percent,
                  fg="red2",
                  bg="red4")
lblMythic.grid(column=2, row=5)
Currentchromatic = chance
lblcurrentc = Label(window,
                    text="Current chromatic" + ":" + str(Currentchromatic) +
                    percent,
                    fg="#F6EC48",
                    bg="#F56755")
lblcurrentc.grid(column=2, row=15)
Lastseasonc = chanceMythic
lbllastseasonc = Label(window,
                       text="Last season's chromatic" + ":" +
                       str(Lastseasonc) + percent,
                       fg="yellow1",
                       bg="pink4")
lbllastseasonc.grid(column=2, row=20)
window.mainloop()