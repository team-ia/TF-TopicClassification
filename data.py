# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import csv
import json
stemmer = LancasterStemmer()

# 3 classes of training data

training_data = []

training_data.append({"class":"actualidad", "sentence":"covid 19"}) #1
training_data.append({"class":"actualidad", "sentence":"pandemia"})
training_data.append({"class":"actualidad", "sentence":"richard swing"})
training_data.append({"class":"actualidad", "sentence":"martín vizcarra"})
training_data.append({"class":"actualidad", "sentence":"black lives matter"})
training_data.append({"class":"actualidad", "sentence":"ni una menos"})
training_data.append({"class":"actualidad", "sentence":"random"})
training_data.append({"class":"actualidad", "sentence":"actualidad"})
training_data.append({"class":"actualidad", "sentence":"5g"})
training_data.append({"class":"actualidad", "sentence":"televisión"})
training_data.append({"class":"actualidad", "sentence":"twitter"})
training_data.append({"class":"actualidad", "sentence":"emprendimiento"})

training_data.append({"class":"hobbies", "sentence":"Bicicleta"})
training_data.append({"class":"hobbies", "sentence":"Música"})
training_data.append({"class":"hobbies", "sentence":"baile"})
training_data.append({"class":"hobbies", "sentence":"fútbol"})
training_data.append({"class":"hobbies", "sentence":"deportes"})
training_data.append({"class":"hobbies", "sentence":"netflix"})
training_data.append({"class":"hobbies", "sentence":"series"})
training_data.append({"class":"hobbies", "sentence":"dibujo"})
training_data.append({"class":"hobbies", "sentence":"manualidades"})
training_data.append({"class":"hobbies", "sentence":"programacion"})
training_data.append({"class":"hobbies", "sentence":"libros"})
training_data.append({"class":"hobbies", "sentence":"escribir"})

training_data.append({"class":"comida", "sentence":"restaurantes"})
training_data.append({"class":"comida", "sentence":"comida"})
training_data.append({"class":"comida", "sentence":"tacos"})
training_data.append({"class":"comida", "sentence":"pizza"})
training_data.append({"class":"comida", "sentence":"master chef"})
training_data.append({"class":"comida", "sentence":"postres"})
training_data.append({"class":"comida", "sentence":"salchipapa"})
training_data.append({"class":"comida", "sentence":"pollo brasa"})
training_data.append({"class":"comida", "sentence":"hamburguesas"})
training_data.append({"class":"comida", "sentence":"menu"})
training_data.append({"class":"comida", "sentence":"cafe"})
training_data.append({"class":"comida", "sentence":"sandwich"})

training_data.append({"class":"juegos", "sentence":"among us"})
training_data.append({"class":"juegos", "sentence":"the last of us"})
training_data.append({"class":"juegos", "sentence":"fall guys"})
training_data.append({"class":"juegos", "sentence":"zelda"})
training_data.append({"class":"juegos", "sentence":"league of legend"})
training_data.append({"class":"juegos", "sentence":"dota 2"})
training_data.append({"class":"juegos", "sentence":"gta v"})
training_data.append({"class":"juegos", "sentence":"free fire pc"})
training_data.append({"class":"juegos", "sentence":"overwatch"})
training_data.append({"class":"juegos", "sentence":"fornite"})
training_data.append({"class":"juegos", "sentence":"juegos"})
training_data.append({"class":"juegos", "sentence":"mario bros"})

def data_actualidad():
    actual_list=[]
    with open('data_cleared/actualidad.json', encoding="utf8") as actJson:
        actual=json.load(actJson)
        
    for item in actual:
        data={"class":None,"sentence":None}
        data['class']="actualidad"
        data['sentence']=item["nombre"]
        training_data.append(data)


def data_games():
    actual_list=[]
    with open('data_cleared/game_cleared.json', encoding="utf8") as actJson:
        actual=json.load(actJson)
        
    for item in actual[:80]:
        data={"class":None,"sentence":None}
        data['class']="juegos"
        data['sentence']=item["nombre"]
        training_data.append(data)

def data_food():
    food_list=[]
    with open('data_cleared/food_esp.csv', encoding="utf8") as foodCsv:
        csv_reader=csv.reader(foodCsv,delimiter=',')
        contador=0
        for row in csv_reader:
            contador=contador+1
            if contador is 80:break
            data={"class":None,"sentence":None}
            data['class']="comida"
            data['sentence']=row[0]
            training_data.append(data)
         
def data_hobbie():
    with open('data_cleared/hobbies.json', encoding="utf8") as hobbiesJson:
        actual=json.load(hobbiesJson)
        
    for item in actual[:80]:
        data={"class":None,"sentence":None}
        data['class']="hobbies"
        data['sentence']=item
        training_data.append(data)
             
# loop through each sentence in our training data
def init_data(words, classes, documents, ignore_words):
    
    print ("%s sentences in training data" % len(training_data))
    for pattern in training_data:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern['sentence'])
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, pattern['class']))
        # add to our classes list
        if pattern['class'] not in classes:
            classes.append(pattern['class'])

    # stem and lower each word and remove duplicates
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words = list(set(words))

    # remove duplicates
    classes = list(set(classes))

    print (len(documents), "documents")
    print (len(classes), "classes", classes)
    print (len(words), "unique stemmed words", words)

def init_training_data(training, output, words, classes, documents):

    # create an empty array for our output
    output_empty = [0] * len(classes)

    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # stem each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create our bag of words array
        for w in words:
            print(w)
            bag.append(1) if w in pattern_words else bag.append(0)

        training.append(bag)
        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        output.append(output_row)

# sample training/output
#i = 2
#w = documents[i][0]
#print ([stemmer.stem(word.lower()) for word in w])
#print (training[i])
#print (output[i])

