from tkinter import *
import os
import subprocess
import tkinter as tk
import time
import random
#asks user for their chances
legendaryChance = float(input("What is your legendary chance?"))
rareChance = float(input("What is your rare chance?"))
superRareChance = float(input("What is your super rare chance?"))
epicChance = float(input("What is your epic chance?"))
mythicChance = float(input("What is your mythic chance?"))
brawlpassseason = int(input("What is season you want to calculate?"))
boxesOpenedwithpass = 264
boxesOpenedwithoutpass=191
print("Type Yes if you have the brawl pass and type anything else if you don't ")
hasBrawlPass = input("Do you have the brawl pass?")
if hasBrawlPass == "Yes":

 chance = 1 - ((1 - legendaryChance)**boxesOpenedwithpass)
 print(chance, "%")
 percent = "%"
 chancerare = 1 - ((1 - rareChance**boxesOpenedwithpass))
 print(chancerare, "%")
 chanceSuperRare=1 - ((1 - superRareChance**boxesOpenedwithpass))
 print(chanceSuperRare,"%")
 chanceEpic=1 - ((1 - epicChance)**boxesOpenedwithpass)
 print(chanceEpic,"%")
 chanceMythic=1 - ((1 - mythicChance**boxesOpenedwithpass))
 print(chanceMythic, "%") 
else:
   chance = 1 - ((1 - legendaryChance)**boxesOpenedwithoutpass)
   print(chance, "%")
   percent = "%"
   chancerare = 1 - ((1 -    rareChance**boxesOpenedwithoutpass))
   print(chancerare, "%")
   chanceSuperRare=1 - ((1 -  superRareChance**boxesOpenedwithoutpass))
   print(chanceSuperRare,"%")
   chanceEpic=1 - ((1 - epicChance) **boxesOpenedwithoutpass)
   print(chanceEpic,"%")
   chanceMythic=1 - ((1 - mythicChance**boxesOpenedwithoutpass))
   print(chanceMythic, "%") 
   print("30 seconds until the program switches back to the main utility")
   time.sleep(30)
   