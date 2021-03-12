from tkinter import *
import os
import subprocess
import tkinter as tk
import time
import random
print("Welcome to Brawl Stars Utilities") 
time.sleep(0.0000000001)
brawlLobby1 = random.randint(1,5)
if brawlLobby1 == 1:
    print("More lobbies coming soon")
mobileorpc = input('enter mobile or pc to perform optimisations for your device:')
password = input("Enter bp to receive info based on the brawl pass or type anything else to see your chances in fancy tkinter style (may be slightly inaccurate):")
if password == 'bp':
    subprocess.run(["python","brawlpass.py"], check=True)
print("Chances for all rarities can be seen when pressing the info icon on a big or mega box in the shop when tapping on a big or mega box in the shop.")
legendaryChance = float(input("What is your legendary chance?"))
rareChance = float(input("What is your rare chance?"))
superRareChance = float(input("What is your super rare chance?"))
epicChance = float(input("What is your epic chance?"))
mythicChance = float(input("What is your mythic chance?"))
boxesOpened = int(input("How many boxes do you want to open?"))
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
bigboxes = boxesOpened/3
megaboxes =boxesOpened/10
print("Y/N")
convert = input("Convert normal boxes to big and mega boxes?")
if convert == "Y":
  print("",megaboxes,"Mega Boxes",",","or",bigboxes,"bigboxes")
if mobileorpc == 'pc':
 window = tk.Tk()
 window.title("Welcome to Brawl Stars Utilities")
 window.geometry('250x250')
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
print("Loading...")
time.sleep(0.1)
print("10%")
time.sleep(1.1)
print("50%")
time.sleep(1.8)
print("90%")
time.sleep(0.5)
print("Loaded")
time.sleep(0.1)
subprocess.run(["gcc","main.c"], check=True)
tmp = subprocess.run(["./a.out"])  
print(tmp)
