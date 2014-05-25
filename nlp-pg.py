"""
Author: Amrita Ray
May 21 2014
Natural language pre-processing library in Python ('nltk') has been used 
to process the text descriptions to retrieve feature vector.
"""

from __future__ import division
import nltk
import csv
import random
import numpy
import sys
import operator
from nltk.tag import pos_tag

#def set_trace():
#        from IPython.core.debugger import Pdb
#        import sys
#        Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)

text = open('fitness_pre-processed_TEXT(2820).txt', 'r')
textread = text.readlines()

label = open('fitness_Label_DATA_nlp.txt', 'r')
labelread = label.readlines()

# random 75% of the data in training set
trainid = random.sample(range(0,len(textread)),int(round(len(textread)*0.75,0)))

testid = []
trainlabel = []
testlabel = []

for i in range(0, len(textread)):
  if i in trainid:
    trainlabel.append(labelread[i])
  else:
    testid.append(i)
    testlabel.append(labelread[i])

dict = {}

for li in range(0, len(textread)):  
#  print "processing line number " + str(li)
  line = textread[li]
  tagged_sent = pos_tag(line.split())
  #nounverb = [word for word,pos in tagged_sent if pos == 'VB' or pos == 'NN' or pos == 'NNS' or pos == 'VBD']
  nounverb = [word for word,pos in tagged_sent if pos == 'NN' or pos == 'NNS']
  for j in nounverb :
    if j in dict.keys():
      dict[j] += 1
    else :
      dict[j] = 1 

param = sys.argv[1]

# thresholding
dict_select = {}
for k in dict.keys():
  if dict[k] > int(param):
    dict_select[k] = dict[k]

writer = csv.writer(open('trainid.csv', 'wb'))
writer.writerow(trainid)

writer = csv.writer(open('testid.csv', 'wb'))
writer.writerow(testid)

writer = csv.writer(open('dict.csv', 'wb'))
for w in dict_select:
   writer.writerow([w, dict_select[w]])

"""
Once you get the dictionary for words in training set dict_train, 
check each text in training that matches with dict_train.key()
"""

allwords = []

for num in range(0, len(textread)):
  line = textread[num]
  print "word for line " + str(num)
  tagged_sent = pos_tag(line.split())
  nounverb = [word for word,pos in tagged_sent if pos == 'NNS' or pos == 'NN']
  lineprop = []
  for word in dict_select.keys():  
    Nword = nounverb.count(word)
    if len(nounverb) > 0:
      lineprop.append(100*(Nword/len(nounverb)))
    else:
      lineprop.append(0)
  allwords.append(lineprop)

with open('allwords.csv', "wb") as f:
	writer = csv.writer(f)
	writer.writerows(allwords)    

