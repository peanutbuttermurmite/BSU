import enquiries
import time
import os
import subprocess
import random
from easypydb import DB
token =os.getenv("token","default value")
DB2 = DB("brawlers",token)
DB3 = DB2
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
        brawlername = enquiries.freetext('Brawlers Name:')
        brawlernp = brawlername + 's' + ' '+ 'Power Level'+':'
        brawlerpowerlevel =enquiries.freetext(brawlernp)
        brawlerPL = brawlerpowerlevel
        if brawlerPL == '10':
            brawlerpowerpoints = 0
            while True:
                brawlerstarpowers = input("How many star powers does this brawler have?")
                brawlersp = ["0","1","2"]
                if brawlerstarpowers in brawlersp:
                    break
                else:
                   print("Error:The range is 0-2 and you inputted outside of that range")
                   time.sleep(1)
        elif int(brawlerPL) <10:
            brawlerstarpowers = 0
            while True:
                brawlerpowerpoints = int(input("How many power points does this brawler have?"))
                if brawlerpowerpoints in range(851):
                    break
                else:
                    print("Error:Outside of range(0-850)")
                    time.sleep(1)
    brawlerpowerpoints2=int(brawlerpowerpoints)
    brawlerPL2=int(brawlerPL)
    brawlerstarpowers2 = int(brawlerstarpowers)
    DB3[brawlername]=brawlerpowerpoints2,brawlerPL2,brawlerstarpowers2
print (DB3[brawlername])
if action == 'U:Power Points & Coins required to next level':
    print("Brawler power points")
    


         
            
          
             

 
    

