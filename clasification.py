import numpy as np
import json
import neural_network as nn
import data as data

# probability threshold
ERROR_THRESHOLD =0.2



# load our calculated synapse values
synapse_file = 'synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])
    classes = np.asarray(synapse['classes'])
    words = np.asarray(synapse['words'])
   
def classify(sentence, show_details = False):
    results = nn.think(words, synapse_0, synapse_1, sentence, show_details)
    results = [[i,r] for i, r in enumerate(results) if r > ERROR_THRESHOLD ] 
    results.sort(key = lambda x: x[1], reverse = True) 
    return_results =[[classes[r[0]], r[1]] for r in results]
    print ("%s \n classification: %s" % (sentence, return_results))
    print()
    return return_results

# Todo en minúscula

classify("among us")
classify("among us 2")
classify("restaurant")
classify("restaurantes conocidos")
classify("animes")
classify("lucifer")
classify("covid 19")
classify("profesores")
classify("tele")
classify("dota 2")
classify("platano")
classify("guitarra")
classify("Thanos")
classify("hamburguesa")
classify("alimento")
classify("frijol")