import enquiries
import time
import os
import subprocess
import random
from replit import db
print("Warning:")
#power point calculator
PWR_PTS_LVL_1 = 0
PWR_PTS_LVL_2 = 20
PWR_PTS_LVL_3 = 30
PWR_PTS_LVL_4 = 50
PWR_PTS_LVL_5 = 80
PWR_PTS_LVL_6 = 130
PWR_PTS_LVL_7 = 210
PWR_PTS_LVL_8 = 340
PWR_PTS_LVL_9 = 550
PWR_PTS_LVL_10 = 0
#coin calculator
COINS_LVL_1 = 0
COINS_LVL_2 = 20
COINS_LVL_3 = 35
COINS_LVL_4 = 75
COINS_LVL_5 = 140
COINS_LVL_6 = 290
COINS_LVL_7 = 480
COINS_LVL_8 = 800
COINS_LVL_9 = 1250
COINS_LVL_10 = 0
print('#######################################')
def OPTIONS():
  return ['A:Add a new brawler','R:Remove a brawler.','D:Display brawlers.','U:Power Points & Coins required to next level','M:Power Points & Coins required to max level','E:Select all brawlers for a single action','L:Load brawlers from file.','Q:Quit Program','?: Print context menu.']
options = OPTIONS()
while True:
    action = enquiries.choose('Choose one of these options',options)
    if action == 'A:Add a new brawler':
        A = True
        brawlername = enquiries.freetext('Brawlers Name:')
        brawlernp = brawlername + 's' + ' '+ 'Power Level'+':'
        brawlerpowerlevel =enquiries.freetext(brawlernp)
        brawlerPL = brawlerpowerlevel
        if brawlerPL == '10':
            brawlerpowerpoints = 0
            while A is True:
                brawlerstarpowers = input("How many star powers does this brawler have?")
                brawlersp = ["0","1","2"]
                if brawlerstarpowers in brawlersp:
                    A = False
                else:
                   print("Error:The range is 0-2 and you inputted outside of that range")
                   time.sleep(1)
        if A is False:
            pass
        elif int(brawlerPL) <10:
            brawlerstarpowers = 0
            bob = True
            while bob is True:
                brawlerpowerpoints = str(input("How many power points does this brawler have?"))
                if int(brawlerpowerpoints) in range(851):
                    bob = False
                else:
                    print("Error:Outside of range(0-850)")
                    time.sleep(1)
    brawlerpowerpoints2= str(brawlerpowerpoints)
    brawlerPL2=str(brawlerPL)
    brawlerstarpowers2 =  str(brawlerstarpowers)
    db[brawlername]=brawlerpowerpoints2,brawlerPL2,brawlerstarpowers2
    if action == 'D:Display brawlers.':
         brawlerpowerpoints3 =   "Power Points = "+str(brawlerpowerpoints)
         db[brawlername] = 
         brawlerdb = enquiries.freetext('Type the name of the brawler you want to display')
         if  brawlername in brawlerdb:
             print(db[brawlername])
             pass
         else:
            print(brawlerdb,"does not exist")
            break
    if action == 'U:Power Points & Coins required to next level':
        brawlerdb2 = enquiries.freetext('Type the name of the brawler you would like to calculate')
        if brawlername in brawlerdb2:
            db[brawlername].get(brawlerPL2) 
        if brawlerPL == 1:
            neededpowerpoints =  PWR_PTS_LVL_1 
            print(neededpowerpoints) 
        if brawlerPL == 2:
            neededpowerpoints = PWR_PTS_LVL_2
        if brawlerPL == 3:
            neededpowerpoints = PWR_PTS_LVL_3
        if brawlerPL == 4:
            neededpowerpoints = PWR_PTS_LVL_4
        if brawlerPL == 5:
            neededpowerpoints = PWR_PTS_LVL_5
        if brawlerPL == 6:
            neededpowerpoints = PWR_PTS_LVL_6
        if brawlerPL == 7:
            neededpowerpoints = PWR_PTS_LVL_7
        if brawlerPL == 8:
            neededpowerpoints = PWR_PTS_LVL_8
        if brawlerPL == 9:
            neededpowerpoints = PWR_PTS_LVL_9
        if brawlerPL == 10:
            neededpowerpoints = PWR_PTS_LVL_10
    
    


         
            
          
             

 
    

