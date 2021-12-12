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
from tkinter.filedialog import askopenfilename
typer.out("Welcome to Brawl Stars Utilities\n")
time.sleep(0.0000000001)
windowacc = tk.Tk()
windowacc.title("Login/Register Menu")
windowacc.geometry('500x500')
windowacc.bind("<x>", lambda e: window.destroy())
canvas1 = tk.Canvas(windowacc, width = 800, height = 600)
canvas1.pack()
def registerbsusubmit():
    subprocess.run(["bash","register.sh"],check=True)
    exit()
    
def registerbsu():
    regwin = tk.Tk()
    regwin.title("Login/Register Menu")
    regwin.geometry('500x500')
    tk.Label(regwin, text="Username").grid(row=0)
    tk.Label(regwin, text="Brawl Tag").grid(row=1)
    tk.Label(regwin, text="Rare chance").grid(row=2)
    tk.Label(regwin, text="Super rare chance").grid(row=3)
    tk.Label(regwin, text="Epic chance").grid(row=4)
    tk.Label(regwin, text="Mythic chance").grid(row=5)
    tk.Label(regwin, text="Legendary chance").grid(row=6)
    tk.Label(regwin, text="Number of boxes to be opened").grid(row=7)
    username = tk.Entry(regwin)
    brawltag = tk.Entry(regwin)
    rareChance = tk.Entry(regwin)
    superRareChance = tk.Entry(regwin)
    epicChance = tk.Entry(regwin)
    mythicChance = tk.Entry(regwin)
    legendaryChance = tk.Entry(regwin)
    boxesOpened= tk.Entry(regwin)
    username.grid(row=0, column=1)
    brawltag.grid(row=1, column=1)
    rareChance.grid(row=2, column=1)
    superRareChance.grid(row=3, column=1)
    epicChance.grid(row=4, column=1)
    mythicChance.grid(row=5, column=1)
    legendaryChance.grid(row=6, column=1)
    boxesOpened.grid(row=7, column=1)
    username1 = username.get()
    brawltag1 = brawltag.get()
    legendaryChance1 = legendaryChance.get()
    rareChance1 = rareChance.get()
    superRareChance1 = superRareChance.get()
    epicChance1 = epicChance.get()
    mythicChance1 = mythicChance.get()
    boxesOpened1= boxesOpened.get()
    brawltag2 = repr(str(brawltag1))
    username2 = repr(str(username1))
    username3 = "username="+ username2
    brawltag3 = "brawltag="+ brawltag2
    chanceL = 1 - ((1 - legendaryChance1)**boxesOpened1)
    chanceR = 1 - ((1 - rareChance1**boxesOpened1))
    chanceSR = 1 - ((1 - superRareChance1**boxesOpened1))
    chanceE = 1 - ((1 - epicChance1)**boxesOpened1)
    chanceM = 1 - ((1 - mythicChance1**boxesOpened1))
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
    submitbutton= tk.Button(text='Submit', command=registerbsusubmit)
    canvas1.create_window(200,180, window=submitbutton)
    regwin.mainloop()
def loginbsu ():
    subprocess.run(["bash","login.sh"],check=True)
    exit()
button1 = tk.Button(text='Login', command=loginbsu)
canvas1.create_window(200, 180, window=button1)
button2= tk.Button(text='Register', command=registerbsu)
canvas1.create_window(350, 180, window=button2)
windowacc.mainloop()
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
