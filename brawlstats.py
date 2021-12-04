import os
from dotenv import load_dotenv
import brawlstats as brawl
import pandas as pd
try:
    load_dotenv()
    TOKEN = os.getenv("BRAWL_TOKEN")
    client = brawl.Client(TOKEN)
    player = client.get_player("2GGYGV8YQ")
    print("Connected successfully and returned player: ",player.name)
except:
    print("an error occured with connection")
df = pd.DataFrame(player.brawlers)#read the brawlers list from my player data
df.drop(columns=['id'], inplace=True)#drop the brawler id columns
df = df[['name','trophies','gadgets','power', 'highest_trophies',   'rank', 'star_powers', ]]#reorder columns
for index, row in df.iterrows():#loop through the dataframe
    dicList = row["gadgets"]#get the list from the column
    for i in range(len(dicList)):#loop through the list
        if(type(dicList[i])!= str):#if the list item is a dictionary and not a string
            item = dicList[i]['name']#get the name from the dictionary
            dicList[i] = item#replace the list with just the name
    df.at[index,'gadgets'] = dicList#update the dataframe with the new list
    powerList = row["star_powers"]#DO THE SAME FOR GADGETS
    for i in range(len(powerList)):
        if(type(powerList[i])!= str):
            item = powerList[i]['name']
            powerList[i] = item
    df.at[index,'star_powers'] = powerList
df.sort_values(by=['trophies'], ascending=False)#sort by trophies, highest-lowest
#edit the dataframe to contain only necessary information
maxTrophies = 550
estimateDF = df.copy()
estimateDF.drop(columns=['star_powers','rank','highest_trophies'], inplace=True)
for index, row in estimateDF.iterrows():#loop through the dataframe
    gagExist = 0
    gList = row["gadgets"]#get the list from the column
    if(len(gList)>0):
        gagExist = 1
    estimateDF.at[index,'gadgets'] = gagExist
#find the estimate and insert it into the dataframe
for index, row in estimateDF.iterrows():
    powerLevel = row['power']
    gagExist = row["gadgets"]
    troph = row['trophies']
    estimate = ((powerLevel-1)+gagExist)/10
    trophyEstimate = estimate * maxTrophies
    estimateDF.at[index,'trophyEstimate'] = trophyEstimate
    estimateDF.at[index,'trophyError'] = troph-trophyEstimate
estimateDF.sort_values(by=['trophyError'])#sort by error, most-least
