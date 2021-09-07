from tkinter import *
import os
import subprocess
import tkinter as tk
import time
import random
import typer
from tkinter import messagebox
from PIL import Image, ImageTk
from replit import audio
import enquiries
import turtle
from goto import goto 
typer.out("Welcome to Brawl Stars Utilities\n")
time.sleep(0.0000000001)
brawlLobby1 = random.randint(1, 5)
if brawlLobby1 == 1:
    typer.out("You got lobby 1\n")
if brawlLobby1 == 2:
    typer.out("You got lobby 2\n")
if brawlLobby1 == 3:
    typer.out("You got lobby 3\n")
username = input("Enter your username:")
brawltag = input("Enter your brawl stars tag:")
brawltag2 = repr(str(brawltag))
username2 = repr(str(username))
username3 = "username="+ username2
brawltag3 = "brawltag="+ brawltag2
Save = open("save1.bsu","w")
Save.write(username3)
options = [
    'Chance Calculator', 'Brawl stats', 'Power point calculator', 'Settings',
    'Battle Pass Calc', 'Update', 'Load save'
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
    subprocess.run(["bash","updater.sh"])
    exit()
if choice == 'Settings':
    subprocess.run(["python", "brawlsettings.py"], check=True)
    exit()
print("Warning:Do not type Y if you have not created a .bsu file yet")
nosave = input("Type Y to skip the creation of the .bsu file:")
if nosave == "Y":
    goto(98)
print("Chances for all rarities can be seen when pressing the info icon on a big or mega box in the shop when tapping on a big or mega box in the shop.")
legendaryChance = float(input("What is your legendary chance?"))
rareChance = float(input("What is your rare chance?"))
superRareChance = float(input("What is your super rare chance?"))
epicChance = float(input("What is your epic chance?"))
mythicChance = float(input("What is your mythic chance?"))
boxesOpened = int(input("How many boxes do you want to open?"))
print("Your chances are displayed below")
chance = 1 - ((1 - legendaryChance)**boxesOpened)
print(chance, "%")
percent = "%"
chancerare = 1 - ((1 - rareChance**boxesOpened))
print(chancerare, "%")
chanceSuperRare = 1 - ((1 - superRareChance**boxesOpened))
print(chanceSuperRare, "%")
chanceEpic = 1 - ((1 - epicChance)**boxesOpened)
print(chanceEpic, "%")
chanceMythic = 1 - ((1 - mythicChance**boxesOpened))
print(chanceMythic, "%")
chance2 = repr(str(chance))
chance3 = "chance="+ chance2
chancerare2 = repr(str(chance))
chancerare3 = "chancerare=" + chancerare2
chanceSuperRare2 = repr(str(chanceSuperRare))
chanceSuperRare3 = "chanceSuperRare=" +chanceSuperRare2
chanceEpic2 = repr(str(chance))
chanceEpic3 = "chanceEpic=" + chanceEpic2
chanceMythic2 = repr(str(chance))
chanceMythic3 = "chanceMythic="+chanceMythic2
bsusave ="\n"+brawltag3 + "\n"+ chancerare3 + "\n" + chanceSuperRare3 +"\n"+chanceSuperRare3 + "\n" + chanceMythic3 + "\n" + chance3
bigboxes = boxesOpened / 3
megaboxes = boxesOpened / 10
Save.write(str(bsusave))
Save.close()
print("Y/N")
convert = input("Convert normal boxes to big and mega boxes?")
if convert == "Y":
    print("", megaboxes, "Mega Boxes", ",", "or", bigboxes, "bigboxes")
savename = subprocess.run(["bash","findbsu.sh"])
def get_var(varname):
    CMD = 'echo $(source findbsu.sh; echo $%s)' % varname
    p = subprocess.Popen(CMD, stdout=subprocess.PIPE, shell=True, executable='/bin/bash')
    return p.stdout.readlines()[0].strip()
savename2=get_var("findbsu")
saveloader = input("Do you have a .bsu file in this directory?(Type Y for Yes or N for No")
if saveloader == 'Y':
    with open(savename2) as infile:
     exec(infile.read())
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
