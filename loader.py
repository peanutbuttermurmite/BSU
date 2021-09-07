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
Currentchromatic = chance - 0
lblcurrentc = Label(window,
                    text="Current chromatic" + ":" + str(Currentchromatic) +
                    percent,
                    fg="#F6EC48",
                    bg="#F56755")
lblcurrentc.grid(column=2, row=15)
Lastseasonc = chanceMythic - 0
lbllastseasonc = Label(window,
                       text="Last season's chromatic" + ":" +
                       str(Lastseasonc) + percent,
                       fg="yellow1",
                       bg="pink4")
lbllastseasonc.grid(column=2, row=20)
window.mainloop()
