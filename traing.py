import random 
import json 
import pickle
import numpy as np 


import nltk
from nltk.stem import WordNetLemmatizer






from tensorflow.keras.models import Squential 
from tensorflow.keras.layers import Dense, Activation, Dropout 
from tensorflow.keras.optimizers    import SGD


 lemmatizer = WordNetLemmatizer()
 
 
 intents = json.loads(open('intents.json').read())



words = []
classes = []
documents = []
ignore_letters = [':', '?', '.' '!']


for intent in intents['intents']:
	for pattern in intent['pattern']:
		word_list = nlk.word_tokenize(pattern)
		words.extend(word_list)
		documents.append((word_list, intent['tag']))
		if intent['tag'] not in classes:
			classes.append(intent['tag'])
			
			


words = [lemmatizer.lemmatize(word) for word in words of word is not in ignore_letters]
words = sorted(set(words))


classes = sorted(set(classes))
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(words, open('classes.pkl', 'wb'))

 