import json
import csv
import time
from pytrends.request import TrendReq
from googletrans import Translator
import pandas as pd
import requests
import sys

translator = Translator()
pytrends = TrendReq(hl='es-PE', tz=360)
game_list=[]



def transalate_hobbys():
    with open('hobbies.csv') as hobbiesCsv:
        csv_reader=csv.reader(hobbiesCsv,delimiter=',')
        hobbie_list=[]
        
        for row in csv_reader:
            try:
                #print(row)
                hobbie=translator.translate(row[0], src='en', dest='es').text
                print(hobbie)

                hobbie_list.append(hobbie)
                with open('hobbies.json', 'w') as outfile:
                 json.dump(hobbie_list,outfile)
            except:
                translator = Translator()
                continue
    with open('hobbies.json', 'w') as outfile:
        json.dump(hobbie_list,outfile)
        
        
def read_games_api():
    for i in range(500):
        response = requests.get("https://api.rawg.io/api/games?9347941d52e24e478689b1c5a1536710=key&page="+str(i+1))
        games=response.json()
        #print(games)
        for item in games["results"]:
            game_detail={'nombre':None}
            game_detail['nombre']=item['name']
            game_list.append(game_detail)
    print(game_list)
    with open('game_cleared.json', 'w') as outfile:
        json.dump(game_list,outfile)
            
    
    
def read_games_dataset():
    with open('games.json', encoding="utf8") as gamesJson:
        games=json.load(gamesJson)
        
    for item in games['results']:
        game=item['name']
        game_list.append(game)
    


def read_food_dataset():
    food_list=[]
    with open('data_used/food.json', encoding="utf8") as foodJson:
        food=json.load(foodJson)
    with open('food_cleared.csv',mode='w') as outfile:     
        for item in food:
            f_writer=csv.writer(outfile, delimiter=',', quotechar=" ", quoting=csv.QUOTE_MINIMAL)
            f_writer.writerow([item['word']])
           # food_item={"nombre":None}
            #food_item['nombre']=item['word']
            #food_list.append(food_item) 
    #print(food_list)

    #    json.dump(food_list,outfile)
      #  print(food_list)       
    
    
dataset = []  
def actualidad_dataset():
 
     dataset=pytrends.top_charts(2009, hl='es', tz=300, geo='PE').values.tolist()
  
     dataset+=pytrends.top_charts(2011, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2012, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2014, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2013, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2015, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2016, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2017, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2018, hl='es', tz=300, geo='PE').values.tolist()
     dataset+=pytrends.top_charts(2019, hl='es', tz=300, geo='PE').values.tolist()
     word_list=[]
     for items in dataset:
         words={"nombre":None}
         words['nombre']=items[0]
         word_list.append(words)
         
     with open('actualidad.json', 'w') as outfile:
        json.dump(word_list,outfile)
     print(word_list)
  
def mainP():
  #  read_games_dataset()
    read_food_dataset()
    #read_games_api()
#transalate_hobbys()
   # actualidad_dataset()
mainP()