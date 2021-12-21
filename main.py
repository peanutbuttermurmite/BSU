from tkinter import *
import os
import subprocess
import tkinter as tk
import time
import random
import typer
from tkinter import messagebox
from PIL import Image, ImageTk
import enquiries
import turtle
import PySimpleGUI as sg
typer.out("Welcome to Brawl Stars Utilities\n")
time.sleep(0.0000000001)
def registerbsu():
<<<<<<< HEAD
=======

>>>>>>> c435b7fcc0ab280a00c34b24ac3cd0f7d858f094
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
<<<<<<< HEAD
        brawltag = values ['BRAWLTAG']
        chanceL = 1 - (1 - int(legendaryChance)**int(boxesOpened))
        chanceR = 1 - (1 - int(rareChance)**int(boxesOpened))
        chanceSR = 1 - (1 - int(superRareChance)**int(boxesOpened))
        chanceE = 1 - (1 - int(epicChance)**int(boxesOpened))
        chanceM = 1 - (1 - int(mythicChance)**int(boxesOpened))
=======
        chanceL = 1 - ((1 - legendaryChance)**boxesOpened)
        chanceR = 1 - ((1 - rareChance**boxesOpened))
        chanceSR = 1 - ((1 - superRareChance**boxesOpened))
        chanceE = 1 - ((1 - epicChance)**boxesOpened)
        chanceM = 1 - ((1 - mythicChance**boxesOpened))
>>>>>>> c435b7fcc0ab280a00c34b24ac3cd0f7d858f094
        username2 = repr(str(username))
        username3 = "username=" + username2
        brawltag2 = repr(str(brawltag))
        brawltag3 = "brawltag=" + brawltag2
        chance2 = repr(str(chanceL))
        chanceL3 = "chance="+ chance2
        chancerare2 = repr(str(chanceR))
        chanceR3 = "chancerare=" + chancerare2
        chanceSuperRare2 = repr(str(chanceSR))
        chanceSR3 = "chanceSuperRare=" +chanceSuperRare2
        chanceEpic2 = repr(str(chanceE))
        chanceE3 = "chanceEpic=" + chanceEpic2
        chanceMythic2 = repr(str(chanceM))
        chanceM3 = "chanceMythic="+chanceMythic2
        bsusave ="\n" + brawltag3 + "\n" + username3 + "\n" + chanceR3 + "\n" + chanceSR3 + "\n" + chanceM3 + "\n" + chanceL3 + "\n" + chanceE3
        Save = open("bsusave.py","w")
        Save.write(bsusave)
        Save.close()
        subprocess.run(["bash","register.sh"],check=True)
        exit()

        print("Your mythic chance was",values['mythicChance'])
    else:
        print('User cancelled')
        regwin.close()
  
   
    
    
  
    
def loginbsu ():
<<<<<<< HEAD

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
         

=======
    subprocess.run(["bash","login.sh"],check=True)
    exit()
>>>>>>> c435b7fcc0ab280a00c34b24ac3cd0f7d858f094
layoutmenu = [
    [sg.Text("Login/Register Menu")],
    [sg.Button("Login")],
    [sg.Button("Register")],
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
        break
accwin.close()
brawlLobby1 = random.randint(1, 5)
if brawlLobby1 == 1:
    typer.out("You got lobby 1\n")
if brawlLobby1 == 2:
    typer.out("You got lobby 2\n")
if brawlLobby1 == 3:
    typer.out("You got lobby 3\n")
options = [
    'Chance Calculator', 'Brawl stats', 'Power point calculator', 'Settings',
    'Battle Pass Calc', 'Update', 'Save Maker'
]
choice = enquiries.choose('Choose one of these options:', options)
print(choice, "was selected")
if choice == 'Brawl stats':
    subprocess.run(["python", "brawlstats.py"], check=True)
if choice == 'Power point calculator':
    import powerpointcalc
    exit()
if choice == 'Battle Pass Calc':
    subprocess.run(["python", "brawlpass.py"], check=True)
    exit()
if choice == 'Update':
    subprocess.run(["bash","updater.sh"],check=True)
    exit()
if choice == 'Settings':
    subprocess.run(["python", "brawlsettings.py"], check=True)
    exit()
if choice == 'Save Maker':
    print("This only works with files created with the power point calculator")
    time.sleep(5)
    subprocess.run(["bash","adder.sh"],check=True)

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
