#  Assignment-2 AIT-690
# This project is done by Meena Rapaka, Siva Naga Lakshmi Karamsetty, Ying Ke
# In the below program, we are generating random sentences
# 1. Using the argparse library, we accept arguments
# 2. We tokenize sentences and detect boundaries and tokenize from the sentences, using the text file
# 3. Based on the tokens, we generate tokens
# 4. We then calculate frequency and probability of count of the words in sentences
# 5. Store the key, value pairs and then generate random sentences based on the count of probabilities
# We run this file on the command prompt using: filename.py
# Eg: ngram.py 3 10 filename.txt(filename for the text file can be ABC.txt)








#Importing the libraries
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
import random
import numpy as np
from nltk import ngrams, FreqDist, ConditionalFreqDist, trigrams
from collections import defaultdict
import argparse


parser = argparse.ArgumentParser()#argument parser is used for the code to run on the terminal
parser.add_argument("n",type = int, help = "Enter n-gram")#it takes n-gram value as input
parser.add_argument("m",type = int,help = "Enter no. of sentences you want")# it takes m value as input
parser.add_argument("text",type = str, nargs='+',help = "Enter text file path or whole text file")
args = parser.parse_args()

gram = {}

B=""
#Loops around filename
for i in range(0,len(args.text)): 
    A = open(args.text[i], 'rt', encoding="utf8")
    B=B+" "+A.read()
    B=B.lower()

#The text is tokenized here.
count=sent_tokenize(B)

gram1=[]
i=0
#This loop is for the n-gram generation.
while i<len(count):
    gram = nltk.ngrams(word_tokenize(count[i]),args.n,pad_left=True,pad_right=True)
    gram1.insert(len(gram1),gram)
    i = i + 1
words_list=[]

for X in gram1:
    for Y in X:
      words_list.append(Y)

#The below model calculates the frequency and the probabiltiy of the words
model = {}
model = defaultdict(lambda:defaultdict(lambda:0))
for i in words_list:
    model[(i[:-1])][i[-1]] += 1
for words in model:
    total_count = float(sum(model[words].values()))
    for last in model[words]:
        model[words][last] /= total_count

#Boundaries are defined to generate complete sentences based on the probabilties gained from the
# model, which are stored as key or value-pairs.
#Value pairs will be use to generate sentences.

#Using the while loop, we generate sentences using the switch key based on the probabilities.
#Then randomly generates the sentences using the random function, based on the n-gram key.
#The tuples will be appended and it checks for the stop words(.,?,!) which we used and then statement is ended.
# the loop will iterates till the m-value is reached or satisfied.
i=0
while i <args.m:  
        
    switch = {1 : (),2 : (None,),3 : (None,None),4 : (None,None,None),5 : (None,None,None,None),6 : (None,None,None,None,None)}
    first_key=switch[args.n]
    sentence = []
    c1 = 0
    while (c1 < 100):
        value = list(model[first_key].values())
        key1 = list(model[first_key].keys())
        value1 = np.cumsum(value)
        nGramkey = dict(zip(key1, value1))
        k = random.uniform(0, 1)
        for key in nGramkey:
            if k <= nGramkey[key]:
                break
        sentence.append(key)
        next_key = first_key[1:] + tuple([key])
        first_key = next_key
        if key == "." or key =="?" or key =="!":
            break
        c1 += 1
    i=i+1    
    print("\n")
    print(' '.join(sentence))
print("\nThankYou\n")
print("This Program is done by Meena rapaka, K.Siva Naga Lakshmi, Ying ke")
 
#we used the below reference to build our n-gram probability model-https://nlpforhackers.io/language-models/
