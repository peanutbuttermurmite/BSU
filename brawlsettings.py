from tkinter import *
import os
import subprocess
import tkinter as tk
import time
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from easypydb import DB
from replit import audio
import enquiries
import turtle
token = os.getenv("token")
db1=DB("myBrawl",token)
print("Welcome to Brawl Stars Utilities S") 
time.sleep(0.0000000001)
brawlLobby1 = input("Input the background number you would like:1/2/3:")
mobileorpc = input('enter mobile or pc to perform optimisations for your device:')
databaseuser = input("To skip the inputs, enter your username:")
username =input("Enter your username:")
password = input("Enter bp to receive info based on the brawl pass or type anything else to see your chances in fancy tkinter style (may be slightly inaccurate):")
if password == 'bp':
    subprocess.run(["python","brawlpass.py"], check=True)
    exit()
options = ['Chance Calculator', 'Brawl stats', 'Power point calculator']
choice = enquiries.choose('Choose one of these options:', options)
print(choice, "was selected")
if choice == 'Brawl stats':
    subprocess.run(["python","brawlstats.py"],check=True)
if choice == 'Power point calculator':
    import powerpointcalc
    exit() 
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
chanceSuperRare=1 - ((1 - superRareChance**boxesOpened))
print(chanceSuperRare,"%")
chanceEpic=1 - ((1 - epicChance)**boxesOpened)
print(chanceEpic,"%")
chanceMythic=1 - ((1 - mythicChance**boxesOpened))
print(chanceMythic, "%")
db1[username]=chance,chancerare,chanceEpic,chanceSuperRare, chanceMythic
db1.autoload=True
print(db1[username])
bigboxes = boxesOpened/3
megaboxes =boxesOpened/10
print("Y/N")
convert = input("Convert normal boxes to big and mega boxes?")
if convert == "Y":
  print("",megaboxes,"Mega Boxes",",","or",bigboxes,"bigboxes")
if mobileorpc == 'mobile':
 subprocess.run(["gcc","main.c"], check=True)
 tmp = subprocess.run(["./a.out"])  
 print(tmp)
 exit()
window = tk.Tk()
source = audio.play_file("brawlmusic1.mp3")
volume = 1
loops = 1
window.title("Welcome to Brawl Stars Utilities")
window.geometry('250x250')
if brawlLobby1 == 1:
  icon = ImageTk.PhotoImage(Image.open('brawl.png'))
  label = tk.Label(window, image = icon)
  label.place(x=0, y=0, relwidth=1, relheight=1)
if brawlLobby1 == 2:
 icon2 = ImageTk.PhotoImage(Image.open   ('brawl2.png'))
 label2 = tk.Label(window, image = icon2)
 label2.place(x=0 , y=0, relwidth=1, relheight=1)
if brawlLobby1 == 3:
 icon3 = ImageTk.PhotoImage(Image.open('brawl3.png'))
 label3 = tk.Label(window, image = icon3)
 label3.place(x=0, y=0, relwidth=1, relheight=1)
lbl = Label(window, text="Legendary"+" "+str(chance)+percent, fg="yellow1",bg="yellow3")
lbl.grid(column=2, row=0)
lblrare = Label(window, text="Rare"+" "+str(chancerare)+percent,fg="green1",bg="green3")
lblrare.grid(column=2, row=2)
lblsuperRare = Label(window, text="Super Rare"+" "+str(chanceSuperRare)+percent,fg="cyan",bg="blue4")
lblsuperRare.grid(column=2, row=3)
lblEpic = Label(window, text="Epic"+" "+str(chanceEpic)+percent,fg="purple2",bg="purple4") 
lblEpic.grid(column=2,row=4)
lblMythic= Label(window, text="Mythic"+" "+str(chanceMythic)+percent,fg="red2",bg="red4") 
lblMythic.grid(column=2,row=5)
Currentchromatic = chance - 0 
lblcurrentc = Label(window, text="Current chromatic"+":"+str(Currentchromatic)+percent,fg="#F6EC48",bg="#F56755")
lblcurrentc.grid(column=2,row=15)        
Lastseasonc = chanceMythic-0
lbllastseasonc=Label(window, text="Last season's chromatic"+":"+str(Lastseasonc)+percent,fg="yellow1",bg="pink4")
lbllastseasonc.grid(column=2, row=20)
window.mainloop()                                
